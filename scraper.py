# Dependencies
import requests
from bs4 import BeautifulSoup

# Fetching function
def fetch_classifieds(url):
    
    # Anti-block measure
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # GET response
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Error handling
    except requests.exceptions.RequestException as error:
        print(f"Error fetching the requested URL: {error}")
        return []
    
    # Parsing retrieved HTPP content
    soup = BeautifulSoup(response.content, 'html.parser')
    print("Retriving successul")

    listings = []

    links = []
    
    # Extracting data
    for item in soup.select('h3[data-testid="listing-title"]'):
        title = item.get_text(strip=True)
        listings.append(title)

    for link_tag in soup.select('a[data-testid="listing-link"]'):
        link = link_tag['href']
        links.append(link)
        
    # Error handling
    if not listings:
        print("No listings found")
    
    return listings, links

# Main 
def main():
    url = "https://www.kijiji.ca/b-bikes/ottawa/c644l1700185"
    titles, links = fetch_classifieds(url)
    
    print("Titles:")
    for title in titles:
        print(title)
    
    print("\nLinks:")
    for link in links:
        print(link)

if __name__ == "__main__":
    main()
