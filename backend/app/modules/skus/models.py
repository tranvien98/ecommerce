from typing import Literal
from beanie import Document, PydanticObjectId
from pydantic import Field
from datetime import datetime

class SkuSchema(Document):
	sku_name: str = Field(...)
	sku_tier_ids: list # pich theo thứ tự options
	sku_slug: str
	sku_price: float = Field(...)
	sku_default: bool = False
	sku_quantity: int = Field(...)
	product_id: PydanticObjectId = Field(...)
	is_deleted: bool = False
	updated_at: datetime = Field(default_factory=datetime.now)
	created_at: datetime = Field(default_factory=datetime.now)

