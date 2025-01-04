from fastapi import FastAPI
from api import weather
from api.db.connect import db_engine, Base

app = FastAPI()
app.include_router(weather.router)


#on startup create db models
Base.metadata.create_all(bind=db_engine)


@app.get("/")
def read_root():
    return {"status": "ok"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)