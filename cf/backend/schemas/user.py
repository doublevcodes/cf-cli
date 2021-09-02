from datetime import datetime
from typing import Annotated, Field, Optional

from pydantic import BaseModel

from cf.backend.schemas.utils import id
from cf.backend.schemas.organization import Organization

class User(BaseModel):
    id: Annotated[str, id]
    email: Annotated[str, Field(..., max_length=90)]
    first_name: Optional[Annotated[str, Field(..., max_length=60)]]
    last_name: Optional[Annotated[str, Field(..., max_length=60)]]
    username: Annotated[str, Field(..., min_length=3, max_length=90, regex=r"^[a-z0-9]+([\-\._]?[a-z0-9]+)+$")]
    telephone: Optional[Annotated[str, Field(..., max_length=20)]]
    country: Optional[Annotated[str, Field(..., max_length=30)]]
    zipcode: Optional[Annotated[str, Field(..., max_length=20)]]
    created_on: datetime
    modified_on: datetime
    two_factor_authentication_enabled: bool
    suspended: bool
    organizations: list[Organization]
    betas: list[str]