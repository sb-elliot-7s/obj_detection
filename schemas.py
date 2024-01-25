from pydantic import BaseModel


class ResultSchema(BaseModel):
    message: str
    status_code: int


class SucessResultSchema(ResultSchema):
    pass


class ErrorResultSchema(BaseModel):
    error: str
