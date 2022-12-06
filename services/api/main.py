import pendulum
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="MiiCare Test API")

@app.get("/", response_class = HTMLResponse)
async def home_page():
    return HTMLResponse(content = "This API is for testing", status_code = 200)

@app.get("/get/function", response_class = HTMLResponse)
async def test_function():
    return HTMLResponse(content= "MiiCare Test API: Get Function called at: %s"%pendulum.now().to_datetime_string(), status_code = 200)