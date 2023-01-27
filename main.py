from fastapi import FastAPI
import json
from typing import Union
from sensors import json_creator

app = FastAPI()

@app.get("/")
def read_root():
    data = json.loads(json_creator())
    print(data, 'data desde main')
    return data


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
    

