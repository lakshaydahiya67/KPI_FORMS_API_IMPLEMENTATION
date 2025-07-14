from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class BogieDetails(BaseModel):
    bogieNo: Optional[str] = None
    dateOfIOH: Optional[str] = None
    deficitComponents: Optional[str] = None
    incomingDivAndDate: Optional[str] = None
    makerYearBuilt: Optional[str] = None

class BogieChecksheetFields(BaseModel):
    axleGuide: Optional[str] = None
    bogieFrameCondition: Optional[str] = None
    bolster: Optional[str] = None
    bolsterSuspensionBracket: Optional[str] = None
    lowerSpringSeat: Optional[str] = None

class BMBCChecksheet(BaseModel):
    adjustingTube: Optional[str] = None
    cylinderBody: Optional[str] = None
    pistonTrunnion: Optional[str] = None
    plungerSpring: Optional[str] = None

class BogieChecksheetCreate(BaseModel):
    formNumber: str
    inspectionBy: str
    inspectionDate: str
    bogieDetails: BogieDetails
    bogieChecksheet: BogieChecksheetFields
    bmbcChecksheet: BMBCChecksheet

class BogieChecksheetCreateResponse(BaseModel):
    success: bool
    message: str
    data: dict