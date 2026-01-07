from pydantic import BaseModel,Field,field_validator
from typing import Literal

class per_info(BaseModel):
    name : str =Field(...,min_length=3,max_length=20,description="name of a person")
    gender:Literal['M','F','N']=Field(...,description="gender of a person")
    age:int|None =Field(...,ge=0,le=30,description="age of a paerson")
    email: str =Field(...,description="email of a person")

    @field_validator('email')
    def email_check(cls,value):
        if '@' not in value:
            raise ValueError("Invalid email of pathak bcoz @ missing")
        elif '.com' not in value:
            raise ValueError("Invalid email of pathak because .com missing")
        
        else: 
         return value
    
pyd_inp =per_info(**{"name":"Prashant","gender":'M',"age":30,"email":"Example@gmail.com"})
print(pyd_inp)