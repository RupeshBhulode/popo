import requests
from bs4 import BeautifulSoup

def scrape_video_data(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
    }
    res = requests.get(url, headers=headers, timeout=15)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")

    # Open Graph
    title = soup.find("meta", property="og:title")
    image = soup.find("meta", property="og:image")

    # Fallbacks
    if not title:
        title = soup.find("title")
    if not image:
        image = soup.find("meta", property="twitter:image")

    return {
        "url": url,
        "title": title["content"] if title and title.has_attr("content") else title.text if title else "Unknown Video",
        "thumbnail": image["content"] if image and image.has_attr("content") else "https://via.placeholder.com/120x70?text=No+Thumbnail"
    }
