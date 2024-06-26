from beanie import Document
from pydantic import Field
from typing import Literal
from datetime import datetime
from beanie import PydanticObjectId

class ProductSchema(Document):
	product_name: str = Field(...)
	product_thumbnail: str = Field(...)
	product_description: str
	product_slug: str
	product_category: list[str]
	product_shop: PydanticObjectId
	product_price: float = Field(...)
	product_variations: list[dict] = []
	product_quantity: int = Field(...)
	"""
	các thuọc tính của sản phẩm
	[
        {
            "name: "size",
            "options": ["S", "M", "L"],
            "image": "https://example.com/image.jpg"
        }
    ]
	"""
	product_rating: float = Field(default=0, ge=0, le=5)
	product_status: Literal['draft', 'public'] = Field(default='draft')
	is_deleted: bool = False
	created_at: datetime = Field(default_factory=datetime.now)
	updated_at: datetime = Field(default_factory=datetime.now)

