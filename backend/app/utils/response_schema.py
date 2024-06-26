# from typing import Any, Optional
# from pydantic import BaseSchema
# from fastapi.responses import Response, BackgroundTasks

# # utils/schemas.py

# class JSONResponse(Response):
#     media_type = "application/json"

#     def __init__(
#         self,
#         content: typing.Any = None,
#         status_code: int = 200,
#         headers: t.Optional[t.Mapping[str, str]] = None,
#         media_type: t.Optional[str] = None,
#         background: t.Optional[BackgroundTasks] = None,
#     ) -> None:
#         self.status_code = status_code
#         if media_type is not None:
#             self.media_type = media_type
#         self.background = background
#         self.body = self.render(content)
#         self.init_headers(headers)

#     def render(self, content: BaseSchema | list[BaseSchema] | Any):
#        # This is not 100% battle proof, but as our services are controlled (only return Pydantic modules) works fine
#         if isinstance(content, BaseSchema):
#             return content.json().encode("utf-8")
#         if isinstance(content, list):
#             if isinstance(content[0], BaseSchema):
#                 def uuid_decoder(obj):
#                     if isinstance(obj, UUID):
#                         return str(obj)
#                 return orjson.dumps([item.dict() for item in content], default=uuid_decoder)

