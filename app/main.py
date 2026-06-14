from fastapi import FastAPI # import FastAPI from fastapi

import app.models # import models from app.models

from app.api.auth import router as auth_router # import auth router
from app.api.rooms import router as rooms_router # import rooms router
from app.api.bookings import router as bookings_router # import bookings router
from app.api.admin import router as admin_router # import admin router

# create FastAPI app:
app = FastAPI(
    title="Coworking Booking Service"
)

# import BusinessException from app.core.exceptions:
from app.core.exceptions import (
    BusinessException
)

# import business_exception_handler from app.core.error_handlers:
from app.core.error_handlers import (
    business_exception_handler
)

# add exception handler:
app.add_exception_handler(
    BusinessException,
    business_exception_handler
)

app.include_router(auth_router) # include auth router
app.include_router(rooms_router) # include rooms router
app.include_router(bookings_router) # include bookings router
app.include_router(admin_router) # include admin router