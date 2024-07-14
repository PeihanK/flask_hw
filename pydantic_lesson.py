# models

# lesson1
#------------------------------------------------------
# Создать класс, который принимает данные пользователя в
# формате JSON и валидирует их на уровне типов данных.
# Данные включают:
# ● имя пользователя
# ● возраст
# ● email
# ● адрес (город, улица, номера дома)

# from pydantic import BaseModel, EmailStr, ValidationError
#
#
# class Address(BaseModel):
#     city: str
#     street: str
#     house_number: int
#
#
# class User(BaseModel):
#     name: str
#     age: int
#     email: EmailStr
#     address: Address
#
#
# json_string = """{
#  "name": "John Doe",
#  "age": 22,
#  "email": "john.doe@example.com",
#  "address": {
#  "city": "New York",
#  "street": "5th Avenue",
#  "house_number": 123
#  }
# }"""
#
# try:
#     # Создание экземпляра User из JSON строки
#     user = User.parse_raw(json_string)
#     print(user)
# except ValidationError as e:
#     print("Validation error:", e)
#
# # Сериализация объекта User обратно в JSON
# print(user.json())

#----------------------------------------------

# примеры наследования

# Реализовать систему пользователей:
# базовые пользователи имеют базовые атрибуты и возможности
# администраторы наследуют все атрибуты
# пользователей и имеют дополнительные привилегии

# from pydantic import BaseModel, EmailStr
#
#
# class User(BaseModel):
#     username: str
#     email: EmailStr
#
#     def __str__(self):
#         return f"User {self.username},Email: {self.email}"
#
#
# class AdminUser(User):
#     access_level: int = 10
#
#     # Предоставляем более высокий уровень доступа по умолчанию
#     def __str__(self):
#         return f"Admin {self.username}, Email: {self.email}, Access Level: {self.access_level}"
#
#     def promote_user(self, user: User):
#         print(f"Promoting {user.username} to higher privileges")
#         return AdminUser(username=user.username, email=user.email, access_level=self.access_level + 1)
#
#
# # Создание объекта пользователя
# user = User(username='john_doe', email='john.doe@example.com')
# print(user)
# # Создание объекта администратора и продвижение пользователя
# admin = AdminUser(username='admin_user', email='admin@example.com')
# print(admin)
# promoted_user = admin.promote_user(user)
# print(promoted_user)
#---------------------------------------------------------------------------------

# lesson2
#
# from pydantic import BaseModel, Field, EmailStr, field_validator, ValidationError
#
#
# class User(BaseModel):
#     name: str
#     age: int
#     email: EmailStr
#
#     @field_validator('email')
#     def check_email_domain(cls, value):
#         allowed_domains = ['example.com', 'test.com']
#         email_domain = value.split('@')[-1]
#         if email_domain not in allowed_domains:
#             raise ValueError(f"Email must be from one of the following domains: {', '.join(allowed_domains)}")
#         return value
#
#
# # Пример создания пользователя
# try:
#     # Этот email проходит валидацию
#     user_valid = User(name="Alice", age=30, email="alice@example.com")
#     print(f"Valid user: {user_valid}")
#
#     # Этот email вызовет ошибку валидации
#     user_invalid = User(name="Bob", age=25, email="bob@gmail.com")
# except ValidationError as e:
#     print(e)
#
# #валидация эмейла по буквам и .com
#
# from pydantic import BaseModel, field_validator, EmailStr
#
# # Базовая модель пользователя с валидацией email
# class User(BaseModel):
#     name: str
#     email: EmailStr
#
#     # Валидатор для проверки имени
#     @field_validator('name')
#     def validate_name(cls, value):
#         if not value.isalpha():
#             raise ValueError('Name must contain only letters')
#         return value
#
#     # Валидатор для проверки емейла
#     @field_validator('email')
#     def check_email(cls, value):
#         allowed_domains = ['example.com', 'test.com']
#         email_domain = value.split('.')[-1]
#         if email_domain != 'com':
#             raise ValueError(f"Email must ends with .com")
#         return value
# try:
#     # Валидный пример
#     user = User(name='John', email='john@example.com')
#     print(user)
#     # Невалидный пример
#     user2 = User(name='John>', email='john@example.ge')
#     print(user2)
#
# except ValueError as e:
#     print(e)

#
# from datetime import datetime
# from pydantic import BaseModel
#
#
# class User(BaseModel):
#     signup_ts: datetime
#
#     class Config:
#         json_encoders = {
#             datetime: lambda v: v.strftime('%d-%m-%Y %H:%M')
#         }
#
#
# user = User(signup_ts=datetime.now())
# print(user)
# print(user.json())  # Выводит время регистрации пользователя в заданном формате

#
# from datetime import datetime
# from pydantic import BaseModel, EmailStr
#
#
# class User(BaseModel):
#     first_name: str
#     last_name: str
#     email: EmailStr
#     created_at: datetime
#
#     class Config:
#         str_min_length = 2
#         str_strip_whitespace = True
#         json_encoders = {
#             datetime: lambda v: v.strftime('%y-%m-%d %H:%M')
#         }
#
#
# user = User(first_name='John', last_name='Doe', email='doe@example.com', created_at=datetime.now())
# print(user)
# print(user.json())  # Выводит пользователя в формате json
