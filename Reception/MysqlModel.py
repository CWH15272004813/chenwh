from flask import Flask
import config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 连接mysql数据库配置
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URL

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class Article(db.Model):
    # 表名
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), unique=False, nullable=False)
    content = db.Column(db.String(1000), unique=False,nullable=False)
    # comment_on = db.Column(db.Integer, nullable=Flask)
    author = db.Column(db.String(50),unique=False, nullable=False)
    # label_on = db.Column(db.Integer, nullable=Flask)
    state = db.Column(db.String(20),unique=False, default="显示")
    time = db.Column(db.TIMESTAMP, nullable=False, server_default=db.text('NOW()'))
    pictures = db.relationship('Picture', backref='Article')
    labels = db.relationship('Label', backref='Article',)
    comments = db.relationship('Comment', backref='Article', )
    # 对应repr(object)这个函数，返回一个可以用来表示对象的可打印字符串
    # '{"id":%r,"title":%r,"content":%r,"author":%r,"state":%r,"time":%r}' %(self.id, self.title, self.content, self.author, self.state, self.time.strftime('%Y-%m-%d %H:%M:%S'))
    def __repr__(self):
        return '"id"=%r,title=%r,content=%r,author=%r,state=%r,time=%r' %(self.id, self.title, self.content, self.author, self.state, self.time.strftime('%Y-%m-%d %H:%M:%S'))


class Picture(db.Model):
    __tablename__ = 'pictures'
    id = db.Column(db.Integer, primary_key=True)
    article_on = db.Column(db.Integer, db.ForeignKey('articles.id'))
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(500),unique=False, nullable=Flask)
    picture = db.Column(db.String(1000),unique=False, nullable=Flask)
    state = db.Column(db.String(20), unique=False, default="显示")
    time = db.Column(db.TIMESTAMP,nullable=False,server_default=db.text('NOW()'))

    def __repr__(self):
        return '<Admin %r>' % self.title

class Label(db.Model):
    __tablename__ = 'labels'
    id = db.Column(db.Integer, primary_key=True)
    article_on = db.Column(db.Integer,db.ForeignKey('articles.id'))
    label = db.Column(db.String(20),unique=False)
    state = db.Column(db.String(20),unique=False, default="显示")
    time = db.Column(db.TIMESTAMP, nullable=False, server_default=db.text('NOW()'))

    def __repr__(self):
        return 'label=%r' % self.label

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    article_on = db.Column(db.Integer,db.ForeignKey('articles.id'))
    nickname = db.Column(db.String(100),unique=False)
    mailbox = db.Column(db.String(100),unique=False)
    content = db.Column(db.String(1000),unique=False)
    pic = db.Column(db.String(1000),unique=False)
    state = db.Column(db.String(20),unique=False, default="显示")
    time = db.Column(db.TIMESTAMP, nullable=False, server_default=db.text('NOW()'))
    replys = db.relationship("Reply", backref='Comment')

    # def __repr__(self):
    #     return 'id=%r,nickname=%r,mailbox=%r,content=%r,pic=%r,time=%r' %(self.id, self.nickname, self.mailbox, self.content, self.pic, self.time)

class Reply(db.Model):
    __tablename__ = 'replys'
    id = db.Column(db.Integer, primary_key=True)
    comment_on = db.Column(db.Integer, db.ForeignKey('comments.id'))
    nickname = db.Column(db.String(100),unique=False)
    mailbox = db.Column(db.String(100),unique=False)
    content = db.Column(db.String(1000),unique=False)
    pic = db.Column(db.String(1000),unique=False, default="")
    state = db.Column(db.String(20),unique=False, default="显示")
    time = db.Column(db.TIMESTAMP, nullable=False, server_default=db.text('NOW()'))









db.create_all()

