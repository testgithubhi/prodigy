
import requests


def scrape_website(url):
    # Make a GET request to the website
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Example: Extract all the links on the page
        links = soup.find_all('a')
        for link in links:
            print(link.get('href'))

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Replace 'https://example.com' with the URL of the website you want to scrape
scrape_website('https://vvce.ac.in/')