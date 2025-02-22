from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Threshold to classify fraud
THRESHOLD = 4.0

# Request model
class Transaction(BaseModel):
    value: float

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust to specific origins if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setting up templates and static files
templates = Jinja2Templates(directory="templates")

# Optional: Serve static files (like CSS, JS, images) if needed
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("Index.html", {"request": request})

@app.get("/cridet", response_class=HTMLResponse)
async def cridet_page(request: Request):
    return templates.TemplateResponse("cridet.html", {"request": request})

@app.get("/form", response_class=HTMLResponse)
async def cridet_page(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})
@app.get("/about", response_class=HTMLResponse)
async def cridet_page(request: Request):
    return templates.TemplateResponse("Aboutus.html", {"request": request})
@app.get("/success", response_class=HTMLResponse)
async def cridet_page(request: Request):
    return templates.TemplateResponse("success.html", {"request": request})
@app.get("/security", response_class=HTMLResponse)
async def cridet_page(request: Request):
    return templates.TemplateResponse("security.html", {"request": request})

# Endpoint to check if the transaction is fraudulent
@app.post("/check-transaction/")
def check_transaction(transaction: Transaction):
    if transaction.value > THRESHOLD:
        return {"result": "The Account Id is detected as Not Safe"}
    return {"result": "The Account Id is detected as Safe"}
    