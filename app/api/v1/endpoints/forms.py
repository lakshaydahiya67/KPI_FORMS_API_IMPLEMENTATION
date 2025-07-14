from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional, List
from datetime import datetime

from app.db.database import get_db
from app.db.models import WheelSpecification, BogieChecksheet
from app.schemas.wheel_specification import (
    WheelSpecificationCreate,
    WheelSpecificationListResponse,
    WheelSpecificationCreateResponse,
    WheelSpecificationResponse,
    WheelSpecificationFields
)
from app.schemas.bogie_checksheet import (
    BogieChecksheetCreate,
    BogieChecksheetCreateResponse
)

router = APIRouter()

@router.get("/wheel-specifications", response_model=WheelSpecificationListResponse)
async def get_wheel_specifications(
    formNumber: Optional[str] = Query(None),
    submittedBy: Optional[str] = Query(None), 
    submittedDate: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(WheelSpecification)
    
    if formNumber:
        query = query.filter(WheelSpecification.form_number.ilike(f"%{formNumber}%"))
    if submittedBy:
        query = query.filter(WheelSpecification.submitted_by.ilike(f"%{submittedBy}%"))
    if submittedDate:
        try:
            date_obj = datetime.strptime(submittedDate, "%Y-%m-%d").date()
            query = query.filter(WheelSpecification.submitted_date >= date_obj)
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD")
    
    specifications = query.all()
    
    response_data = []
    for spec in specifications:
        fields = WheelSpecificationFields(
            axleBoxHousingBoreDia=spec.axle_box_housing_bore_dia,
            bearingSeatDiameter=spec.bearing_seat_diameter,
            condemningDia=spec.condemning_dia,
            intermediateWWP=spec.intermediate_wwp,
            lastShopIssueSize=spec.last_shop_issue_size,
            rollerBearingBoreDia=spec.roller_bearing_bore_dia,
            rollerBearingOuterDia=spec.roller_bearing_outer_dia,
            rollerBearingWidth=spec.roller_bearing_width,
            treadDiameterNew=spec.tread_diameter_new,
            variationSameAxle=spec.variation_same_axle,
            variationSameBogie=spec.variation_same_bogie,
            variationSameCoach=spec.variation_same_coach,
            wheelDiscWidth=spec.wheel_disc_width,
            wheelGauge=spec.wheel_gauge,
            wheelProfile=spec.wheel_profile
        )
        
        response_data.append(WheelSpecificationResponse(
            formNumber=spec.form_number,
            submittedBy=spec.submitted_by,
            submittedDate=spec.submitted_date.strftime("%Y-%m-%d"),
            fields=fields
        ))
    
    return WheelSpecificationListResponse(
        success=True,
        message="Filtered wheel specification forms fetched successfully.",
        data=response_data
    )

@router.post("/wheel-specifications", response_model=WheelSpecificationCreateResponse)
async def create_wheel_specification(
    specification: WheelSpecificationCreate,
    db: Session = Depends(get_db)
):
    # Check if form number already exists
    existing = db.query(WheelSpecification).filter(
        WheelSpecification.form_number == specification.formNumber
    ).first()
    
    if existing:
        raise HTTPException(
            status_code=400, 
            detail="Form number already exists"
        )
    
    # Parse date
    try:
        submitted_date = datetime.strptime(specification.submittedDate, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD")
    
    # Create new specification
    db_specification = WheelSpecification(
        form_number=specification.formNumber,
        submitted_by=specification.submittedBy,
        submitted_date=submitted_date,
        axle_box_housing_bore_dia=specification.fields.axleBoxHousingBoreDia,
        bearing_seat_diameter=specification.fields.bearingSeatDiameter,
        condemning_dia=specification.fields.condemningDia,
        intermediate_wwp=specification.fields.intermediateWWP,
        last_shop_issue_size=specification.fields.lastShopIssueSize,
        roller_bearing_bore_dia=specification.fields.rollerBearingBoreDia,
        roller_bearing_outer_dia=specification.fields.rollerBearingOuterDia,
        roller_bearing_width=specification.fields.rollerBearingWidth,
        tread_diameter_new=specification.fields.treadDiameterNew,
        variation_same_axle=specification.fields.variationSameAxle,
        variation_same_bogie=specification.fields.variationSameBogie,
        variation_same_coach=specification.fields.variationSameCoach,
        wheel_disc_width=specification.fields.wheelDiscWidth,
        wheel_gauge=specification.fields.wheelGauge,
        wheel_profile=specification.fields.wheelProfile
    )
    
    db.add(db_specification)
    db.commit()
    db.refresh(db_specification)
    
    return WheelSpecificationCreateResponse(
        success=True,
        message="Wheel specification submitted successfully.",
        data={
            "formNumber": db_specification.form_number,
            "submittedBy": db_specification.submitted_by,
            "submittedDate": db_specification.submitted_date.strftime("%Y-%m-%d"),
            "status": "Saved"
        }
    )

@router.post("/bogie-checksheet", response_model=BogieChecksheetCreateResponse)
async def create_bogie_checksheet(
    checksheet: BogieChecksheetCreate,
    db: Session = Depends(get_db)
):
    # Check if form number already exists
    existing = db.query(BogieChecksheet).filter(
        BogieChecksheet.form_number == checksheet.formNumber
    ).first()
    
    if existing:
        raise HTTPException(
            status_code=400, 
            detail="Form number already exists"
        )
    
    # Parse dates
    try:
        inspection_date = datetime.strptime(checksheet.inspectionDate, "%Y-%m-%d")
        date_of_ioh = None
        if checksheet.bogieDetails.dateOfIOH:
            date_of_ioh = datetime.strptime(checksheet.bogieDetails.dateOfIOH, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD")
    
    # Create new checksheet
    db_checksheet = BogieChecksheet(
        form_number=checksheet.formNumber,
        inspection_by=checksheet.inspectionBy,
        inspection_date=inspection_date,
        bogie_no=checksheet.bogieDetails.bogieNo,
        date_of_ioh=date_of_ioh,
        deficit_components=checksheet.bogieDetails.deficitComponents,
        incoming_div_and_date=checksheet.bogieDetails.incomingDivAndDate,
        maker_year_built=checksheet.bogieDetails.makerYearBuilt,
        axle_guide=checksheet.bogieChecksheet.axleGuide,
        bogie_frame_condition=checksheet.bogieChecksheet.bogieFrameCondition,
        bolster=checksheet.bogieChecksheet.bolster,
        bolster_suspension_bracket=checksheet.bogieChecksheet.bolsterSuspensionBracket,
        lower_spring_seat=checksheet.bogieChecksheet.lowerSpringSeat,
        adjusting_tube=checksheet.bmbcChecksheet.adjustingTube,
        cylinder_body=checksheet.bmbcChecksheet.cylinderBody,
        piston_trunnion=checksheet.bmbcChecksheet.pistonTrunnion,
        plunger_spring=checksheet.bmbcChecksheet.plungerSpring
    )
    
    db.add(db_checksheet)
    db.commit()
    db.refresh(db_checksheet)
    
    return BogieChecksheetCreateResponse(
        success=True,
        message="Bogie checksheet submitted successfully.",
        data={
            "formNumber": db_checksheet.form_number,
            "inspectionBy": db_checksheet.inspection_by,
            "inspectionDate": db_checksheet.inspection_date.strftime("%Y-%m-%d"),
            "status": "Saved"
        }
    )