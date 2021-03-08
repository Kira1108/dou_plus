import sys
import os
sys.path.append('..')
from config import DB_CONN_INFO,DB_URI
import pymysql
import pandas as pd
import sqlalchemy
import logging

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

USER_STATS_SQL = """select l.id,
    sum(l.sales_volume) as total_volume,
    count(distinct l.uid) as num_lives,
    sum(l.total_viewer) as total_viewer,
    avg(l.total_viewer) as avg_viewer,
    max(l.max_viewer) as max_viewer,
    g.goods_count as total_goods_count,
    g.total_sales_money as live_sales_money,
    g.total_sales_money / count(distinct l.uid) as avg_live_sales_money
from base_live l
left join (
    select id,
        count(distinct goods_id) as goods_count,
        sum(sales_price) as total_sales_money,
        sum(sales_count) as total_sales_count
    from base_live_goods
    group by id
) g on l.id = g.id
group by l.id
order by g.total_sales_count desc"""

TAG_SQL = '''select id, tag, sum(sales_count) as scount from base_live_goods
group by id, tag'''

TABLE_NAME = 'blogger_stats'

def user_stats():
    logging.info("Running user statistics pipeline")
    connection = pymysql.connect(**DB_CONN_INFO)
    df = pd.read_sql_query(USER_STATS_SQL, connection)
    connection.close()
    return df

def user_tags():
    logging.info("Running user tags pipeline")
    connection = pymysql.connect(**DB_CONN_INFO)
    df = pd.read_sql_query(TAG_SQL, connection)
    connection.close()

    blogger_tags = df.sort_values(by = ['id','scount'],ascending = False)\
    .groupby('id')\
    .head(3)\
    .groupby('id')['tag'].apply(lambda x:list(x))

    blogger_tags = pd.DataFrame(blogger_tags)['tag'].apply(lambda x: [xx for xx in x if xx != '']).reset_index()
    blogger_tags['tag'] = blogger_tags['tag'].apply( lambda x: ','.join(x))
    return blogger_tags

def run_pipeline():
    engine = sqlalchemy.create_engine(DB_URI)
    df = user_stats().merge(user_tags(), on = 'id', how = 'left')
    df.to_sql(TABLE_NAME, con = engine, index = False, if_exists = 'replace')
    logging.info('User stats completed')


if __name__ == '__main__':
    run_pipeline()
