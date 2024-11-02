from sqlalchemy import Column, BigInteger, ForeignKey, Float, Boolean, String
from sqlalchemy.orm import relationship
from app.database import Base  # Assuming Base is your declarative base


class Crop(Base):
    __tablename__ = 'Crop'
    
    Crop_ID = Column(BigInteger, primary_key=True)
    Seed_Provider = Column(String, nullable=False)  # Adjust type as necessary
    Seed_Type = Column(String, nullable=False)
    Hybrid_Type = Column(String, nullable=False)
    Seed_Number = Column(String, nullable=False)

    # Relationship to FieldData
    field_data = relationship("FieldData", back_populates="crop")

class Farmer(Base):
    __tablename__ = 'Farmer'
    
    Farmer_ID = Column(BigInteger, primary_key=True)
    FName = Column(String, nullable=False)
    LName = Column(String, nullable=False)
    Phone_Number = Column(String, nullable=False)
    Email = Column(String, nullable=False)
    Street = Column(String, nullable=False)
    City = Column(String, nullable=False)
    State = Column(String, nullable=False)
    Zipcode = Column(BigInteger, nullable=False)

    # Relationship to Field
    fields = relationship("Field", back_populates="farmer")

class Field(Base):
    __tablename__ = 'Field'
    
    Field_ID = Column(BigInteger, primary_key=True)
    Farmer_ID = Column(BigInteger, ForeignKey('Farmer.Farmer_ID'), nullable=False)
    Longitude = Column(Float, nullable=False)
    Latitude = Column(Float, nullable=False)
    Soil_Type = Column(String, nullable=False)  # Adjust type as necessary
    Elevation = Column(BigInteger, nullable=False)

    # Relationships
    farmer = relationship("Farmer", back_populates="fields")
    field_data = relationship("FieldData", back_populates="field")
    probes = relationship("Probe", back_populates="field")

class FieldData(Base):
    __tablename__ = 'FieldData'
    
    FDID = Column(BigInteger, primary_key=True)
    Field_ID = Column(BigInteger, ForeignKey('Field.Field_ID'), nullable=False)
    Water_ID = Column(BigInteger, ForeignKey('Water.Water_ID'), nullable=False)
    Irrigation_Status = Column(Boolean, nullable=False)
    Avg_Yield = Column(Float, nullable=False)
    Crop_ID = Column(BigInteger, ForeignKey('Crop.Crop_ID'), nullable=False)
    Tillage = Column(String(10), nullable=False)  # Adjust type as necessary
    Field_Residue = Column(Boolean, nullable=False)
    Planting_Style = Column(String(10), nullable=False)  # Adjust type as necessary
    Depth = Column(Float, nullable=False)
    Cover_Crop = Column(Boolean, nullable=False)
    Row_Spacing = Column(Float, nullable=False)
    Pivot_Corners = Column(String(10), nullable=False)  # Adjust type as necessary

    # Relationships
    field = relationship("Field", back_populates="field_data")
    crop = relationship("Crop", back_populates="field_data")
    water = relationship("Water", back_populates="field_data")

class Probe(Base):
    __tablename__ = 'Probe'
    
    Probe_ID = Column(BigInteger, primary_key=True)
    Field_ID = Column(BigInteger, ForeignKey('Field.Field_ID'), nullable=False)
    Salinity = Column(Float, nullable=False)
    Temperature = Column(Float, nullable=False)
    Moisture = Column(Float, nullable=False)
    Nitrogen = Column(Float, nullable=False)
    Phophorus = Column(Float, nullable=False)
    Potassium = Column(Float, nullable=False)
    Sunlight = Column(Float, nullable=False)
    pH = Column(Float, nullable=False)

    # Relationships
    field = relationship("Field", back_populates="probes")

class Water(Base):
    __tablename__ = 'Water'
    
    Water_ID = Column(BigInteger, primary_key=True)
    Avg_Annual_Rainfall = Column(Float, nullable=False)
    Irrigation_App = Column(Float, nullable=False)
    Runoff = Column(Float, nullable=False)
    Leaching = Column(Boolean, nullable=False)

    # Relationships
    field_data = relationship("FieldData", back_populates="water")
