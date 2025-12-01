from typing import List, Dict, Any, Literal
from pathlib import Path
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from home.main import generate_loadouts_endpoint

# ------------------------------------------------------------
# FastAPI app
# ------------------------------------------------------------
app = FastAPI(title="Helldivers Loadout API")

# CORS – needed only for browsers, not native iOS.
ALLOWED_ORIGINS = [
    "http://localhost",
    "http://127.0.0.1",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------------------------------------
# Static files (images)
# ------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[1]
STATIC_DIR = PROJECT_ROOT / "static"
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# ------------------------------------------------------------
# Pydantic models (request/response)
# ------------------------------------------------------------
class LoadoutRequest(BaseModel):
    players: int = Field(ge=1, le=4)
    warbonds: List[str] = []
    style: Literal["default", "spec_ops", "explosive"] = "default"


class PlayerLoadout(BaseModel):
    player: int
    loadout: Dict[str, Any]


class LoadoutResponse(BaseModel):
    players: List[PlayerLoadout]


# ------------------------------------------------------------
# Endpoint
# ------------------------------------------------------------
@app.post("/loadouts", response_model=LoadoutResponse)
def create_loadouts(payload: LoadoutRequest):
    """
    POST /\n
    TEST CASE EXAMPLE:\n
    loadouts
    {\n
      "players": 4,\n
      "warbonds": ["ODST", "STEELED_VETERANS"],\n
      "style": "spec_ops"\n
    }\n
    DLC's:\n
    "base", "Steeled Veterans", "Helldivers Mobilize", "Helldivers x Killzone Crossover"\n
    "Viper Commandos", "Polar Patriots", "Democratic Detonation", "Force of Law", "Masters of Ceremony" \n
    "Freedom's Flame", "Obedient Democracy Support Troopers", "Dust Devils", "Control Group", "Borderline Justice"\n
    "Servants of Freedom", "Truth Enforcers", "Urban Legends", "Cutting Edge", "Super Store", "Super Citizen Edition" \n
    "Servants of Freedom", "Chemical Agents"\n

    Playlists:\n
    "spec_ops", "default", "explosive"
    """
    result_dict = generate_loadouts_endpoint(payload.model_dump())
    return result_dict
