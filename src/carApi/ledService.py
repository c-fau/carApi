from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Value(BaseModel):
    value: bool

# A global variable to store the boolean value
current_value = {"value": False}

@app.post("/set")
async def set_value(value: Value):


    global current_value
    current_value["value"] = value.value
    return {"success": True, "value": current_value["value"]}

@app.get("/get")
async def get_value():
    return {"value": current_value["value"]}

@app.get("/10X/{value}")
async def process_value(value: int):
    result = value * 10
    return {"value": result}

