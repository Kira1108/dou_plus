from db import db

class LiveModel(db.Model):

    __tablename__ = "base_live"
    id = db.Column(db.String(50))
    # id = db.Column(db.String(50), db.ForeignKey("base_user_info.id"))
    uid = db.Column(db.String(50), primary_key = True)
    create_time = db.Column(db.DateTime)
    begin_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    avg_review_time = db.Column(db.String(50))
    total_viewer = db.Column(db.Integer)
    max_viewer = db.Column(db.Integer)
    goods_count = db.Column(db.Integer)
    attention = db.Column(db.Integer)
    yinlang = db.Column(db.Integer)
    sales_volume = db.Column(db.Integer)
    profits = db.Column(db.Integer)
    fans = db.Column(db.Integer)
    goods = db.Column(db.Integer)
    is_live_user = db.Column(db.Integer)
    # db.relationship('BloggerModel')
    # db.relationship('LiveGoodModel')


    @classmethod
    def get_by_uid(cls, uid):
        '''Return a Live idenfied by uid'''
        return cls.query.filter_by(uid = uid).first()

    @classmethod
    def get_by_blogger_id(cls, blogger_id):
        '''Return a list of Lives'''
        return cls.query.filter_by(id == blogger_id)


    def json(self):
        return {
            'uid':self.uid,
            'begine_time':self.begin_time,
            'end_time':self.end_time,
            'avg_review_time':self.avg_review_time,
            'total_viewer':self.total_viewer,
            'max_viewer':self.max_viewer,
            'goods_count':self.goods_count,
            'attention':self.attention,
            'yinlang':self.yinlang,
            'sales_volume':self.sales_volume,
            'profits':self.profits,
            'fans':self.fans,
            'goods':self.goods,
        }
