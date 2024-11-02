from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session, aliased
from sqlalchemy import join
from app.database import get_db  # Your database session dependency
from app.models import Field, Crop, FieldData, Probe, Water,Farmer
from app import schemas  # Your SQLAlchemy models
import os

router = APIRouter(
    prefix="/field",
    tags=["field"]
)


templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), 'templates'))


@router.get("/", response_class=HTMLResponse)
async def get_fields(request: Request, db: Session = Depends(get_db)):
    # Use standard join without aliases
    results = (
        db.query(FieldData,Crop,Water,Field,Probe,Farmer)
        .select_from(FieldData)
        .join(Field, FieldData.Field_ID == Field.Field_ID)
        .join(Crop, FieldData.Crop_ID == Crop.Crop_ID)
        .join(Water, FieldData.Water_ID == Water.Water_ID)
        .join(Probe, Field.Field_ID == Probe.Field_ID)
        .join(Farmer, Field.Farmer_ID == Farmer.Farmer_ID)
        .all())
    

    # Transform the results for the template
    fields_list = []
    for field, field_data, crop, probe, water, farmer in results:
        fields_list.append({
            "Field_ID": field.Field_ID,
            "Farmer Fname": farmer.Fname,
            "Farmer Lname": farmer.Lname,
            "Longitude": field.Longitude,
            "Latitude": field.Latitude,
            "Soil_Type": field.Soil_Type,
            "Elevation": field.Elevation,
            "FDID": field_data.FDID,
            "Avg_Yield": field_data.Avg_Yield,
            "Irrigation_Status": field_data.Irrigation_Status,
            "Water_ID": field_data.Water_ID,
            "Crop_ID": crop.Crop_ID,
            "Seed_Provider": crop.Seed_Provider,
            "Salinity": probe.Salinity,
            "Temperature": probe.Temperature,
            "Moisture": probe.Moisture,
            "Phophorus": probe.Phophorus,
            "Nitrogen": probe.Nitrogen,
            "Potassium": probe.Potassium,
            "Sunlight": probe.Sunlight,
            "Ph": probe.Ph,
            "Avg_Annual_Rainfall": water.Avg_Annual_Rainfall,
            "Irrigation_App": water.Irrigation_App,
            "Runoff": water.Runoff,
            "Leaching": water.Leaching
        })

    return templates.TemplateResponse("fields.html", {"request": request, "fields": fields_list})