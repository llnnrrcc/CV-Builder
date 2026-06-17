from fastapi import FastAPI

app = FastAPI(title="CV App API")


@app.get("/health")
def health_check():
    return {"status": "ok"}