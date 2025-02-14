# Email Inbox Filter

This project is built using FastAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.7+ that's based on standard Python type hints.

## Features

- **List Rules**: Retrieve a list of filtering rules that can be applied to your email inbox.
- **Apply Rule**: Use the `apply rule` endpoint to apply a specific filtering rule to organize your inbox.

## Folder format and structure

```
├── README.md
├── alembic # Migration library
│   ├── README
│   ├── env.py # Migration override through code
│   ├── script.py.mako
│   └── versions
│       └── 8e917efa703b_user_and_email_table_migration.py
├── alembic.ini # Migration config
├── app
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── endpoints.py # Restapi for the all version
│   │   └── v1
│   │       ├── endpoints.py # Restapi v1 for the modules like rules, .., ..
│   │       └── rules # Module where rules will be created
│   │           ├── __init__.py
│   │           ├── controller.py # Business logic to setup the rules
│   │           ├── endpoints.py # Restapi for operation specific to rule module
│   │           ├── rule.py # file which apply the rule
│   │           └── schema.py # See the Pydantic model of the rules, ..
│   ├── config.py - General config with should changed based on environment
│   ├── database.py - Configuration releated to DB.
│   ├── dependency.py - Holding depenecy resoucres, for ex global db variable
│   ├── main.py - Main file where the api starts
│   └── models.py - Models which can structure the database schema
└── requirements.txt
```
## API Documentation

The API documentation for this project is available in the `doc` folder. Navigate to the `doc` folder to find detailed information about the API endpoints, their expected inputs, and outputs.


## Installation
To set up and run the FastAPI project from your repository, follow these steps:



# 1. Clone the Repository: 
Clone your project repository to your local machine.


```bash

git clone https://github.com/Rajeshwar77/mail_proccessing_api.git

cd mail_proccessing_api

```

# 2. Create a Virtual Environment: 
It's recommended to use a virtual environment for Python projects. This keeps dependencies required by different projects separate by creating isolated environments for them.

```bash
python3 -m venv venv
source venv/bin/activate  # On Unix/macOS
.\venv\Scripts\activate   # On Windows
```


# 3. Install Dependencies: 
Install the required packages, including FastAPI and any others listed in your requirements.txt file.

```bash
pip install -r requirements.txt
```

# 4. Run the Application: 
Use Uvicorn, an ASGI server, to run your FastAPI application. Replace main with the name of your Python file that creates the FastAPI app instance, and app with the name of the FastAPI instance if it's different.

```bash 
uvicorn main:app --reload
```

The ``--reload`` flag makes the server restart after code changes. This is very useful during development but should be omitted in a production environment.

# 5. Access the Application: 

By default, Uvicorn runs on port 8000. You can access your FastAPI application by navigating to ``http://127.0.0.1:8000`` in your web browser. For the API documentation auto-generated by FastAPI, visit ``http://127.0.0.1:8000/docs.``
