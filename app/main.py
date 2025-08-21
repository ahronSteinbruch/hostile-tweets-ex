import uvicorn
from fastapi import FastAPI, HTTPException
from manager import AnalysisManager
import os

app = FastAPI(
    title="Hostile Tweets Analyzer API",
    description="API for fetching and processing tweets from a MongoDB database.",
    version="1.0.0"
)

# create an instance of AnalysisManager
manager = AnalysisManager()
manager.run_full_analysis()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Hostile Tweets Analyzer API. Go to /processed-data to get the data."}


@app.get("/processed-data")
def get_data():
    """
    Endpoint that returns the processed data in JSON format.
    """
    try:
        data = manager.get_processed_data()
        if not data:
            print("no data to return")
            return 204
        return data
    except Exception as e:
        # handle the exception thet accured and return a 500 error
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8001)