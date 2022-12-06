
from fastapi import APIRouter, status, HTTPException

from ...api_metadata_cache import api_metadata_cache
from ...data_model import Company
from ...data_generator import generate_company_data

router = APIRouter(
    prefix="/v1/company",
    tags=['Company']
)


@router.get("/{jurisdiction_code}/{company_number}", status_code=status.HTTP_200_OK)
def get_company_data(jurisdiction_code: str, company_number: int):
    providers = api_metadata_cache[jurisdiction_code]
    if not providers:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"We do not support {jurisdiction_code} jurisdiction")

    company_profile = Company(**generate_company_data(providers))

    return company_profile.dict()
