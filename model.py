# -*- coding: utf-8 -*-

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///model.sqlite', echo=False)
Model = declarative_base()


class Staff(Model):
    __tablename__ = "staff"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Project(Model):
    __tablename__ = "project"
    id = Column(Integer, primary_key=True)
    grant_number = Column(String, unique=False)
    name = Column(String)
    grant_type = Column(String)
    leader_id = Column(Integer, ForeignKey(Staff.id))
    leader = relationship(Staff)


class Requisition(Model):
    __tablename__ = "requisition"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    date = Column(Date, default=func.now())
    applicant_id = Column(Integer, ForeignKey(Staff.id))
    applicant = relationship(Staff)
    purchase_type = Column(String)
    project_id = Column(Integer, ForeignKey(Project.id))
    project = relationship(Project)
    purchase_method = Column(String)
    purchase_reason = Column(String)
    tech_specification = Column(String)


class Contract(Model):
    __tablename__ = "contract"
    id = Column(Integer, primary_key=True)


Model.metadata.create_all(engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


def generate_test_db():
    su_fu_hai = Staff(name=u'苏付海')
    liu_xiao_di = Staff(name=u'刘晓迪')
    yang_xue = Staff(name=u'杨雪')
    jiang_shu_qing = Staff(name=u'姜树清')
    ding_jun_feng = Staff(name=u'丁俊峰')
    wang_yuan = Staff(name=u'王媛')
    jiang_hua_chao = Staff(name=u'蒋华超')
    names = [u'苏付海', u'刘晓迪', u'杨雪', u'姜树清', u'丁俊峰', u'王媛', u'蒋华超']

    p1 = Project(grant_number='Y64NLXG362', name=u'极端高压超快光学实验平台', grant_type=u'中科院修购专项', leader=su_fu_hai)
    p2 = Project(grant_number='Y64NLYZ251', name=u'高温高压下热导率原位测量', grant_type=u'中科院科研装备研制项目', leader=su_fu_hai)
    p3 = Project(grant_number='Y64NLXG363', name=u'极端条件下新奇化学态的探索', grant_type=u'中科院修购专项', leader=su_fu_hai)
    req = Requisition(title=u'实验室办公用品采购申请测试用例一', applicant=jiang, project=p1, purchase_method=u'公开招标',
                      purchase_reason=u'该项目是中科院修购专项批准购买的专项设备。')
    session.add_all([su_fu_hai, jiang, temp])
    session.add(p1)
    session.add(req)
    session.commit()


def test_db():
    staffs = session.query(Staff).all()
    for s in staffs:
        print s.id, s.name
    reqisitions = session.query(Requisition).filter_by(title=u'实验室办公用品采购申请测试用例一').all()
    if len(reqisitions) > 0:
        req = reqisitions[0]
        print req.applicant.id, req.applicant.name, req.project.name, req.project.leader.name, req.project.grant_number, req.project.id
        projects = session.query(Project).all()
        for p in projects:
            print p.id, p.name, p.grant_number
    session.commit()


s = session.query(Staff).all()
if len(s) == 0:
    generate_test_db()
# test_db()
