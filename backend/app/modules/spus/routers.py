from fastapi import APIRouter, Depends
from app.modules.spus import schemas, services
from app.auth.dependences import get_current_user
from app.users.models import Users


router = APIRouter(prefix="/spus", tags=["spus"])

@router.post("/create-product")
async def create_product(product: schemas.ProductSchemaCreate, user:Users = Depends(get_current_user)):
    product.product_shop = user.id
    product = await services.create_product(product)
    return {
        "status_code": 201,
        "message": "Product created successfully",
        "metadata": product
    }


@router.get("/{product_id}")
async def get_one_product(product_id: str):
    product = await services.get_one_product(product_id)
    return {
        "status_code": 200,
        "message": "Product retrieved successfully",
        "metadata": product
    }
