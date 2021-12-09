from enum import Enum
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

# app = FastAPI() # FastAPI클래스의 인스턴스

# 1
# @app.get("/items/{item_id}")
# async def root(item_id: int): #:라는 어노테이션(주석)을 통해 경로매개변수의 타입을 선언 할 수 있음
#     return {"item_id": item_id}


# 2
# 경로 동작은 순차적으로 평가되기 때문에 /users/{user_id} 이전에 /users/me를 먼저 선언
# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}
#
# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}

#3
# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"
#
#
# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName): # :어노테이션을 이용해 ModelName사용하는 어노테이션으로 경로매개변수 만듬
#     if model_name == ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}
#
#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}
#
#     return {"model_name": model_name, "message": "Have some residuals"}

# 4
# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
#
#
# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]


# 5
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Optional[str] = None, short: bool = False): #optional없으면 필수 파라미터로 인식, =None로 기본 default값
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item

# 6
# @app.get("/items/{item_id}")
# async def read_user_item(
#     item_id: str, needy: str, skip: int = 0, limit: Optional[int] = None
# ):
#     item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
#     return item

# 7
# class Item(BaseModel): #model 만듬
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#
#
# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax}) # 사전에 정의되지 않은 객체 변수를 추가할 수 있다.
#     return item_dict
#
#
# # body , path 및 쿼리 매개변수를 동시에 선언할 수도 있음
# @app.put("/items/{item_id}")
# async def create_item(item_id: int, item: Item, q: Optional[str] = None):
#     result = {"item_id": item_id, **item.dict()}
#     if q:
#         result.update({"q": q})
#     return result