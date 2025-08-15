#!/usr/bin/env python3
"""
Simple script to validate if a sched.com URL is accessible and contains slides
"""
import sys
import requests
from bs4 import BeautifulSoup
import re

def validate_url(url):
    """Check if URL is accessible and contains slide links"""
    try:
        print(f"Testing: {url}")
        response = requests.get(url, timeout=10)
        
        if response.status_code != 200:
            print(f"❌ HTTP {response.status_code} - URL not accessible")
            return False
            
        soup = BeautifulSoup(response.text, "html.parser")
        slides_links = []
        
        # Extract links to PDF and PPTX files
        for link in soup.find_all("a", href=True):
            href = link["href"]
            if re.search(r'\.pdf$|\.pptx$', href):
                slides_links.append(href)
        
        if slides_links:
            print(f"✅ Found {len(slides_links)} slide files")
            print("Sample files:")
            for link in slides_links[:3]:  # Show first 3 files
                filename = link.split("/")[-1]
                print(f"  - {filename}")
            if len(slides_links) > 3:
                print(f"  ... and {len(slides_links) - 3} more")
            return True
        else:
            print("⚠️  URL accessible but no slide files found")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Connection error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 validate_url.py <sched_url>")
        print("Example: python3 validate_url.py https://kccncna2024.sched.com/list/descriptions/")
        sys.exit(1)
    
    url = sys.argv[1]
    validate_url(url)