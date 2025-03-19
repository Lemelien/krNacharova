from sqlalchemy import (Column, Integer, String, Date, ForeignKey, Float)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    manager_id = Column(Integer, ForeignKey('employees.id'))
    employees = relationship("Employee", back_populates="department")

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    position = Column(String(100))
    salary = Column(Float)
    hire_date = Column(Date)
    department_id = Column(Integer, ForeignKey('departments.id'))
    department = relationship("Department", back_populates="employees")

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String)
    status = Column(String(20))
    project_id = Column(Integer, ForeignKey('projects.id'))
    assignee_id = Column(Integer, ForeignKey('employees.id'))

class Connect():
    @staticmethod
    def create_connection():
        engine = create_engine("postgresql://postgres:1234@localhost:5432/company_managemen")
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
    from sqlalchemy import (Column, Integer, String, Date, ForeignKey, Float)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

# Таблица departments
class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    manager_id = Column(Integer, ForeignKey('employees.id'))

    # Однозначное указание связи
    employees = relationship("Employee", back_populates="department", 
                             foreign_keys='[Employee.department_id]')

# Таблица employees
class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    position = Column(String(100))
    salary = Column(Float)
    hire_date = Column(Date)
    department_id = Column(Integer, ForeignKey('departments.id'))

    # Связь с отделом
    department = relationship("Department", back_populates="employees", 
                              foreign_keys=[department_id])

# Таблица tasks
class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(255))
    status = Column(String(20))
    project_id = Column(Integer, ForeignKey('projects.id'))
    assignee_id = Column(Integer, ForeignKey('employees.id'))

# Подключение к базе
class Connect():
    @staticmethod
    def create_connection():
        engine = create_engine("postgresql://postgres:1234@localhost:5432/company_managemen")
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        return session

