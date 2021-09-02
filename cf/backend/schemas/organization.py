from typing import Annotated, Literal

from pydantic import BaseModel, Field

from cf.backend.schemas.utils import id


class Organization(BaseModel):
    id: Annotated[str, id]
    name: Annotated[str, Field(..., max_length=100)]
    status: Literal["member", "invited"]
    permissions: list[Annotated[str, Field(..., max_length=160)]]
    roles: list[Annotated[str, Field(..., max_length=120)]]