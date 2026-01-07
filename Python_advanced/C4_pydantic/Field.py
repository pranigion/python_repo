# from pydantic import BaseModel,Field,EmailStr
# from typing import Dict,List,Optional,Literal

# class per_info(BaseModel):
#     id : Optional[int] =Field(...,ge=0,description="id of a person")
#     name :str =Field(...,min_length=3,max_length=20,description = "name of a person")
#     gender:Literal["male","female","none"] =Field(...,description ="gender of a person")
#     place : str =Field(...,description="place of a person")
#     email : EmailStr = Field(...,description="email of a person")


# pyd_inp = per_info(**{"name" :"Prashant","gender":"male","place":"ballia","email":"example@gmail.com"})
# # print(pyd_inp)
# def main(param1:per_info):
#     print("id is: ",param1.id)
#     print("name is: ",param1.name)
#     print("gender is: ",param1.gender)
#     print("place is: ",param1.place)
#     print("email is: ",param1.email)


# main(pyd_inp)


from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Dict, Any, List, Literal


class personal_info(BaseModel):

    name : str = Field(...,min_length=3,max_length=20,description="this is name")
    age : int | None = Field(...,ge=0, description="this is age")
    email : EmailStr = Field(...,description="this is email")
    gender : Literal["male", "female", "other"] = Field(...,description="this is gender")
    salaries : List[int] = Field(...,description="this is salaries")

def main(para1:personal_info):

    print("name:", para1.name)
    print("age:", para1.age)
    print("email:", para1.email)
    print("gender:", para1.gender)
    print("salaries:", para1.salaries)

pyd_ins = personal_info(**{"name": "Ansh Lamba", "age": 0, "email": "anshlamba@example.com", "gender": "male", "salaries": [0,0]})

main(pyd_ins)
