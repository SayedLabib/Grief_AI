from pydantic import BaseModel
from typing import Dict, List
from enum import Enum

class Emotion(str, Enum):
    HAPPY = "Happy"
    SAD = "Sad"
    ANGRY = "Angry"
    NUMB = "Numb"
    CONFUSED = "Confused"

class Relationship(str, Enum):
    PARENT = "Parent"
    CHILD = "Child"
    SIBLING = "Sibling"
    PARTNER = "Partner"
    FRIEND = "Friend"
    GRANDPARENT = "Grandparent"
    PET = "Pet"
    TAPS = "TAPS"
    OTHER = "Other"

class CauseOfDeath(str, Enum):
    ILLNESS = "Illness"
    ACCIDENT = "Accident"
    SUICIDE = "Suicide"
    NATURAL = "Natural"
    MURDER = "Murder"
    HOMICIDE = "Homicide"
    OVERDOSE = "Overdose"
    STILLBIRTH = "Stillbirth"
    COVID19 = "COVID19"
    OTHER = "Other"
    AFSP = "AFSP"

class UserInput(BaseModel):
    user_thoughts: str
    relationship: Relationship
    cause_of_loss: CauseOfDeath

class ToolInfo(BaseModel):
    description: str
    tools: List[str]

class ToolsResponse(BaseModel):
    mood: Emotion
    titles: Dict[str, ToolInfo]

# Response models for API validation
class ErrorResponse(BaseModel):
    detail: str