from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from platform_base.logging_factory import get_logger
from platform_base.error_handler import register_error_handlers

def create_base_app(app_name: str = "Platform Service", enable_cors: bool = True) -> FastAPI:
    get_logger()

    app = FastAPI(
        title=app_name,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json"
    )

    if enable_cors:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    register_error_handlers(app)

    return app
