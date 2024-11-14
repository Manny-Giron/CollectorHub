import requests
from bs4 import BeautifulSoup

"""
    DISCLAIMER: The following is script is meant to webscrape ebay as a current alternative 
    of using their API. This DOES go against their terms. This is just for current
    testing for the front end whilst working on getting / understandings ebay's API.


"""

# Hold each items in this array, as a array itself. Index array will represent item.
# ex. arr[0] == First item parsed. arr[0][0] == Item index, arr[0][1] == Item title, etc etc
cardsArray = []



"""
    Set-up: Using BS4, we give it ebays base url setup, and add the search term we input to it.
    Send / Get a response when use combine the url and term together (making seearch url)
    We then grab the first 10 items, (can change) and store its html into listings.
    We then parse through i
"""
def find_card(search_term):
    # Format the search term for the eBay URL
    formatted_search_term = search_term.replace(' ', '+')
    url = f"https://www.ebay.com/sch/i.html?_nkw={formatted_search_term}"

    # Send a request to eBay and parse the page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the listings and limit to the first 10 results
    listings = soup.select('.s-item')[:10]

    # Check if any listings were found
    if not listings:
        print(f"No results found for '{search_term}'.")
        return

    print(listings)
    # Output each result to the terminal
    for idx, listing in enumerate(listings, 1):
        # Extract the title
        title_tag = listing.select_one('.s-item__title')
        title = title_tag.get_text(strip=True) if title_tag else 'No title available'

        # Extract the link
        link_tag = listing.select_one('.s-item__link')
        link = link_tag['href'] if link_tag else 'No link available'

        # Extract the image URL
        image_wrapper = listing.select_one('.s-item__image-wrapper.image-treatment img')
        image_url = image_wrapper['src'] if image_wrapper else 'No image available'

        # Extract the price
        price_tag = listing.select_one('.s-item__price')
        price = price_tag.get_text(strip=True) if price_tag else 'No price available'
        cardsArray.append([[idx],[title],[link],[image_url],[price]])
        # Print each item's details
        print(f"Item {idx}:")
        print(f"Title: {title}")
        print(f"Link: {link}")
        print(f"Image URL: {image_url}")
        print(f"Price: {price}")
        print("-" * 100)

# Get user input and call the function
search_term = str(input("Enter the name of the card you're looking for: "))
find_card(search_term)