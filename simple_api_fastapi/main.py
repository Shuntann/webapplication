from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

#run command -> uvicorn main:app --reload

class Hello(BaseModel):
    texts: str

app = FastAPI()

@app.get("/")
def root():
    return {"message":"hello"}

#パスパラメーター
@app.get("/countries/{country_name}")
async def country(country_name: str):
    return {"country_name":country_name}


@app.get("/countries/japan")
async def japan():
    return {"country_name":"this is japan"}


#クエリパラメーター
@app.get("/flags/")
def flags(flag_name: str = "japan", flag_no: int = 1):
    return {"flag_name": flag_name,
            "flag_no":flag_no,        
    }

#クエリパラメーターとパスパラメーター組合せ
@app.get("/colors/{color_name}")
def color(color_name:str="black", color_no:int=1):
    return{
        "color_name":color_name,
        "color_no":color_no,
    }


@app.get("/flowers/")
def flower(flower_name:Optional[str] = None, flower_no:Optional[int]=None):
    return{
        "flower_name":flower_name,
        "flower_no":flower_no,
    }


@app.post("/send_post_method/")
async def send_data(first: Optional[str] =None, No: Optional[int]=None):
    #print(first.texts)
    return {"username": first,
            "No":No        
    }