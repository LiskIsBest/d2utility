import os
import json
from random import randint

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, parse_obj_as

load_dotenv()


class Site(BaseModel):
    name: str
    url: str
    ios_url: str | None
    android_url: str | None
    discord_url: str | None
    description: str


class Bot(BaseModel):
    name: str
    url: str | None
    invite_link: str
    description: str


app = FastAPI()

app.mount(
    "/static", StaticFiles(directory=os.path.abspath("webapp/static")), name="static"
)

templates = Jinja2Templates(directory=os.path.abspath("webapp/templates"))


def parse_sites() -> list[Site]:
    sites = []
    f = open("data/sites.json", "r")
    data = json.load(f)
    for site in data:
        sites.append(parse_obj_as(type_=Site, obj=site))
    return sites


def parse_bots() -> list[Bot]:
    bots = []
    f = open("data/bots.json", "r")
    data = json.load(f)
    for site in data:
        bots.append(parse_obj_as(type_=Bot, obj=site))
    return bots


d2utility_sites = parse_sites()
d2utility_bots = parse_bots()


def rand_bg_image() -> str:
    return f"d2Background{randint(1,7)}.png"


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "base.html",
        {
            "request": request,
            "sites": d2utility_sites,
            "bots": d2utility_bots,
            "filename": rand_bg_image(),
        },
    )
