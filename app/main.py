from fastapi import FastAPI
import uvicorn


from fastapi.responses import PlainTextResponse
from app.api.endpoints import router as version_router

from app.config import settings
from app.dependency import db
app = FastAPI(title=settings.app_name, version="v1")
app.include_router(version_router)

from app.models import User
    
    # db.query(User).all()

@app.get(
    "/health",
    response_class=PlainTextResponse,
    tags=["Health"],
    include_in_schema=False,
)
def health_check():
    return "OK"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80, log_level="debug", reload=True)
    
from app.api.v1.rules.schema import Rule, ConditionalPredicate, SearchCriteria, SearchPredicate, DateSearchPredicate,SearchField, MoveAction, FlagAction, Flag
from datetime import datetime, timedelta


rule = Rule(
    id=0,
    description="Emails from icici received in the last 10 days",
    conditional_predicate=ConditionalPredicate.All,
    search_predicate=[
        SearchCriteria(
            search_field=SearchField.SENDER, 
            search_predicate=SearchPredicate.CONTAINS, 
            search_value="icici"
        ),
        SearchCriteria(
            search_field=SearchField.RECEIVED_DATE, 
            search_predicate=DateSearchPredicate.LESS_THAN, 
            search_value=datetime.now() - timedelta(days=10)
        ),
    ],
    actions=[
        FlagAction(mark=Flag.READ)
    ]
)

print(rule.dict())