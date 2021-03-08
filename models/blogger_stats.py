from db import db

class BloggerStatsModel(db.Model):

    __tablename__ = "blogger_stats"

    id = db.Column(db.String(50), primary_key=True)
    total_volume = db.Column(db.Float)
    num_lives = db.Column(db.BigInteger)
    total_viewer = db.Column(db.Float)
    avg_viewer = db.Column(db.Float)
    max_viewer = db.Column(db.Float)
    total_goods_count = db.Column(db.Float)
    live_sales_money = db.Column(db.Float)
    avg_live_sales_money = db.Column(db.Float)
    tag = db.Column(db.String(50))


    def __repr__(self):
        return '<BloggerStats %r>' % self.name

    @classmethod
    def get_by_id(cls, id_):
        return cls.query.filter_by(id = id_).first()

    @classmethod
    def getn(cls, n):
        return cls.query.limit(n)

    def json(self):
        return dict(
                id = self.id,
                total_volume = self.total_volume,
                num_lives = self.num_lives,
                total_viewer = self.total_viewer,
                avg_viewer = self.avg_viewer,
                max_viewer = self.max_viewer,
                total_goods_count = self.total_goods_count,
                live_sales_money = self.live_sales_money,
                avg_live_sales_money = self.avg_live_sales_money,
                goods_tag = self.tag.split(',') if self.tag else [])
