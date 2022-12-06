def generate_company_data(providers: list):

    print(providers)

    return {
        "company_number": 1,
        "company_name": "Stuff",
        "country": "UK",
        "address": "London",
        "founded": "2022-01-01",
        "disolved": None,
        "related_entities": [
            {"name": "abc"},
            {"name": "b2c"}
        ]
    }
