# -*- coding: utf-8 -*-

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///model.sqlite', echo=False)
Model = declarative_base()
Model.metadata.create_all(engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


class Person(Model):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class ResearchProject(Model):
    __tablename__ = "project"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    user_id = Column(Integer, ForeignKey(Person.id))
    user = relationship(Person)


class PurchaseRequisition(Model):
    __tablename__ = "requisition"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    date = Column(Date, default=func.now())
    applicant_id = Column(Integer, ForeignKey(Person.id))
    applicant = relationship(Person)
    purchase_type = Column(String)
    project_id = Column(Integer, ForeignKey(ResearchProject.id))
    project = relationship(ResearchProject)
    purchase_method = Column(String)
    purchase_reason = Column(String)
    qualification = Column(String)
    review_group = Column(String)


class Contract(Model):
    __tablename__ = "contract"
    id = Column(Integer, primary_key=True)

    # from contextlib import contextmanager
    #
    # @contextmanager
    # def session_scope():
    #     session = Session()
    #     try:
    #         yield session
    #         session.commit()
    #     except:
    #         session.rollback()
    #         raise
    #     finally:
    #         session.close()
    # with session_scope() as session:
    #     all = session.query(Person).all()
    #     return all
