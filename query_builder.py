from pydantic import BaseModel, Field
from marvin import ai_model, ai_classifier
import marvin
from typing import Tuple, Optional, List
from enum import Enum




@ai_model
class CustomQueryBase(BaseModel):
    """
    Custom query base class for creating custom queries. Can to define fields that should appear in all queries.
    """
    full_text: str = Field(description="Full text of the document")
    
    
from marvin import ai_classifier
from enum import Enum


@ai_classifier
class YesorNo(Enum):
    """Classifies that evaluates results of query"""

    YES = "Yes"
    NO = "No"


@ai_classifier
class Sentiment(Enum):
    """Classifies that evaluates results of query"""

    POSITIVE = "Positive"
    NEUTRAL = "Neutral"
    NEGATIVE = "Negative"






# Creates tuple for use in create_model
def create_param_tuple(name: str, data_type: str, description: str, required: bool = True) -> Tuple[str, Tuple[Optional[type], Field]]:
    if data_type == list:
        return (name, (List[str], Field(description=description)))
    elif not required:
        return (name, (Optional[data_type], Field(description=description)))
    else:
        return (name, (data_type, Field(description=description)))

    
   