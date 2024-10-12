from fastapi import APIRouter, HTTPException
from app.crud import items as crud_items
from app.schemas.item import ItemCreate, ItemUpdate

router = APIRouter()

@router.post("/")
async def create_item(item: ItemCreate):
    item_id = await crud_items.create_item(item)
    return {"id": item_id}
    

@router.get("/{id}")
async def read_item(id: str):
    item = await crud_items.get_item_by_id(id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/{id}")
async def update_item(id: str, item: ItemUpdate):
    await crud_items.update_item(id, item.dict(exclude_unset=True))
    return {"message": "Item updated"}

@router.delete("/{id}")
async def delete_item(id: str):
    await crud_items.delete_item(id)
    return {"message": "Item deleted"}
