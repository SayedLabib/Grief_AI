from enum import Enum
from pydantic import BaseModel, ConfigDict
from typing import List, Dict, Any, Optional

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

class CauseOfLoss(str, Enum):
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

class CombinedRequest(BaseModel):
    user_thoughts: str
    relationship: Relationship
    cause_of_loss: CauseOfLoss

class Activity(BaseModel):
    time_frame: str
    activity: str
    description: str | None = None

class ToolInfo(BaseModel):
    description: str
    tools: List[str]

class DailySchedule(BaseModel):
    date: str
    morning: List[Activity]
    noon: List[Activity]
    afternoon: List[Activity]
    evening: List[Activity]
    night: List[Activity]
    
    model_config = ConfigDict(from_attributes=True)

class CombinedResponse(BaseModel):
    mood: Emotion
    titles: Dict[str, ToolInfo]
    schedule: DailySchedule