from pydantic import BaseModel
from typing import Any, Optional

class SuccessResponse(BaseModel):
    success: bool = True
    message: Optional[str] = "Operation successful"
    data: Optional[Any] = None

class ErrorResponse(BaseModel):
    success: bool = False
    error: str
    details: Optional[Any] = None
