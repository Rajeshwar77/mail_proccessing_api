from app.api.v1.rules.schema import Rule, ConditionalPredicate, SearchCriteria, SearchPredicate, DateSearchPredicate,SearchField, MoveAction, FlagAction, Flag, MoveFolder
from datetime import datetime, timedelta
from .schema import Rule, SearchCriteria, ConditionalPredicate, SearchPredicate, DateSearchPredicate, Email, MoveAction, FlagAction
from typing import List, Union
from .rule import apply_rule, perform_actions
from sqlalchemy.orm import Session

class CreateRule:
    def __init__(self) -> None:
        self.rules = []
        self.generate_rules()
        
    def generate_rules(self):
        icici_rules = Rule(
            id = 1,
            name="icici",
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
                MoveAction(move_to=MoveFolder.SPAM)
            ]
        )
        linked_in_rules = Rule(
            id=2,
            name="liknedin",
            description="Emails from linkedin received in the last 30 days",
            conditional_predicate=ConditionalPredicate.Any,
            search_predicate=[
                SearchCriteria(
                    search_field=SearchField.SENDER, 
                    search_predicate=SearchPredicate.CONTAINS, 
                    search_value="linkedin"
                ),
                SearchCriteria(
                    search_field=SearchField.RECEIVED_DATE, 
                    search_predicate=DateSearchPredicate.LESS_THAN, 
                    search_value=datetime.now() - timedelta(days=30)
                ),
                SearchCriteria(
                    search_field=SearchField.MESSAGE, 
                    search_predicate=SearchPredicate.CONTAINS, 
                    search_value="job"
                ),
            ],
            actions = [
                FlagAction(mark=Flag.READ)
            ]
        )       
        self.rules.append(icici_rules.dict())
        self.rules.append(linked_in_rules.dict())
        return self.rules

all_rules = CreateRule().generate_rules()

class ApplyRule:
    def __init__(self, rule_id, db) -> None:
        self.rule = None
        self.rule_id = rule_id
        self.db = db
        for each in all_rules:
            if each['id'] == rule_id:
                self.rule = Rule(**each)
                emails = apply_rule(self.db, self.rule)
                self.emails = [
                    Email(
                        subject=email.subject, 
                        sender=email.sender, 
                        receiver=email.receiver, 
                        received_at=email.received_at, 
                        message = email.message,
                        message_id=email.message_id, 
                        history_id=email.history_id, 
                        folder=email.folder,
                        is_read=email.is_read
                    ).dict() for email in emails]
                
                perform_actions(self.db, emails, self.rule.actions)
        if not self.rule:
            raise ValueError("Rule not found")        
        