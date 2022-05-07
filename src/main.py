#print("Hello AWS World!")


import logging
from logging.config import dictConfig
from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel
#from reddit_and_huggingface_student import reddit, GetListOfComments, GetPredict, GetSinglePredict
from src.RedditObj import RedditandHugging
from src.logdoconfig import logger

class PredictionRequest(BaseModel):
      query_string: str
 
app = FastAPI()


@app.get("/health")
async def gethealth():
    logging.info("this is test to work with logging")
    return {"test for the first get API using fastAPI"}

@app.post("/getsinglepredict")
async def getpredict(request: PredictionRequest):
    prd = RedditandHugging()
    logger.info("this is test to work with single predict")
    predictvar = prd.GetSinglePredict(request.query_string)
    return predictvar
