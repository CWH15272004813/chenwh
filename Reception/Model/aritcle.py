import MysqlModel
from MysqlModel import db
from flask import g,jsonify

model = MysqlModel
class ArticleModel(object):
    # 获取所有的所有的文章
    def GetAll(self):
        article = model.Article.query.all()
        # print(article[0])
        # print(type(article[0]))
        # print(type(article[0]))
        # print(article)
        # art = article[0]
        # print(type(art))
        # print(art.time)
        # for i in article:
        #     for item in i:
        #         print(item.id)
        Data = []
        for item in article:
            data = {
                "id": item.id,
                "title": item.title,
                "content": item.content,
                "author": item.author,
                "state": item.state,
                "time": item.time.strftime('%Y-%m-%d %H:%M:%S'),
                "label":self.Getalllable(item.id)
            }
            Data.append(data)
        return Data

    def Getalllable(self,id):
         data = model.Label.query.filter_by(article_on=id).all()
         da = []
         for item in data:
             da.append(item.label)
         label = "，".join(da)
         return label
    def Getcomment(self,id):
        data = model.Comment.query.filter_by(article_on=id).all()
        g.html = ''
        for item in data:
            html = '<div class="comment">'
            html += '<img src="http://placehold.it/100x100" alt="img" width="100" height="100">'\
                    '<div class="text">'\
                    '<div class="name">' + item.nickname + ' <a class="reply" abc="'+str(item.id)+'" href="#">回 复</a></div>'\
                    '<div class="date">' + item.time.strftime('%Y-%m-%d %H:%M:%S') + '</div> '+item.content+''\
                    '</div>' \
                    '<div class="clear"></div>'
            for i in self.Getreply(item.id):
                html += '<div class="comment sub">'\
                        ' <img src="http://placehold.it/100x100" alt="img" width="100" height="100">'\
                        ' <div class="text">'\
                        ' <div class="name">'+i.nickname+' <a class="reply" abc="'+str(i.id)+'" href="#">回 复</a></div>'\
                        '<div class="date">'+i.time.strftime('%Y-%m-%d %H:%M:%S')+'</div>'+i.content+''\
                        '</div>'\
                        ' <div class="clear"></div>'\
                        ' </div>'\
                        ' <div class="clear"></div>'\

            html += '</div>'
            g.html += html
        # print(g.html)
        return g.html

    def Getreply(self,id):
        data = model.Reply.query.filter_by(comment_on =id).all()
        return data

    def Addcomment(self, article_on, nickname, mailbox, content):
        sql = model.Comment(article_on=article_on,nickname=nickname,mailbox=mailbox,content=content,pic="abc.jpg")
        db.session.add(sql)
        db.session.commit()
        # print(sql)
        data = {"id": sql.id, "nickname": sql.nickname, "time": sql.time.strftime('%Y-%m-%d %H:%M:%S'), "content": sql.content, "pic": sql.pic}
        if sql.id == "":
            return jsonify({"code": 500,"content": "error"})
        return jsonify({"code": 200,"content": data})











