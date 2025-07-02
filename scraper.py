import time
import os
from datetime import datetime
# from pymongo import MongoClient

def scrape_all():
    print("🚀 Starting dummy scraping...")
    # Dummy MongoDB URI (replace with your actual)
    # mongo_uri = "mongodb+srv://username:password@cluster.mongodb.net/"

    # client = MongoClient(mongo_uri)
    # db = client["superbike_db"]
    # collection = db["product_links"]

    store_name = "dummy_store"
    urls_to_scrape = [
        "https://dummy.com/product/1",
        "https://dummy.com/product/2",
        "https://dummy.com/product/3"
    ]

    scraped_links = []
    
    # Create debug file with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    debug_filename = f"{store_name}_{timestamp}_debug.txt"

    for url in urls_to_scrape:
        print(f"⏳ Scraping {url} (simulated, will take ~2 seconds)...")
        time.sleep(12)  # simulate scraping delay

        scraped_links.append(url)

        # Incremental update
        # collection.update_one(
        #     {"store_name": store_name},
        #     {"$addToSet": {"links": url}},
        #     upsert=True
        # )
        print(f"✅ Stored: {url}")
        
        # Save to debug file after each link is scraped
        with open(debug_filename, "a") as debug_file:
            debug_file.write(f"{url}\n")

    print("🎉 Dummy scraping finished!")
    
    # Save all links to a final results file
    results_filename = f"{store_name}_{timestamp}_results.txt"
    with open(results_filename, "w") as results_file:
        results_file.write(f"Scraping completed at: {timestamp}\n")
        results_file.write(f"Total links scraped: {len(scraped_links)}\n\n")
        for link in scraped_links:
            results_file.write(f"{link}\n")
    
    print(f"📄 Debug file saved: {debug_filename}")
    print(f"📄 Results file saved: {results_filename}")
