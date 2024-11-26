#Path Parameter and Query Parameter

# from fastapi import FastAPI,HTTPException
# from typing import List

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "Hello World"}

# #Path Parameter
# @app.get("/path/{name}",tags=["path_parameter"])
# async def get_user(name:str):
#     return {"name":name}

# @app.get("/path/{age}/{name}",tags=["multiple_path_parameter"])
# async def read_multiple_parameter(age:int, name:str):
#     return {"message":f"my name is {name} and age is {age}"}

# #Query Parameter
# @app.get('/query_parameter',tags=["Query Parameter"])
# async def  read_query(name : str = None, limit : int =10):
#     return {"message": [name,limit]}
#http://127.0.0.1:8000/query_parameter?name=Harshal&limit=10


# @app.get('/query_parameter_list', tags=["QueryParameterList"])
# async def query_parameter(fruits: List[str] = []):
#     return {"fruits": fruits}



#Pydantic Tutorial
# from pydantic import BaseModel,field_validator

# class Item(BaseModel):
#     name : str
#     age  : int
#     addr : str
#     price : float = 0.0

#     @field_validator('age')
#     def check_age(cls,value):

#         if value <= 0:
#          raise ValueError("Age should be greater than 0")
#         return value
# @app.post('/get_items',tags=["pydantic_model"])
# async def getItems(item:Item):
#     return {"name":item.name,"age":item.age,"addr":item.addr,"price":item.price}

# @app.post('/calc',tags=["query_paramter_pydantic"])
# async def calculate(item:Item,discount : float = 10):
#     final_price = item.price - discount
#     if final_price == 0:
#         raise HTTPException(status_code=404,detail="Price not found")
#     else:
#       return{"message": f"total price is {final_price}"}
    

# @app.get('/items/{items_id}',response_model=Item,tags=['custom_response_model'])
# def custom_response(items_id :int):
#  return {"name":"name" }





#Form Request In Python
from fastapi import FastAPI, Form, Request,UploadFile,File
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

# Define the template directory correctly
templates = Jinja2Templates(directory="application/templates")
print(templates)

# Route to render the form
@app.get('/', response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

# # Route to handle form submission
# @app.post('/submit')
# async def submit_form(username: str = Form(...), password: str = Form(...), file:UploadFile = File(...)):
#     return {"message": f"Welcome {username}! Your password {password} has been secured","filename": file.filename,
#         "content_type": file.content_type}

#Pass all data in one dictonary
@app.post('/submit')
async def submit_form(request:Request,file: UploadFile = File(...)):
    form_data = await request.form() # Access all form data as a dictionary
    return {
        "form_data" : form_data,
        "filename" : file.filename,
        "content_type": file.content_type
    

    }
