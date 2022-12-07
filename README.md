# SK Company Data API

## About

THis is an API based application which is running on FastAPI. It aggregates and standardises company data from a number of different APIs and can be used a single point of entry.

## How to run the project locally?

### Prerequisites

* Docker
* Browser or any other tool to call the API endpoint

### Steps

1. Clone the repository
2. Enter the directory and run
```
docker build -t <IMAGE NAME> .
```
3. Once the build is finishes, run
```
docker run -dp 8000:8000 <IMAGE NAME>
```
4. The command above will start the application which will be accessible through http://localhost:8000/. You should see the following message once {"message":"Hello to Company Data API!"}, if that's the case everything is running as expected.
5. Query company data using the following structure: http://localhost:8000/v1/company/{jurisdiction_code}/{company_number}