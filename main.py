from fastapi import FastAPI 

app = FastAPI(title="Simple Rest API")

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
