#print("Hello AWS World!")
from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
async def gethealth():
    return {"test for the first get API using fastAPI"}
