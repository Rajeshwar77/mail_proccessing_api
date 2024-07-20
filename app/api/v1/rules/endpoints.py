from fastapi import APIRouter, Depends
from .controller import CreateRule, ApplyRule
from app.dependency import get_db
from sqlalchemy.orm import Session


router = APIRouter()

@router.get("/", tags=["Rules"], description="Get all rules")
def get_rules():
    rule = CreateRule()
    rule.generate_rules()
    return rule.rules

@router.get("filter/{rule_id}", tags=["Rules"], description="Filter by given rule id")
def apply_rule(rule_id: int, db: Session = Depends(get_db)):
    approval_rule = ApplyRule(rule_id, db)
    return approval_rule.emails