from pydantic import BaseModel
from typing import List, Optional

class CropBase(BaseModel):
    Seed_Provider: str
    Seed_Type: str
    Hybrid_Type: str
    Seed_Number: str

    class Config:
        from_attributes = True

class CropCreate(CropBase):
    pass

class Crop(CropBase):
    Crop_ID: int

    class Config:
        from_attributes = True


class FarmerBase(BaseModel):
    FName: str
    LName: str
    Phone_Number: str
    Email: str
    Street: str
    City: str
    State: str
    Zipcode: int

    class Config:
        from_attributes = True

class FarmerCreate(FarmerBase):
    pass

class Farmer(FarmerBase):
    Farmer_ID: int
    fields: List['Field'] = []  # Forward reference

    class Config:
        from_attributtes = True


class FieldBase(BaseModel):
    Farmer_ID: int
    Longitude: float
    Latitude: float
    Soil_Type: str
    Elevation: int

    class Config:
        from_attributes = True

class FieldCreate(FieldBase):
    pass

class Field(FieldBase):
    Field_ID: int
    field_data: List['FieldData'] = []  # Forward reference
    probes: List['Probe'] = []  # Forward reference

    class Config:
        from_attributes = True


class FieldDataBase(BaseModel):
    Field_ID: int
    Water_ID: int
    Irrigation_Status: bool
    Avg_Yield: float
    Crop_ID: int
    Tillage: str
    Field_Residue: bool
    Planting_Style: str
    Depth: float
    Cover_Crop: bool
    Row_Spacing: float
    Pivot_Corners: str

    class Config:
        from_attributes = True

class FieldDataCreate(FieldDataBase):
    pass

class FieldData(FieldDataBase):
    FDID: int

    class Config:
        from_attributes = True


class ProbeBase(BaseModel):
    Field_ID: int
    Salinity: float
    Temperature: float
    Moisture: float
    Nitrogen: float
    Phosphorus: float
    Potassium: float
    Sunlight: float
    pH: float

    class Config:
        from_attributes = True

class ProbeCreate(ProbeBase):
    pass

class Probe(ProbeBase):
    Probe_ID: int

    class Config:
        from_attributes = True


class WaterBase(BaseModel):
    Avg_Annual_Rainfall: float
    Irrigation_Application: float
    Runoff: float
    Leaching: bool

    class Config:
        from_attributes = True

class WaterCreate(WaterBase):
    pass

class Water(WaterBase):
    Water_ID: int

    class Config:
        from_attributes = True


# Setting forward references to resolve circular dependencies
Farmer.update_forward_refs()
Field.update_forward_refs()
FieldData.update_forward_refs()
Probe.update_forward_refs()
