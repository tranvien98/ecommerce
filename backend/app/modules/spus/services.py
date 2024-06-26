
import pydash
from beanie import PydanticObjectId
from slugify import slugify
from app.modules.spus.models import ProductSchema
from app.modules.skus.services import create_sku, get_all_skus
from app.modules.spus.schemas import ProductSchemaCreate


async def create_product(product: ProductSchemaCreate):
    """
    Create a new product in the database
    """
    product.product_slug = slugify(product.product_name)
    product_schema = ProductSchema(**product.model_dump(exclude={"sku_list"}))
    await product_schema.insert()

    for sku in product.sku_list:
        sku.product_id = product_schema.id
        await create_sku(sku)


async def get_one_product(product_id: str):
    """
    Get all products from the database
    """
    product = await ProductSchema.find_one(ProductSchema.id == PydanticObjectId(product_id), ProductSchema.is_deleted == False)
    if product:
        sku_list = await get_all_skus(product.id)
        sku_list = [pydash.omit(sku.model_dump(), ["product_id", "updated_at", "created_at", "is_deleted"]) for sku in sku_list]
    return {
        "product": product,
        "sku_list": sku_list
    }
