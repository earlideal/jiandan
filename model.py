# -*- coding: utf-8 -*-

import os

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

if __name__ == '__main__':
    if os.path.exists('model.sqlite'):
        os.remove('model.sqlite')

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


class PurchaseCategory(Model):
    __tablename__ = "purchase_category"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class PurchaseMethod(Model):
    __tablename__ = "purchase_method"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Requisition(Model):
    __tablename__ = "requisition"
    id = Column(Integer, primary_key=True)
    date = Column(Date, default=func.now())
    applicant_id = Column(Integer, ForeignKey(Staff.id))
    applicant = relationship(Staff)
    title = Column(String)
    purchase_category_id = Column(Integer, ForeignKey(PurchaseCategory.id))
    purchase_category = relationship(PurchaseCategory)
    purchase_method_id = Column(Integer, ForeignKey(PurchaseMethod.id))
    purchase_method = relationship(PurchaseMethod)
    project_id = Column(Integer, ForeignKey(Project.id))
    project = relationship(Project)
    is_budget = Column(Boolean)
    budget_amount = Column(Float)
    request_reason = Column(String)
    technical_spec = Column(String)


class Company(Model):
    __tablename__ = "company"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    contact = Column(String)
    telephone = Column(String)
    address = Column(String)


class Contract(Model):
    __tablename__ = "contract"
    id = Column(Integer, primary_key=True)
    contract_name = Column(String)
    contract_number = Column(String)
    sign_date = Column(Date, default=func.now())
    company_id = Column(Integer, ForeignKey(Company.id))
    company = relationship(Company)


Model.metadata.create_all(engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


def preinstall_db():
    names = [u'苏付海', u'刘晓迪', u'杨雪', u'姜树清', u'丁俊峰', u'王媛', u'蒋华超', u'Alex', u'Eugene']
    staffs = []
    for name in names:
        staffs.append(Staff(name=name))

    p1 = Project(grant_number='Y64NLXG362', name=u'极端高压超快光学实验平台', grant_type=u'中科院修购专项', leader=staffs[0])
    p2 = Project(grant_number='Y64NLYZ251', name=u'高温高压下热导率原位测量系统研制', grant_type=u'中科院科研装备研制项目', leader=staffs[0])
    p3 = Project(grant_number='Y54NL2150H', name=u'极端条件下新奇化学态的探索', grant_type=u'面上项目', leader=staffs[7])
    p4 = Project(grant_number='Y54NL11507', name=u'高压下金刚石NV色心能级变化', grant_type=u'青年基金', leader=staffs[1])

    categories_list = [u'仪器设备', u'研制加工', u'办公设备', u'仪器部件']
    categories = []
    for c in categories_list:
        categories.append(PurchaseCategory(name=c))

    method_list = [u'公开招标', u'邀请招标', u'竞争性磋商', u'竞争性谈判', u'询价', u'单一来源']
    methods = []
    for m in method_list:
        methods.append(PurchaseMethod(name=m))

    req = Requisition(title=u'拟采购的实验设备', applicant=staffs[5], project=p2, purchase_category=categories[0],
                      is_budget=True, budget_amount=100000, purchase_method=methods[0],
                      request_reason=u'该项目是中科院修购专项批准购买的专项设备。')

    session.add_all(staffs)
    session.add_all(categories)
    session.add_all(methods)
    session.add_all([p1, p2, p3, p4])
    session.add(req)

    ####################################################################################################################

    # 添加公司信息
    company = Company(name=u'安徽长和进出口有限公司', contact=u'江云云', telephone=u'0551-64260008',
                      address=u'合肥市高新区香樟大道211号创展大厦C座2003室')
    contract = Contract(contract_name=u'低温恒温器代理进口协议', contract_number='AHCC20160001', company=company)
    session.add(company)
    session.add(contract)
    session.commit()


if __name__ == '__main__':
    preinstall_db()
