# -*- coding: utf-8 -*-

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///model.sqlite')
Model = declarative_base()


class User(Model):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class ResearchProject(Model):
    __tablename__ = "project"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    user_id = Column(Integer, ForeignKey(User.id))
    user = relationship(User)


class PurchaseRequisition(Model):
    __tablename__ = "requisition"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    date = Column(Date, default=func.now())
    applicant_id = Column(Integer, ForeignKey(User.id))
    applicant = relationship(User)
    purchase_type = Column(String)
    project_id = Column(Integer, ForeignKey(ResearchProject.id))
    project = relationship(ResearchProject)
    purchase_method = Column(String)
    purchase_reason = Column(String)
    qualification = Column(String)
    review_group = Column(String)

    def add(self):
        print "add"
        s = session()
        s.add(self)
        s.commit()


class Contract(Model):
    __tablename__ = "contract"
    id = Column(Integer, primary_key=True)


session = sessionmaker()
session.configure(bind=engine)
Model.metadata.create_all(engine)

# user1 = User(name=u'蒋华超')
# user2 = User(name=u'赵钱孙')
# s.add(user1)
# s.add(user2)
# project = ResearchProject(name=u"高压超快光学平台", user=user1)
# s.add(project)
# p = PurchaseRequisition(title=u"太赫兹光谱系统", purchase_type=u"公开招标", applicant=user1, project=project)
# s.add(p)
# s.commit()
# users = s.query(User).all()
# for u in users:
#     print u.name, u.id
# purchases = s.query(PurchaseRequisition).all()
# for p in purchases:
#     print p.title, p.date, p.applicant.name, p.applicant_id, p.project.name
