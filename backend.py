from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Threshold to classify fraud
THRESHOLD = 1.0

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

# Endpoint to check if the transaction is fraudulent
@app.post("/check-transaction/")
def check_transaction(transaction: Transaction):
    if transaction.value > THRESHOLD:
        return {"result": "The Account Id is detected as Not Safe"}
    return {"result": "The Account Id is detected as Safe"}
