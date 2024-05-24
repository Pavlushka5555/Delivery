import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from api import user_router, dishes_router, orders_router
from fastapi.responses import HTMLResponse


app = FastAPI(
    title="API для доставки еды",
    version="0.0.1"
)

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(dishes_router, prefix="/dishes", tags=["dishes"])
app.include_router(orders_router, prefix="/orders", tags=["orders"])

app.mount("/static", StaticFiles(directory="app/site/static"), name="static")

templates = Jinja2Templates(directory="app/site/templates")

@app.get("/", response_class=HTMLResponse, tags=["Root"])
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
