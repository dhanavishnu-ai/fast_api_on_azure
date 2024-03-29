import uvicorn
from fastapi import FastAPI

# initialize FastAPI
app = FastAPI()

@app.get("/")
def index():
    return {"data": "Application ran successfully - FastAPI"}
  
  
if __name__ == "__main__":
    uvicorn.run(app, port=8000)