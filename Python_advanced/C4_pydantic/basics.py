from pydantic import BaseModel,Field,StrictInt

class info(BaseModel):
    id : StrictInt = Field(...,description="id of a person")
    name : str = Field(...,description= "name of the person")


# pyd_input = info(id = 1,name = "ansh")
pyd_input = info(**{"id" :"1","name":"ansh"})
print(pyd_input)

def main(param1: info):
    print("Hello pk")

main(pyd_input)
