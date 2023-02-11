from fastapi import FastAPI

app = FastAPI()


@app.get("/healthcheck")
def healthcheck():  # type: ignore # Simple view used as uptests in deployments.
    return {}
