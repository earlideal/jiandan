# -*- coding: utf-8 -*-

import datetime
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
    __tablename__ = "staffs"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        super(Staff, self).__init__()
        self.name = name


class Project(Model):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    grant_number = Column(String, unique=False)
    name = Column(String)
    grant_type = Column(String)
    leader_id = Column(Integer, ForeignKey(Staff.id))
    leader = relationship(Staff)


class PurchaseCategory(Model):
    __tablename__ = "purchase_categories"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class PurchaseMethod(Model):
    __tablename__ = "purcase_methods"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class PropertyType(Model):
    __tablename__ = 'property_types'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Requisition(Model):
    __tablename__ = "requisitions"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    date = Column(Date, default=func.now())
    applicant_id = Column(Integer, ForeignKey(Staff.id))
    applicant = relationship(Staff)
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
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    contact = Column(String)
    telephone = Column(String)
    address = Column(String)


class Contract(Model):
    __tablename__ = "contracts"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    number = Column(String)
    amount = Column(Float, default=0)
    sign_date = Column(Date, default=func.now())
    company_id = Column(Integer, ForeignKey(Company.id))
    company = relationship(Company)


class Transaction(Model):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    swift_code = Column(String, default=datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
    requisition_id = Column(Integer, ForeignKey(Requisition.id))
    requisition = relationship(Requisition)
    contract_id = Column(Integer, ForeignKey(Contract.id))
    contract = relationship(Contract)
    created_time = Column(DateTime, default=func.now())
    modified_time = Column(DateTime, default=func.now())


class Inventory(Model):
    __tablename__ = "inventories"
    id = Column(Integer, primary_key=True)
    swift_code = Column(String, ForeignKey(Transaction.swift_code), nullable=False)
    name = Column(String)
    model = Column(String)
    manufacture = Column(String)
    property_type_id = Column(String, ForeignKey(PropertyType.id))
    property_type = relationship(PropertyType)
    unit = Column(String)
    quantity = Column(Float)
    quotation_price = Column(Float)
    quotation_currency = Column(String)
    requisition_price = Column(Float)
    requisition_sum = Column(Float)
    acceptance_price = Column(Float)
    acceptance_sum = Column(Float)
    description = Column(String)

    def __init__(self, swift_code, name, model, manufacture='', property_type_id=2, unit=u'只', quantity=1,
                 quotation_price=0, quotation_currency='CNY', requisition_price=0, acceptance_price=0, description=''):
        self.swift_code = swift_code
        self.name = name
        self.model = model
        self.manufacture = manufacture
        self.property_type_id = property_type_id
        self.unit = unit
        self.quantity = quantity
        self.quotation_price = quotation_price
        self.quotation_currency = quotation_currency

        if requisition_price == 0:
            self.requisition_price = quotation_price
        else:
            self.requisition_price = requisition_price
        if acceptance_price == 0:
            self.acceptance_price = quotation_price
        else:
            self.acceptance_price = acceptance_price

        self.description = description
        self.requisition_sum = quantity * self.requisition_price
        self.acceptance_sum = quantity * self.acceptance_price


Model.metadata.create_all(engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


# 模拟数据
def preinstall_db():
    names = [u'虚拟员工', u'苏付海', u'刘晓迪', u'杨雪', u'姜树清', u'丁俊峰', u'王媛', u'蒋华超', u'Alex', u'Eugene']
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

    methods_list = [u'公开招标', u'邀请招标', u'竞争性磋商', u'竞争性谈判', u'询价', u'单一来源']
    methods = []
    for m in methods_list:
        methods.append(PurchaseMethod(name=m))

    req = Requisition(title=u'拟采购的实验设备', applicant=staffs[0], project=p2, purchase_category=categories[0],
                      is_budget=True, budget_amount=100000, purchase_method=methods[0],
                      request_reason=u'该项目是中科院修购专项批准购买的专项设备。')

    session.add_all(staffs)
    session.add_all(categories)
    session.add_all(methods)
    session.add_all([p1, p2, p3, p4])
    session.add(req)

    ####################################################################################################################

    # 添加公司信息及合同信息
    changhe = Company(name=u'安徽长和进出口有限公司', contact=u'江云云', telephone=u'0551-64260008',
                      address=u'合肥市高新区香樟大道211号创展大厦C座2003室')

    kehua = Company(name=u'安徽省科华贸易有限责任公司', contact=u'杨国华', telephone=u'0551-65392835',
                    address=u'安徽省合肥市长江西路677号高新开发区昌河科创大厦702室')

    contract = Contract(name=u'代理进口协议示例一', number='AHCC20160001', amount=123456.78, company=changhe)

    session.add(changhe)
    session.add(kehua)
    session.add(contract)

    ####################################################################################################################

    # 添加事务信息
    transaction = Transaction(requisition=req, contract=contract)
    session.add(transaction)
    session.commit()

    ####################################################################################################################

    # 添加资产类型
    property_types = [u'固定资产', u'低值易耗品', u'材料消耗品']
    for i in xrange(len(property_types)):
        p = PropertyType(id=i, name=property_types[i])
        session.add(p)
    session.commit()

    ####################################################################################################################

    # 添加采购清单列表
    for i in xrange(0, 15):
        inventory = Inventory(swift_code=transaction.swift_code, name=u'针式打印机' + str(i), model='LQ-80KF', quantity=i,
                              quotation_price=123)
        session.add(inventory)

    session.commit()


if __name__ == '__main__':
    preinstall_db()
