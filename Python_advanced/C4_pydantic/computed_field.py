from pydantic import BaseModel,Field,computed_field


class amount(BaseModel):
    unit:int =Field(...,description = "Units")
    amount:int =Field(...,description="amount")

    @computed_field
    @property
    def total_amount(self)->int:
        return self.unit * self.amount
    
pyd_inp = amount(**{"unit":2,"amount":10})
print(pyd_inp)