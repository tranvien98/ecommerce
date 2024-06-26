from pydantic import Field, BaseModel
from app.modules.skus.schemas import SkuSchemaCreate


class ProductSchemaCreate(BaseModel):
    product_name: str = Field(...)
    product_thumbnail: str = Field(...)
    product_description: str
    product_category: list[str]
    product_price: float = Field(...)
    product_quantity: int = Field(...)
    product_variations: list[dict] = []
    sku_list: list[SkuSchemaCreate] = []
    """
    các thuộc tính của sản phẩm
    [
        {
            "name: "size",
            "options": ["S", "M", "L"],
            "image": "https://example.com/image.jpg"
        },
        {
            "name": "color"
        }
    ]
    """


    class Config:
        extra = "allow"
