from fastapi import FastAPI, Query
from typing import List
from services.routers import route_query

app = FastAPI()

@app.get("/search")
def search_items(query: str = Query(...)):
    results = route_query(query)
    return {"results":results}