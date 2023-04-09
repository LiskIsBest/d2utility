import os

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

load_dotenv()

app = FastAPI()
app.add_middleware(CORSMiddleware, expose_headers=["X-Forwarded-Proto"])

app.mount(
    "/static", StaticFiles(directory=os.path.abspath("webapp/static")), name="static"
)

templates = Jinja2Templates(directory=os.path.abspath("webapp/templates"))

d2utility_sites = [
    {
        "name": "DIM",
        "url": "https://app.destinyitemmanager.com/",
        "description": "Destiny Item Manager (DIM) is a free online tool for players of Destiny 2, providing a convenient way to manage inventory across characters and vaults. It offers search and filter options, customizable loadouts, item tagging, and an item optimizer feature to improve gameplay efficiency.",
        "ios_url": "https://apps.apple.com/app/1600203128",
        "android_url":"https://play.google.com/store/apps/details?id=com.destinyitemmanager.app"
    },
    {
        "name": "D2ArmorPicker",
        "url": "https://d2armorpicker.com/#/",
        "description": "D2ArmorPicker is a free online tool designed to help players of Destiny 2 select and optimize their armor loadouts. The website provides an intuitive interface where players can select their preferred stat distributions, such as mobility, resilience, and recovery, and then view recommended armor pieces that match their chosen criteria.",
    },
    {
        "name": "D2Checkpoint",
        "url": "https://d2checkpoint.com/#",
        "description": "D2checkpoint is a website that provides a simple and efficient way for players of Destiny 2 to obtain checkpoints for various raids, dungeons, and other endgame activities.",
    },
    {
        "name": "TodayInDestiny",
        "url": "https://todayindestiny.com/",
        "description": "TodayInDestiny is a website that provides up-to-date information on the daily and weekly activities, events, and challenges in Destiny 2.",
    },
    {
        "name": "D2lfg",
        "url": "https://d2lfg.com/user/",
        "description": "Destiny 2 LFG Discord is a community platform where players can find teammates for a range of in-game activities, including Raids, Strikes, Gambit matches, Crucible matches, Dungeons, Trials of Osiris, Iron Banner, and other game modes.",
        "discord_url": "https://discord.com/invite/d2lfg",
    },
]


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "sites": d2utility_sites}
    )
