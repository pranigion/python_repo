from pydantic import BaseModel,Field

class input(BaseModel):
    input_query: str =Field(...,description="input")

class output(BaseModel):
    input_query:str=Field(...,description="input")
    output_query:str=Field(...,description="output")

def process(param1:input)->output:
    input_res= param1.input_query
    result="Hello bro"
    return output(**{"input_query":input_res,"output_query":result})

pyd_inp = input(**{"input_query":"Hi how are you !!"})
print(process(pyd_inp))
print('-------------------------------')
print('-----model_dump-----')
print(process(pyd_inp).model_dump)
print('-------------------------------')
print('-----model_dump_json-----')
print(process(pyd_inp).model_dump_json)