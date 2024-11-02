from fastapi import FastAPI
from app.router import farmer,field
from app.database import Base, engine
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
import os



Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allow cross-origin requests (optional, based on your needs)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# Serve static files
app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), 'static')), name="static")
app.include_router(farmer.router)
app.include_router(field.router)



static = StaticFiles(directory="templates")


templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse("Index.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/products", response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse("products.html", {"request": request})

@app.get("/contact", response_class=HTMLResponse)
async def login_page(request: Request):
    # Render a login page (you need to create the login.html in templates folder)
    return templates.TemplateResponse("contact.html", {"request": request})

@app.get("/about", response_class=HTMLResponse)
async def login_page(request: Request):
    # Render a login page (you need to create the login.html in templates folder)
    return templates.TemplateResponse("about.html", {"request": request})