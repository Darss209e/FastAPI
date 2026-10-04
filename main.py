# from fastapi import FastAPI

# from pydantic import BaseModel

# app = FastAPI()

# # @app.get("/")
# # def home():
# #     return {"message":"Welcome to fatsapi"}

# # @app.get("/about")
# # def about():
# #     return {"message":"this is about page"}

# # # @app.get("/users")
# # # def users():
# # #     return {
# # #         "users": ["mohit","rohit"]

# #     # }
# # # @app.get("/users/{user_id}")
# # # def get_user(user_id:int):
# # #     return {"user_id": user_id}

# # # @app.get("/users")
# # # def get_users(name):
# # #     return {"Name": name}

# # @app.get("/products")
# # def get_users(limit: int=10):
# #     return {"limit": limit}

# # @app.get("/items")
# # def get_users(name: str = None , price: int=0):
# #     return {
# #         "name": name,
# #         "price": price
# #     }

# class User(BaseModel):
#     name: str
#     age: int


# @app.post("/create-user")
# def create_user(user:User):
#     return{
#        "message": "User created",
#        "data":user
#     }