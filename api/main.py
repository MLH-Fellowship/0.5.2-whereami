from whereamigeo.helper import olc_to_phrase, phrase_to_olc
from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"status": "up"}


@app.get("/lookup_olc")
def lookup_olc(response: Response, olc: str = None):
    # the '+' gets replaced with ' ' for some reason, we need to add it back
    olc = olc.replace(' ', '+')
    try:
        return {"status": 200,
                "phrase": olc_to_phrase(olc, False),
                "olc": olc}
    except KeyError:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"status": 400, "message": "Invalid OLC code."}


@app.get("/lookup_phrase")
def lookup_phrase(response: Response, phrase: str = None):
    try:
        return {"status": 200, "phrase": phrase, "olc": phrase_to_olc(phrase)}
    except KeyError:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"status": 400, "message": "Invalid phrase."}
