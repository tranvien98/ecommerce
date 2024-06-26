from slugify import slugify
from beanie import PydanticObjectId

from app.modules.skus.models import SkuSchema
from app.modules.skus.schemas import SkuSchemaCreate


async def create_sku(sku: SkuSchemaCreate ):
    """
    Create a new SKU in the database
    """
    sku.sku_slug = slugify(sku.sku_name)
    sku = SkuSchema(**sku.model_dump())
    await sku.insert()
    return sku


async def get_all_skus(product_id: str):
    """
    Get all SKUs from the database
    """
    skus = await SkuSchema.find(SkuSchema.is_deleted == False, SkuSchema.product_id == PydanticObjectId(product_id)).to_list()
    return skus
