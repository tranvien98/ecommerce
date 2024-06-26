from pydantic import Field, BaseModel

class SkuSchemaCreate(BaseModel):
    sku_name: str = Field(...)
    sku_tier_ids: list = Field(...)
    sku_price: float = Field(...)
    sku_quantity: int = Field(...)
    sku_default: bool = Field(default=False)
    class Config:
        extra = "allow"
