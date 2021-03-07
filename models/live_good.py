from db import db

class LiveGoodModel(db.Model):

    __tablename__ = "base_live_goods"

    goods_id = db.Column(db.String(50), primary_key = True)
    id = db.Column(db.String(50), db.ForeignKey("base_user_info.id"))
    uid = db.Column(db.String(50))
    create_time = db.Column(db.DateTime)
    name = db.Column(db.String(100))
    link = db.Column(db.String(700))
    tag = db.Column(db.String(50))
    brand = db.Column(db.String(50))
    price = db.Column(db.Float)
    up_time = db.Column(db.String(50))
    down_time = db.Column(db.String(50))
    sales_count = db.Column(db.Integer)
    sales_price = db.Column(db.Float)

    db.relationship('BloggerModel')


    def __repr__(self):
        return '<Live_good %r>' % self.name

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(name = name).first()

    @classmethod
    def get_by_goodsid(cls, goods_id):
        return cls.query.filter_by(id = goods_id).first()


    @classmethod
    def get_tags(cls):
        '''Return a json'''
        result = [a.tag for a in cls.query.with_entities(cls.tag).distinct()]
        print(result)
        return result


    def json(self):
        return dict(goods_id = self.goods_id,
            id = self.id,
            uid = self.uid,
            name = self.name,
            link = self.link,
            tag = self.tag,
            brand = self.brand,
            price = self.price,
            up_time = self.up_time,
            down_time = self.down_time,
            sales_count = self.sales_count,
            sales_price = self.sales_price)
