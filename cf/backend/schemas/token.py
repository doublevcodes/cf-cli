from datetime import datetime
from typing import Annotated, Literal

from pydantic import BaseModel, Field

from cf.backend.schemas.token_condition import Condition
from cf.backend.schemas.utils import id

class Token(BaseModel):
    expires_on: datetime
    not_before: datetime
    name: Annotated[str, Field(..., max_length=120)]
    policies: list
    status: Literal["active", "disabled", "expired"]
    issued_on: datetime
    modified_on: datetime
    id: Annotated[str, id]
    condition: Condition
