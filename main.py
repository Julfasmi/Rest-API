from fastapi import FastAPI
import uvicorn
import os

app = FastAPI(title="Test Rest API")

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {
        "item_id": item_id,
        "title": "Item title"
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
