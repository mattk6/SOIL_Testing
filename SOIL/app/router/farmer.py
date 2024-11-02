from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.database import get_db
from starlette.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app import schemas
import os


router = APIRouter(
    prefix="/farmer",
    tags=["farmer"]
)

from app.models import Farmer
from app.database import get_db


templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), 'templates'))

@router.get("/", response_class=HTMLResponse)
async def get_farmer(request: Request, db: Session = Depends(get_db)):
    farmer = db.query(Farmer).all()
    return templates.TemplateResponse("farmer.html", {"request": request, "farmer":farmer})
