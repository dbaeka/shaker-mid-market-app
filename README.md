# Mid Market Rate

Application to get the mid-market rate for various currencies

Endpoints Provided

**POST `/api/v1/rates/convert`** Convert an amount using the mid-rate between two currencies. Returns 200 HTTP status
code on success and 400 HTTP status codes on content errors

**GET `/api/v1/rates/currencies`** Get the list of accepted currencies as a json. Returns 200 HTTP status code on
success and 400 HTTP status code on content errors

**GET `/api/v1/rates/history`** Get the list of past conversions. Returns 200 HTTP status code on success and 400 HTTP
status code on content errors

**GET `/api/v1/users/me`** Returns information about the user with the current access token

More documentation can be found on [http://127.0.0.1:8000/docs]()

## Set Up

Instructions for environment setup and running your code and tests

**Requires python3.10 and pip with poetry to follow the steps below**

- In your python environment or virtual environment (make sure to call `source venv/bin/activate` to activate the venv.
  Also install virtualenv using pip if you require to do so), make sure python 3.10+ is installed and active
- Run `poetry install`
- Run `cp .env.example .env` to set up .env for setting env variables
- Run `bash launch.sh` to start the server. Alternatively, you can run the commands in the script individually.
  A default user is generated with username and password as test_user and password respectively. This is found in the
  .env file as `TEST_USER` and `TEST_USER_PASSWORD` and can be modified. The authorization uses `Basic authentication`
  and the token can be generated using the `base64` encode of `username:password`. For the default user, the token will
  be `dGVzdF91c2VyOnBhc3N3b3Jk`

### Running Tests

Run tests with `python -m pytest`

## Context on solution and approach, including any assumptions made

Assumptions made on the solution are listed below:

- A stale time of 10s (default but can be changed in the env file) is used to update the data sourced from the chosen
  provider (XE). This means the mid-rate is not older than 10s old and is always replaced. This is to prevent frequent
  calls to the provider which might lead to blacklisting
- Only user generated requests are stored in the database in the conversion table
- Saving the historic data scraped from the provider is not necessary for the base functionality and may add to storage
  footprint but rather saved in the `/storage/app` directory as `currencies.json` and `rates.json`. A timestamp
  parameter is saved at the time of the scrape to determine how stale the data is
- While Celery beat can be used to run a synchronized task to retrieve the scraped data at intervals, it is not fully
  implemented
- sqllite is used as the database primarily to ease with running the application locally. Some design choices such as
  the data type for the primary key being Integer instead of BigInteger for scalability is done to support sqllite's
  issue with auto-incrementing non-Integer set data type
- It is assumed that the keys and structure of the parsed data from the scraped sources will be stable for the duration
  when this application needs to run successfully
- Amount to convert will be greater than 0 always

## What are the shortcomings of your solution?

- Since scraped data is not stored in the db, the json files in the `/storage/app` folder acts as the point of truth
  which can be lost and will be impossible to retrieve past data
- There is no rate limiting on the endpoints which can lead to high number of requests and in turn a high number of
  calls to the provider even with the 10s STALE TIME set
- More descriptive messaging for errors can be provided for the various HTTP status errors
- The API security of the API can use a more robust scheme such as `Bearer` with password authentication
- Test covergae can be improved on other functions such as those by the service classes

## Additions

- Improve the API for `/history` to include date range
- Add a DB (preferably a NoSQL db) to store scraped data and historic data: elasticsearch can be used to index the data
  for quick searches and to build real time tickers. Data is key and can inform on future analytics
- Require IDs for the conversions returned in the JSON spec to easily identify a conversion and get it in the future
- Explore use of Redis to cache data instead of the file method employed in this solution
- Strengthen auth approach. Additionally, rate limits can be applied to restrict
  heavy traffic which can resemble DDoS attacks
- Standardize the response structure of the JSON returned by the service. A status and message field can help determine
  if the service was successfully completed
- Improve the logging with file logging and use of production ready services such as Sentry
  The list is not exhaustive and many improvements can be made to the project