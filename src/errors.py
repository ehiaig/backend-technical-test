from fastapi.responses import JSONResponse

def custom_error(code, message):
    return JSONResponse(status_code=code,content=message)