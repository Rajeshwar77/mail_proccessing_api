```bash
tree -I venv -I "*.pyc" -I "__pycache__*/
```
.
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

7 directories, 21 files