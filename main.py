from fastapi import FastAPI
import threading
from scraper import scrape_all

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Superbikes scraper API!"}

@app.get("/trigger-scrape")
def trigger_scrape():
    thread = threading.Thread(target=scrape_all)
    thread.start()
    return {"status": "Scraping started in background"}
