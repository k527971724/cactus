from . import db


# 【文章】
class Article(db.Model):
    __tablename__ = "articles"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40))
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)
    recommend01 = db.Column(db.Integer)
    recommend02 = db.Column(db.Integer)
    recommend03 = db.Column(db.Integer)
    recommend04 = db.Column(db.Integer)
    recommend05 = db.Column(db.Integer)
    recommend06 = db.Column(db.Integer)

