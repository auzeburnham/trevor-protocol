from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import json
import csv
import re
import requests

# === CONFIG ===
CHROMEDRIVER_PATH = "/Users/asab/Tools/chromedriver"
main_url = "https://paulhopkins.co.uk/Elections/General-Elections-2024"

# === STEP 1: Get all Reform UK candidate links ===
response = requests.get(main_url)
soup = BeautifulSoup(response.text, "html.parser")

links = []
for a_tag in soup.find_all("a", href=True):
    href = a_tag['href']
    if "ReformUK" in href:
        full_url = href if href.startswith("http") else requests.compat.urljoin(main_url, href)
        links.append(full_url)

# === STEP 2: Set up Selenium ===
service = Service(CHROMEDRIVER_PATH)
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=service, options=options)

# === STEP 3: Extract real biography content ===
def extract_biography(soup):
    raw_text = soup.body.get_text(separator="\n", strip=True)
    chunks = re.split(r"\n{2,}|\n", raw_text)
    paragraphs = []

    for chunk in chunks:
        text = chunk.strip()
        if (
            len(text.split()) >= 30 and
            "amazon" not in text.lower() and
            not re.search(r"\b(@|http|\.com|\.uk)\b", text.lower())
        ):
            paragraphs.append(text)

    return " ".join(paragraphs)

# === STEP 4: Scrape bios ===
bios = []

for link in links:
    try:
        print(f"Visiting: {link}")
        browser.get(link)

        WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        time.sleep(2)

        soup = BeautifulSoup(browser.page_source, "html.parser")
        bio_text = extract_biography(soup)

        if bio_text:
            bios.append({
                "url": link,
                "biography": bio_text
            })
        else:
            print(f"⚠️ No valid biography found at: {link}")

    except Exception as e:
        print(f"❌ Error at {link}: {e}")

browser.quit()

# === STEP 5a: Save JSON ===
with open("reform_uk_biographies_ground_truth.json", "w", encoding="utf-8") as f:
    json.dump(bios, f, indent=2)

# === STEP 5b: Save CSV ===
with open("reform_uk_biographies_ground_truth.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["url", "biography"])
    writer.writeheader()
    writer.writerows(bios)

print(f"\n✅ Trevor Protocol v11 complete! Saved {len(bios)} full biographies.")

