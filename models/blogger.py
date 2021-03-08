from db import db

class BloggerModel(db.Model):

    __tablename__ = "base_user_info"

    id = db.Column(db.String(50), primary_key=True)
    create_time = db.Column(db.DateTime)
    name = db.Column(db.String(50))
    douyin_id = db.Column(db.String(50))
    sex = db.Column(db.String(50))
    region = db.Column(db.String(50))
    tag = db.Column(db.String(50))
    introduction = db.Column(db.String(2000))
    fans = db.Column(db.Integer)
    videos = db.Column(db.Integer)
    index_number = db.Column(db.Float)
    cert = db.Column(db.String(50))
    likes = db.Column(db.Integer)
    # livegoods = db.relationship('LiveGoodModel')
    # bloggerstats = db.relationship('BloggerStatsModel')


    def __repr__(self):
        return '<Blogger %r>' % self.name

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(name = name).first()

    @classmethod
    def get_by_id(cls, id_):
        return cls.query.filter_by(id = id_).first()


    @classmethod
    def getn(cls, n):
        return cls.query.limit(n)

    @classmethod
    def get_tags(cls):
        '''Return a json'''
        result = [a.tag for a in cls.query.with_entities(cls.tag).distinct()]
        print(result)
        return result


    def json(self):
        return {
            'id':self.id,
            'name':self.name,
            'douyin_id':self.douyin_id,
            'sex':self.sex,
            'region':self.region,
            'tag':self.tag,
            'introduction':self.introduction,
            'fans':self.fans,
            'videos':self.videos,
            'index_number':self.index_number,
            'cert':self.cert,
            'likes':self.likes
        }

    def json_short(self):
        return {
            'id':self.id,
            'name':self.name,
            'fans':self.fans,
            'videos':self.videos,
        }
