import praw
from transformers import pipeline
import pandas as pd
lstColumnNames = ['Message','Result']
lstColumnNamess = ['label','score']
from praw.models import MoreComments
from pydantic import BaseModel
#import secrets

class RedditOrgName(BaseModel):
    orgName:str
    orgName= 'TSLA'
      
reddit = praw.Reddit(
   client_id = "uimg80Wx_K40GVG-VbGMGQ",
   client_secret = "KvZ3CdQt0RrxQwPK2NXAR7brqjnRFA",
   user_agent ="shikur_bat"
   
)

class RedditandHugging:
    orgname = 'TSLA'
    subreddit = reddit.subreddit(orgname)
           
       
    def GetListOfComments(orgname):
        top_comments = []
        comment_counts = 0
    
        for submission in subreddit.top(limit=10):
            for top_level_comment in submission.comments:
                if isinstance(top_level_comment, MoreComments):
                # if top_level_comment is commentforest then back to next top_level_comment instance in nested for loop
                        continue
            # if top_level_comment an instance of comment model add to list object        
            top_comments.append(top_level_comment.body)
            comment_counts+=1
        return top_comments;    
       
    
    def GetPredict(top_comments):
        datalist = []
        df = pd.DataFrame(lstColumnNames)
        sentiment_model = pipeline("sentiment-analysis")
        for msgcomment in top_comments:
            sentiment = sentiment_model(msgcomment)
            datalist.append([ msgcomment,sentiment])
            df = pd.DataFrame(datalist, columns=lstColumnNames)
            
        return df;  
     
    @staticmethod
    def GetSinglePredict(comment):
       
        print(comment)
        sentiment_model = pipeline("sentiment-analysis")
        sentiment = sentiment_model(comment)
                
        return sentiment;   

    