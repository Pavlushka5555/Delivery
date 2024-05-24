from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime

class OrderCreate(BaseModel):
    user_id: str
    dish_ids: List[str]
    total_price: float
    order_status: str

class OrderUpdate(BaseModel):
    user_id: Optional[str] = None
    dish_ids: Optional[List[str]] = None
    total_price: Optional[float] = None
    order_status: Optional[str] = None

class OrderResponse(BaseModel):
    id: str
    user_id: str
    dish_ids: List[str]
    total_price: float
    order_status: str
    order_time: datetime

