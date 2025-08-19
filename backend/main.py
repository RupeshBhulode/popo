from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routes import router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os
app = FastAPI()

# CORS so frontend can talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(router)

## Serve frontend folder as static files
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# Serve login.html at root
@app.get("/")
def root():
    return FileResponse(os.path.join("frontend", "login.html"))