from pydantic import BaseModel, EmailStr, ValidationError, Field, field_validator


class Address(BaseModel):
    city: str = Field(..., min_length=2)
    street: str = Field(..., min_length=3)
    house_number: int = Field(..., gt=0)


class User(BaseModel):
    name: str = Field(..., min_length=2, strip_whitespace=True)
    age: int = Field(..., ge=0, le=120)
    email: EmailStr
    is_employed: bool
    address: Address

    @field_validator('name')
    def check_name(cls, value):
        if not value.isalpha():
            raise ValueError(f"Name must contain only letters")
        return value

    @field_validator('is_employed')
    def check_employment_status(cls, value, values):
        age = values.data.get('age')
        if value and age is not None:
            if age < 18 and value:
                raise ValueError("Underage users cannot be employed")
            elif age > 67 and value:
                raise ValueError("Pensioners cannot be employed")
        return value


json_string_e1 = """{
 "name": "John Doe",
 "age": 22,
 "email": "john.doe@example.com",
 "is_employed": true,
 "address": {
 "city": "New York",
 "street": "5th Avenue",
 "house_number": 123
 }
}"""

json_string_e2 = """{
 "name": "John Doe",
 "age": 10,
 "email": "john.doe@example.com",
 "is_employed": true,
 "address": {
 "city": "New York",
 "street": "5th Avenue",
 "house_number": 123
 }
}"""

json_string_e3 = """{
 "name": "John",
 "age": 110,
 "email": "john.doe@example.com",
 "is_employed": true,
 "address": {
 "city": "New York",
 "street": "5th Avenue",
 "house_number": 123
 }
}"""

json_string_e4 = """{
 "name": "John",
 "age": 32,
 "email": "john.doe.example.com",
 "is_employed": true,
 "address": {
 "city": "New York",
 "street": "5th Avenue",
 "house_number": 123
 }
}"""

json_string = """{
 "name": "John",
 "age": 22,
 "email": "john.doe@example.com",
 "is_employed": true,
 "address": {
 "city": "New York",
 "street": "5th Avenue",
 "house_number": 123
 }
}"""

json_string_e5 = """{
 "name": "J1",
 "age": 32,
 "email": "john.doe@example.com",
 "is_employed": true,
 "address": {
 "city": "New York",
 "street": "5th Avenue",
 "house_number": 123
 }
}"""

json_string_e6 = """{
 "name": "J",
 "age": 32,
 "email": "john.doe@example",
 "is_employed": true,
 "address": {
 "city": "New York",
 "street": "5th Avenue",
 "house_number": 123
 }
}"""


def process_user_registration(json_data: str):
    try:
        user = User.parse_raw(json_data)
        return user.json()
    except ValidationError as e:
        return str(e)


print(process_user_registration(json_string_e1))
print(process_user_registration(json_string_e2))
print(process_user_registration(json_string_e3))
print(process_user_registration(json_string_e4))
print(process_user_registration(json_string_e5))
print(process_user_registration(json_string_e6))
print(process_user_registration(json_string))
