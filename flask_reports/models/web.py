from pydantic import BaseModel
from typing import TypeVar, Optional, Generic

T = TypeVar('T')

class Response(BaseModel, Generic[T]):
    # success: bool
    data: Optional[T] = None