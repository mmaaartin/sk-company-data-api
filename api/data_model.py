from datetime import date
from pydantic import BaseModel
from typing import List, Union


class Company(BaseModel):
    company_number: int
    company_name: str
    country: str
    address: str
    founded: date
    disolved: Union[date, None]
    related_entities: List[dict]
