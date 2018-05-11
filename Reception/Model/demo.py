# from MysqlModel import db, Article, Comment, Label, Reply ,Picture
#
# class ArticleModel(object):
#     def GetAll(self):
#         pass
        # sql = Article(title="我是标题",
        #               content="常见情况下对于只有一个 Flask 应用，所有您需要做的事情就是创建 Flask 应用，选择加载配置接着创建 SQLAlchemy 对象时候把 Flask 应用传递给它作为参数。一旦创建，这个对象就包含 sqlalchemy 和 sqlalchemy.orm 中的所有函数和助手。此外它还提供一个名为 Model 的类，用于作为声明模型时的 delarative 基类"
        #                       "为了创建初始数据库，只需要从交互式 Python shell 中导入 db 对象并且调用 SQLAlchemy.create_all() 方法来创建表和数据库"
        #                       "从最普通的意义上讲，它Session建立了与数据库的所有对话，并代表了在其生命周期中加载或关联的所有对象的“保留区”。它提供了获取Query对象的入口点，该对象使用Session对象的当前数据库连接向数据库发送查询，将结果行填充到对象中，然后将其存储在 Session名为Identity Map的结构中 - 一个数据结构，该结构保存每个对象，其中“唯一”意味着“只有一个具有特定主键的对象”。",
        #               author="小陈")
        # db.session.add(sql)
        # db.session.commit()
        #
        # sql1 = Comment(article_on=1, nickname="小民", mailbox="2507684583@163.com",content="这篇文章还行", pic="img2.png")
        # sql2 = Comment(article_on=1, nickname="小章", mailbox="603273653@qq.com", content="这篇文章写的还可以", pic="img3.png")
        # sql3 = Comment(article_on=1, nickname="小程", mailbox="152720104813@163.com", content="这篇文章还可以", pic="img2.png")
        # sql4 = Comment(article_on=2, nickname="小明", mailbox="60023456@qq.com", content="这篇文章非常不错", pic="img3.png")
        # sql5 = Comment(article_on=2, nickname="小花", mailbox="152720042813@163.com", content="这篇文章不错啦", pic="img6.png")
        # db.session.add(sql1)
        # db.session.add(sql2)
        # db.session.add(sql3)
        # db.session.add(sql4)
        # db.session.add(sql5)
        # db.session.commit()
        # sql2 = Label(article_on="1",label="redis")
        # sql3 = Label(article_on="2",label="css3+html5")
        # db.session.add(sql2)
        # db.session.add(sql3)
        # db.session.commit()






