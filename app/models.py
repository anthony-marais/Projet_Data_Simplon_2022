from dataclasses import dataclass
from pandas.core.frame import DataFrame
from sqlalchemy.sql import func
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Column, Integer, ForeignKey, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from app.db import db


@dataclass
class User(db, SerializerMixin):
    """Table user de la BDD, il est possible de faire des requete sql
    avec user.query (voir la doc de flask-sqlalchemy)
    """

    __tablename__ = "User"
    ID = Column("ID", Integer, primary_key=True)
    Email_Address = Column("Email Address", VARCHAR(50))
    FirstName = Column("FirstName", VARCHAR(50))
    LastName = Column("LastName", VARCHAR(50))
    ID_Job_Title = Column("ID_Job_Title", Integer, ForeignKey("Job_Title.ID_Job_Title"))
    ID_State = Column("ID_State", Integer, ForeignKey("State.ID_State"))
    ID_City = Column("ID_City", Integer, ForeignKey("City.ID_City"))
    ID_Street = Column("ID_Street", Integer, ForeignKey("Street.ID_Street"))
    ID_Street_Number = Column(
        "ID_Street_Number", Integer, ForeignKey("Street_Number.ID_Street_Number")
    )

    def insert_user_from_pd(connection, User):
        User.to_sql("User", if_exists="append", con=connection, index=False)


@dataclass
class Job_Title(db, SerializerMixin):
    """Table job_title de la BDD, il est possible de faire des requete sql"""

    __tablename__ = "Job_Title"
    ID_Job_Title = Column("ID_Job_Title", Integer, primary_key=True)
    Job_Title = Column("Job Title", VARCHAR(50))

    def insert_job_title_from_pd(connection, Job_Title):
        Job_Title.to_sql("Job_Title", if_exists="append", con=connection, index=False)


@dataclass
class State(db, SerializerMixin):
    """Table state de la BDD, il est possible de faire des requete sql"""

    __tablename__ = "State"
    ID_State = Column("ID_State", Integer, primary_key=True)
    State = Column("State", VARCHAR(50))

    def insert_state_from_pd(connection, State):
        State.to_sql("State", if_exists="append", con=connection, index=False)


@dataclass
class City(db, SerializerMixin):
    """Table books de la BDD, il est possible de faire des requete sql"""

    __tablename__ = "City"
    ID_City = Column("ID_City", Integer, primary_key=True)
    City = Column("City", VARCHAR(50))

    def insert_city_from_pd(connection, City):
        City.to_sql("City", if_exists="append", con=connection, index=False)


@dataclass
class Street(db, SerializerMixin):
    """Table books de la BDD, il est possible de faire des requete sql"""

    __tablename__ = "Street"
    ID_Street = Column("ID_Street", Integer, primary_key=True)
    Street = Column("Street", VARCHAR(50))

    def insert_street_from_pd(connection, Street):
        Street.to_sql("Street", if_exists="append", con=connection, index=False)


@dataclass
class Street_Number(db, SerializerMixin):
    """Table books de la BDD, il est possible de faire des requete sql"""

    __tablename__ = "Street_Number"
    ID_Street_Number = Column("ID_Street_Number", Integer, primary_key=True)
    Number = Column("Number", VARCHAR(50))

    def insert_street_number_from_pd(connection, Street_Number):
        Street_Number.to_sql(
            "Street_Number", if_exists="append", con=connection, index=False
        )
