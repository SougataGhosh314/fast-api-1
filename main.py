from fastapi import FastAPI

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