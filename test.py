import marvin
from marvin import ai_model
from pydantic import BaseModel, Field


@ai_model
class CustomQueryBase(BaseModel):
    """
    Custom query base class for creating custom queries. Can to define fields that should appear in all queries.
    """
    full_text: str = Field(description="Full text of the document")
    
    
answer = CustomQueryBase("The patient needs to perform a MRI which is a type of scan that looks at the brain.")
print(answer)