import time
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

    print("🎉 Dummy scraping finished!")
