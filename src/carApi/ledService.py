from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your Angular app URL
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class Value(BaseModel):
    value: bool
    
class LEDState(BaseModel):
    state: bool

# A global variable to store the boolean value
current_value = {"value": False}
current_led_state = {"state": False}


@app.post("/up/set")
async def set_value(state: LEDState):
    global current_value
    current_led_state["state"] = state.state
    return {"success": True, "State": current_led_state["state"]}

@app.post("/down/set")
async def set_value(state: LEDState):
    global current_value
    current_led_state["state"] = state.state
    return {"success": True, "State": current_led_state["state"]}

@app.post("/left/set")
async def set_value(state: LEDState):
    global current_value
    current_led_state["state"] = state.state
    return {"success": True, "State": current_led_state["state"]}

@app.post("/right/set")
async def set_value(state: LEDState):
    global current_value
    current_led_state["state"] = state.state
    return {"success": True, "State": current_led_state["state"]}

@app.get("/get")
async def get_value():
    return {"value": current_value["value"]}

@app.get("/10X/{value}")
async def process_value(value: int):
    result = value * 10
    return {"value": result}

