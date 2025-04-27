from fastapi import FastAPI
from fastapi.responses import JSONResponse

def add_health_route(app: FastAPI, path: str = "/health") -> None:
    @app.get(path)
    async def health_check():
        return JSONResponse(content={"status": "ok"})
