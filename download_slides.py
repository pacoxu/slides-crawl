import os
import requests
from bs4 import BeautifulSoup
import re
import concurrent.futures
from urllib.parse import unquote

# Function to download a file with a timeout
def download_file(url, file_path, timeout=30):
    try:
        print(f"Started to download: {file_path}")
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            with open(file_path, "wb") as file:
                file.write(response.content)
            print(f"Downloaded: {file_path}")
        else:
            print(f"Failed to download: {file_path}")
    except Exception as e:
        print(f"Download failed for {file_path}: {e}")


# Step 1: Find all topic links on the main page
topics_url = "https://kccncna2023.sched.com/list/descriptions/"
response = requests.get(topics_url)
topic_soup = BeautifulSoup(response.text, "html.parser")

slides_links = []
# Extract links to PDF and PPTX files
for link in topic_soup.find_all("a", href=True):
    href = link["href"]
    if re.search(r'\.pdf$|\.pptx$', href):
        slides_links.append(href)
        print(href)

print("slides number to be downloaded: ", len(slides_links))

# Step 3: Download the slides links (PDF and PPTX) into a local folder
download_folder = "downloaded_slides"
os.makedirs(download_folder, exist_ok=True)

# Configure the maximum number of parallel downloads
max_workers = 5  # You can adjust this value based on your needs

with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
    for link in slides_links:
        file_name = link.split("/")[-1]
        encoded_file_name = unquote(file_name)
        file_path = os.path.join(download_folder, encoded_file_name)
        print(file_path)
        executor.submit(download_file, link, file_path)

print("Download completed.")