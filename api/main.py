from whereamigeo.helper import olc_to_phrase, phrase_to_olc
from fastapi import FastAPI, Response, status

app = FastAPI()


@app.get("/")
def read_root():
    return {"status": "up"}


@app.get("/lookup_olc")
def lookup_olc(response: Response, olc: str = None):
    # the '+' gets replaced with ' ' for some reason, we need to add it back
    olc = olc.replace(' ', '+')
    try:
        return {"status": 200, "phrase": olc_to_phrase(olc, False)}
    except KeyError:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"status": 400, "message": "Invalid OLC code."}


@app.get("/lookup_phrase")
def lookup_phrase(response: Response, phrase: str = None):
    try:
        return {"status": 200, "olc": phrase_to_olc(phrase)}
    except KeyError:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"status": 400, "message": "Invalid phrase."}
