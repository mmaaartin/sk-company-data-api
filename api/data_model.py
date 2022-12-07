from datetime import date
from pydantic import BaseModel
from typing import List, Union, Optional


class Company(BaseModel):
    company_number: int
    company_name: str
    country: str
    address: str
    founded: Union[str, None]
    dissolved: Union[str, None]
    related_entities: Optional[List[dict]]
