from pydantic import BaseModel,Field
from typing import Literal

class address_info(BaseModel):
    street: str=Field(...,description="street")
    city : str =Field(...,description="city")
    state :str =Field(...,description="state")


class personal_info(BaseModel):
    name :str=Field(...,description="name")
    age:int=Field(...,description="age")
    gender:Literal["male","female"]=Field(...,description="gender")
    address:address_info=Field(...,description="address")



pyd_inp = personal_info(**{"name":"Prashant",
                           "age":29,
                           "gender":"male",
                           "address":address_info(**{"street":"panama talkies",
                                                     "city":"ballia",
                                                     "state":"uttar pradesh"})})
def main(param1:personal_info):
    return print(param1)

main(pyd_inp)