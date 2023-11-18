from fastapi import FastAPI
from enum import Enum

app = FastAPI()


@app.get("/", description="This is a GET route")
async def get_route():
    return {"message": "Hello World!"}


@app.post("/")
async def post_route():
    return {"message": "you just hit a post request"}


@app.put("/", deprecated=True)
async def put_route():
    return {"message": "you just hit a put request"}


@app.delete("/")
async def delete_route():
    return {"message": "you just hit a delete request"}


class DayEnum(str, Enum):
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    SUNDAY = "Sunday"


@app.get("/days/{day_name}")
async def get_day(day_name: DayEnum):
    if day_name == DayEnum.TUESDAY:
        return {
            "day_name": day_name.name,
            "day_value": day_name.value
        }

    if day_name.value == "Monday":
        return {
            "day_name": day_name,
            "message": "you are on Monday",
        }
    return {"day_name": day_name, "message": "this is a different day"}
