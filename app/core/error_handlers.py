from fastapi import Request # import request from fastapi
from fastapi.responses import JSONResponse # import JSONResponse from fastapi.responses

from app.core.exceptions import (
    BusinessException # import BusinessException from app.core.exceptions
)


# create business exception handler:
async def business_exception_handler(
    request: Request, # request
    exc: BusinessException # business exception
):

    # return JSON response:
    return JSONResponse(
        status_code=exc.status_code, # status code
        content={
            "detail": exc.message # message
        }
    )