

# from app.modules.spus.schemas import ProductSchemaCreate
# from app.modules.skus.schemas import SkuSchemaCreate


# async def validate_create_product(product: ProductSchemaCreate):
#     """
#     Create a new product in the database
#     """
#     if await ProductSchema.find_one(ProductSchema.product_name == product.product_name, ProductSchema.is_deleted == False):
#         raise ProductAlreadyExists
