from pydantic import BaseModel ,EmailStr

class Customer(BaseModel):
    # id:int
    first_name:str
    last_name:str
    email:EmailStr
    customer_type:str
 

    