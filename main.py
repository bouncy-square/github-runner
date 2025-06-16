from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Environment Variables API",
    description="A simple API to display environment variables",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EnvVarsResponse(BaseModel):
    message: str
    environment_variables: Dict[str, str]

@app.get("/", response_model=EnvVarsResponse)
async def get_environment_vars():
    try:
        env_vars = dict(os.environ)
        
        return {
            "message": "Environment variables retrieved successfully",
            "environment_variables": env_vars
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)