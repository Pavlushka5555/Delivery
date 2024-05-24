from .user_controller import router as user_router
from .dish_controller import router as dishes_router
from .orders_controller import router as orders_router

__all__ = ["user_router", "dishes_router", "orders_router"]