from pydantic import BaseModel, validator, Field
from typing import List, Union, Optional
from datetime import datetime

class ConditionalPredicate(str):
    All = 'All'
    Any = 'Any'

class SearchField(str):
    SENDER = "sender"
    RECEIVER = "receiver"
    SUBJECT = "subject"
    MESSAGE = "message"
    RECEIVED_DATE = "received_at"

class SearchPredicate(str):
    CONTAINS = "contains"
    DOES_NOT_CONTAIN = "does not contain"
    EQUALS = "equals"
    DOES_NOT_EQUAL = "does not equal"

class DateSearchPredicate(str):
    LESS_THAN = "less than"
    GREATER_THAN = "greater than"

class SearchCriteria(BaseModel):
    search_field: SearchField
    search_predicate: Union[SearchPredicate, DateSearchPredicate]
    search_value: Union[str, datetime]
    
    @validator('search_value')
    def validate_value(cls, v, values):
        field_name = values.get('search_field')
        if field_name == SearchField.RECEIVED_DATE and not isinstance(v, datetime):
            raise ValueError("Received date/time field must have a datetime value")
        if field_name != SearchField.RECEIVED_DATE and not isinstance(v, str):
            raise ValueError(f"{field_name} field must have a string value")
        return v

class MoveFolder(str):
    INBOX = "inbox"
    TRASH = "trash"
    SPAM = "spam"
    ARCHIVE = "archive"

class MoveAction(BaseModel):
    move_to: MoveFolder

class Flag(str):
    READ = "read"
    UNREAD = "unread"
    
class FlagAction(BaseModel):
    mark : Flag
    

class Rule(BaseModel):
    id: int
    description: str
    conditional_predicate: ConditionalPredicate
    search_predicate: List[SearchCriteria]
    actions: List[Union[MoveAction, FlagAction]]
    
    # @validator('action')
    # def validate_action(cls, v):
    #     if not v:
    #         raise ValueError("Action must have at least one item")
    #     return v
    
class Email(BaseModel):
    sender: str
    subject: str
    receiver: str
    message: Optional[str]
    received_at: datetime
    history_id: str
    message_id: str
    folder: Optional[str] = "inbox"   