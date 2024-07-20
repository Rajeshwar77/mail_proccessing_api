from sqlalchemy.orm import Session
from sqlalchemy import and_, or_

from .schema import Rule, SearchCriteria, ConditionalPredicate, SearchPredicate, DateSearchPredicate, MoveAction, FlagAction, Flag, MoveFolder
from app.models import Email
from typing import List, Union

def apply_rule(db: Session, rule: Rule) -> List[Email]:
    filters = []

    for criteria in rule.search_predicate:
        field_value = getattr(Email, criteria.search_field)
        if criteria.search_predicate == SearchPredicate.CONTAINS:
            filters.append(field_value.contains(criteria.search_value))
        elif criteria.search_predicate == SearchPredicate.DOES_NOT_CONTAIN:
            filters.append(~field_value.contains(criteria.search_value))
        elif criteria.search_predicate == SearchPredicate.EQUALS:
            filters.append(field_value == criteria.search_value)
        elif criteria.search_predicate == SearchPredicate.DOES_NOT_EQUAL:
            filters.append(field_value != criteria.search_value)
        elif criteria.search_predicate == DateSearchPredicate.LESS_THAN:
            filters.append(field_value < criteria.search_value)
        elif criteria.search_predicate == DateSearchPredicate.GREATER_THAN:
            filters.append(field_value > criteria.search_value)
    if rule.conditional_predicate == ConditionalPredicate.All:
        query = db.query(Email).filter(and_(*filters))
    else:
        query = db.query(Email).filter(or_(*filters))
    return query.all()

def perform_actions(db: Session, emails: List[Email], actions: List[Union[MoveAction, FlagAction, str]]):
    for action in actions:
        print(action)
        if isinstance(action, FlagAction):
            if action == Flag.READ:
                mark_as_read(db, emails)
            elif action == Flag.UNREAD:
                mark_as_unread(db, emails)
        elif isinstance(action, MoveAction):
            move_message(db, emails, action.move_to)

def mark_as_read(db: Session, emails: List[Email]):
    for email in emails:
        email.is_read = True
        db.add(email)
    db.commit()

def mark_as_unread(db: Session, emails: List[Email]):
    for email in emails:
        email.is_read = False
        db.add(email)
    db.commit()

def move_message(db: Session, emails: List[Email], folder: str):
    for email in emails:
        email.folder = folder
        db.add(email)
    db.commit()