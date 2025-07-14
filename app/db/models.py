from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, JSON
from sqlalchemy.sql import func
from app.db.database import Base

class WheelSpecification(Base):
    __tablename__ = "wheel_specifications"
    
    id = Column(Integer, primary_key=True, index=True)
    form_number = Column(String, unique=True, index=True, nullable=False)
    submitted_by = Column(String, nullable=False)
    submitted_date = Column(DateTime(timezone=True), server_default=func.now())
    
    # Technical fields
    axle_box_housing_bore_dia = Column(String)
    bearing_seat_diameter = Column(String)
    condemning_dia = Column(String)
    intermediate_wwp = Column(String)
    last_shop_issue_size = Column(String)
    roller_bearing_bore_dia = Column(String)
    roller_bearing_outer_dia = Column(String)
    roller_bearing_width = Column(String)
    tread_diameter_new = Column(String)
    variation_same_axle = Column(String)
    variation_same_bogie = Column(String)
    variation_same_coach = Column(String)
    wheel_disc_width = Column(String)
    wheel_gauge = Column(String)
    wheel_profile = Column(String)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class BogieChecksheet(Base):
    __tablename__ = "bogie_checksheets"
    
    id = Column(Integer, primary_key=True, index=True)
    form_number = Column(String, unique=True, index=True, nullable=False)
    inspection_by = Column(String, nullable=False)
    inspection_date = Column(DateTime(timezone=True), nullable=False)
    
    # Bogie Details
    bogie_no = Column(String)
    date_of_ioh = Column(DateTime(timezone=True))
    deficit_components = Column(Text)
    incoming_div_and_date = Column(String)
    maker_year_built = Column(String)
    
    # Bogie Checksheet Fields
    axle_guide = Column(String)
    bogie_frame_condition = Column(String)
    bolster = Column(String)
    bolster_suspension_bracket = Column(String)
    lower_spring_seat = Column(String)
    
    # BMBC Checksheet Fields
    adjusting_tube = Column(String)
    cylinder_body = Column(String)
    piston_trunnion = Column(String)
    plunger_spring = Column(String)
    
    status = Column(String, default="Saved")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())