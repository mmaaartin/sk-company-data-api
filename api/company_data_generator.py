import json
import requests

from datetime import datetime

DATE_FORMAT = '%Y-%m-%d'

def get_company_number(company_data: dict) -> str:
    if 'companyNumber' in company_data:
        return company_data['companyNumber']
    else:
        return company_data['company_number']

def get_company_name(company_data: dict) -> str:
    if 'companyName' in company_data:
        return company_data['companyName']
    else:
        return company_data['company_name']


def get_company_country(company_data: dict) -> str:
    if 'country' in company_data:
        return company_data['country']
    else:
        return company_data['jurisdiction_code']


def get_company_address(company_data: dict) -> str:
    if 'address' in company_data:
        return company_data['address']
    else:
        return ' '.join(company_data['official_address'].values())


def get_company_founded_date(company_data: dict) -> str:
    if 'dateFrom' in company_data:
        if company_data['dateFrom']:
            datetime_object = datetime.strptime(company_data['dateFrom'], '%d/%m/%Y')
            return datetime_object.strftime(DATE_FORMAT)
        return None
    else:
        if company_data['date_established']:
            return '-'.join(map(str, company_data['date_established'].values()))
        return None


def get_company_dissolved_date(company_data: dict) -> str:
    if 'dateTo' in company_data:
        if company_data['dateTo']:
            datetime_object = datetime.strptime(company_data['dateTo'], '%d/%m/%Y')
            return datetime_object.strftime(DATE_FORMAT)
        return None
    else:
        if company_data['date_dissolved']:
            return '-'.join(map(str, company_data['date_dissolved'].values()))
        return None


def get_relevant_entities_b(company_data: dict) -> list:
    company_related_entities = []
    related_entities = company_data['relatedPersons'] + company_data['relatedCompanies']
    for entity in related_entities:
        formatted_entity = {
            "name": entity.get('name'),
            "type": entity.get('type'),
            "date_started": None if not entity.get('dateFrom') else datetime.strptime(entity.get('dateFrom'), '%d/%m/%Y').strftime(DATE_FORMAT),
            "date_ended": None if not entity.get('dateTo') else datetime.strptime(entity.get('dateTo'), '%d/%m/%Y').strftime(DATE_FORMAT)
        }
        company_related_entities.append(formatted_entity)

    return company_related_entities


def get_relevant_entities_a(company_data: dict) -> list:
    company_related_entities = []
    related_entities = company_data['officers']
    for entity in related_entities:
        formatted_entity = {
            "name": entity.get('name') if entity.get('name') else entity.get('first_name') + entity.get('last_name'),
            "type": entity.get('role'),
            "date_started": None if not entity.get('dateFrom') else '-'.join(map(str, entity.get('date_from').values())),
            "date_ended": None if not entity.get('date_to') else '-'.join(map(str, entity.get('date_to').values()))
        }
        company_related_entities.append(formatted_entity)

    return company_related_entities


def get_company_related_entities(company_data: dict) -> list:

    if 'relatedPersons' in company_data:
        return get_relevant_entities_b(company_data)
    else:
        return get_relevant_entities_a(company_data)

def generate_company_profile(providers: list, jurisdiction_code: str, company_number: int) -> dict:
    company_data = {}

    endpoints = [provider['url'] + provider['endpoint'] for provider in providers]

    for endpoint in endpoints:
        response = requests.get(endpoint.format(jurisdiction_code=jurisdiction_code,
                                                company_number=company_number,
                                                verify=True))
        if response.status_code == 200:
            company_data |= json.loads(response.text)
        else:
            return None

    return {
        'company_number': get_company_number(company_data),
        'company_name': get_company_name(company_data),
        'country': get_company_country(company_data),
        'address': get_company_address(company_data),
        'founded': get_company_founded_date(company_data),
        'dissolved': get_company_dissolved_date(company_data),
        'related_entities': get_company_related_entities(company_data),
    }
