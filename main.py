from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn
import os

app = FastAPI(title="Test Rest API")

# Contoh model data
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

# Simulasi penyimpanan data di memori
fake_db = {}

# GET: Ambil item berdasarkan ID
@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = fake_db.get(item_id)
    if item:
        return {"item_id": item_id, "data": item}
    return {"error": "Item not found"}

# POST
@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in fake_db:
        return {"error": "Item already exists"}
    fake_db[item_id] = item.dict()
    return {"message": "Item created", "item": fake_db[item_id]}

# PUT: Ganti seluruh isi item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    fake_db[item_id] = item.dict()
    return {"message": "Item replaced", "item": fake_db[item_id]}

# PATCH: Ubah sebagian isi item
@app.patch("/items/{item_id}")
def partial_update_item(item_id: int, item: Item):
    stored_item = fake_db.get(item_id)
    if not stored_item:
        return {"error": "Item not found"}
    
    updated_item = stored_item.copy()
    update_data = item.dict(exclude_unset=True)
    updated_item.update(update_data)
    fake_db[item_id] = updated_item
    return {"message": "Item updated", "item": updated_item}

# DELETE
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in fake_db:
        del fake_db[item_id]
        return {"message": f"Item {item_id} deleted"}
    return {"error": "Item not found"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
