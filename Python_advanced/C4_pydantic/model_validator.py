from pydantic import BaseModel,Field,model_validator
from typing import Optional

class pass_auth(BaseModel):
    username:str =Field(...,description="Username")
    password:str=Field(...,min_length=3,max_length=12,description="password")
    confirm_password:str=Field(...,min_length=3,max_length=12,description="Confirm password")

    @model_validator(mode='after')
    def pass_check(values):
        if values.password != values.confirm_password:
            raise ValueError("password not matching")
        else:
            return values
       
pyd_inp= pass_auth(**{"username":"pranigion","password":"pathak123","confirm_password":"pathak123"})
print(pyd_inp)