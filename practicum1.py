# Pydantic

# Создайте модель Event, которая включает поля:
# ● title (строка),
# ● date (дата и время события),
# ● location (строка).
# Добавьте валидацию, чтобы дата события не была в прошлом
import datetime

# from pydantic import BaseModel, validator, field_validator
# from datetime import datetime, timedelta
#
#
# class Event(BaseModel):
#     title: str
#     date: datetime
#     location: str
#
#     @field_validator('date')
#     def format_date(cls, v):
#         if v < datetime.now():
#             raise ValueError('Event date must be in the future')
#         return v
#
#
# try:
#     event_1 = Event(title='Holiday', date=datetime.now() + timedelta(days=120), location='San Francisco')
#     print(event_1)
# except ValueError as e:
#     print(e)
# -----------------------------------------------------------------------------------------------------------
# Определите модель UserProfile с полями:
# ● username (строка),
# ● password (строка),
# ● email (строка с валидацией email).
# Используйте Field для добавления описаний и настройки валидации пароля (должен быть не менее 8
# символов).

# from pydantic import BaseModel, EmailStr, ValidationError, Field, field_validator
#
#
# class UserProfile(BaseModel):
#     username: str
#     password: str = Field(min_length=8, description='Password must be min. 8 characters')
#     email: EmailStr
#
#
# try:
#     John = UserProfile(username="john_doe", password="securePassword123", email="john.doe@example.com")
#     print(John)
# except Exception as e:
#     print(e)
# ----------------------------------------------------------------------------------------------------------
# Разработайте модель Transaction для управления финансовыми операциями.
# Модель должна содержать:
# ● amount (десятичное число),
# ● transaction_type (строка, принимает значения "debit" или "credit"),
# ● currency (строка).

# from pydantic import BaseModel, EmailStr, ValidationError, Field, field_validator, condecimal
# from decimal import Decimal
#
#
# class Transaction(BaseModel):
#     amount: condecimal(gt=Decimal('1'))
#     transaction_type: str
#     currency: str
#
#     @field_validator('amount')
#     def amount(cls, v):
#         if v not in ['debit', 'credit']:
#             raise ValueError('Wrong value')
#         return v
#
#
# try:
#     first_transaction = Transaction(amount=150.57, transaction_type='debit', currency='euro')
#     print(first_transaction)
# except Exception as e:
#     print(e)
#
# print(first_transaction.amount)
# --------------------------------------------------------------------------------------------------------------
# Создайте модель Appointment для записи на прием, которая включает patient_name (строка),
# appointment_date (дата и время), и проверку, что запись не может быть установлена ранее, чем
# через 24 часа от текущего момента.
#
# from pydantic import BaseModel, EmailStr, ValidationError, Field, field_validator, condecimal
# from decimal import Decimal
#
# class Appointment(BaseModel):
#     patient_name: str
#     appointment_date: datetime
#
#     @field_validator('appointment_date')
#     def date(cls, v):
#         if v < datetime.now()+ datetime.timedelta(hours=24):
#             raise ValueError('Not possible to take time less then 24 hours')
#         return v
#
# try:
#     appointment_1 = Appointment(patient_name='John', appointment_date=datetime.now() + datetime.timedelta(hours=25))
#     print(appointment_1)
# except ValidationError as e:
#     print(e)
# --------------------------------------------------------------------------------------------------------------------

# SQLAlchemy
# -----------
# 1 Создайте экземпляр движка для подключения к MySQL базе данных
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
#
#
# engine = create_engine('mysql+pymysql://ich1:password@ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com/dbpython')


# 2 Напишите код для создания движка SQLAlchemy с подключением к базе данных SQLite,
# который будет располагаться в памяти, и настройте вывод логов всех операций с базой
# данных на экран.

# from sqlalchemy import create_engine
# import logging
# logging.basicConfig(level=logging.INFO)
#
# engine = create_engine('sqlite:///:memory:', echo=True)
#
# 3 Создайте модель User с полями:
# ● id (целочисленный тип, первичный ключ),
# ● name (строковый тип, длина до 50 символов),
# ● age (целочисленный тип).
#
# from sqlalchemy.orm import declarative_base
# from sqlalchemy import Column, Integer, String
#
# Base = declarative_base()
#
#
# class User(Base):
#     __tablename__ = 'users'
#     id= Column(Integer, primary_key=True)
#     name = Column(String(50))
#     age = Column(Integer)

# 4 Определите две модели, User и Post, где пользователь может иметь много постов (один
# ко многим). Используйте декларативный базовый класс.
# from sqlalchemy.orm import declarative_base, relationship
# from sqlalchemy import Column, Integer, String, ForeignKey
#
# from SQLAlchemy import engine
#
# Base = declarative_base()
#
#
# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50))
#     age = Column(Integer)
#
#
# class Post(Base):
#     __tablename__ = 'posts'
#     id = Column(Integer, primary_key=True)
#     title = Column(String(255))
#     user_id = Column(Integer, ForeignKey('users.id'))
#     user = relationship('User', back_populates='posts')
#
#
# Base.metadata.create_all(engine)

#5 Определите две модели: User и Address, где User может иметь множество Address.
# Используйте декларативный базовый класс.

# 7

