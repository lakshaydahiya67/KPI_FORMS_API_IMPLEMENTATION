from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class WheelSpecificationFields(BaseModel):
    axleBoxHousingBoreDia: Optional[str] = None
    bearingSeatDiameter: Optional[str] = None
    condemningDia: Optional[str] = None
    intermediateWWP: Optional[str] = None
    lastShopIssueSize: Optional[str] = None
    rollerBearingBoreDia: Optional[str] = None
    rollerBearingOuterDia: Optional[str] = None
    rollerBearingWidth: Optional[str] = None
    treadDiameterNew: Optional[str] = None
    variationSameAxle: Optional[str] = None
    variationSameBogie: Optional[str] = None
    variationSameCoach: Optional[str] = None
    wheelDiscWidth: Optional[str] = None
    wheelGauge: Optional[str] = None
    wheelProfile: Optional[str] = None

class WheelSpecificationCreate(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: str
    fields: WheelSpecificationFields

class WheelSpecificationResponse(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: str
    fields: WheelSpecificationFields

class WheelSpecificationListResponse(BaseModel):
    success: bool
    message: str
    data: List[WheelSpecificationResponse]

class WheelSpecificationCreateResponse(BaseModel):
    success: bool
    message: str
    data: dict