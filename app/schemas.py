from pydantic import BaseModel, field_validator, Field

class CreateWalletRequest(BaseModel):
    wallet_name : str = Field(..., max_length=127)
    initial_balance : float = 0


    @field_validator('initial_balance')
    def balance_not_negative(cls,v:float) -> float:
        if v < 0:
            raise ValueError('initial_balance must be not negative')
        return v

    @field_validator('wallet_name')
    def wattel_name_not_empty(cls, v:str) ->str:
        v = v.strip()
        if not v:
            raise ValueError('name is  empty')
        return  v


class OperationRequest(BaseModel):
    wallet_name : str = Field(..., max_length=127)
    amount : float
    description : str | None = Field(None, max_length=127)

    @field_validator('amount')
    def amount_must_be_positive(cls,v:float) -> float:
        if v <=0:
            raise ValueError('Amount must be positive')
        return v
    @field_validator('wallet_name')
    def wattel_name_not_empty(cls, v:str) ->str:
        v = v.strip()
        if not v:
            raise ValueError('name is  empty')
        return  v

