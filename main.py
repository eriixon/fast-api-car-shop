from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from db.mongo import MongoDatabase

app = FastAPI()
mongo = MongoDatabase()


@app.get("/", response_class=HTMLResponse)
async def get_main_page():
    return """
    <html>
        <head>
            <title>Awesome Car Shop</title>
        </head>
        <body>
            <h1>Find a car of your dreams </h1>
        </body>
    </html>
    """


@app.get("/cars/{model}")
async def get_car_by_model(model):
    return mongo.get_car_by_model(model)
