from fastapi import FastAPI
import difflib
import json

app = FastAPI()

with open("data.json") as json_data:
    data = json.load(json_data)
keys = [a for a in data.keys()]
values = [value for key, value in data.items()]


@app.get("/")
def read_root():
    return 200


@app.get("/def/{word}")
def define_word(word):
    matches = difflib.get_close_matches(word, keys)
    match_list = [{match: data[match]} for match in matches]
    return {"Matches": match_list}


@app.get("/search/{word}")
def search_word(word):
    matches = difflib.get_close_matches(word, values)
    match_list = [{word: match} for match in matches]
    return {"Closest definitions": match_list}
