from fastapi import FastAPI

app = FastAPI(title="Poker Trainer API")


@app.get("/")
def read_root():
    return {"message": "Poker Trainer API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}