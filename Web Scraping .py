from bs4 import BeautifulSoup
import requests
import pandas as pd

# Initialize data list
data = []

# Define base URL for Amazon search results (change the search term if needed)
base_url = ' '

# Step 1: Scrape up to 7 pages (pagination)
max_pages = 7  # Limit to 7 pages
page = 1  # Starting from page 1

while page <= max_pages:
    print(f"Scraping page {page}...")
    
    # Fetch the URL for the current page
    url = base_url.format(page)
    headers = {'User-Agent':'  ', 'Accept-Language': 'en-US, en;q=0.5'} #add your header
    response = requests.get(url, headers=headers)
    
    # If the page is not available (404 or empty), stop scraping
    if response.status_code != 200:
        print("Reached the end of pages or encountered an error. Stopping.")
        break
    
    # Step 2: Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    products = soup.find_all("div", class_="s-result-item")
    
    # Step 3: Check if we have any products; if not, stop scraping
    if not products:
        print("No products found. Stopping.")
        break

    # Step 4: Extract product data
    for product in products:
        title_tag = product.find("h2", class_="a-size-base-plus a-spacing-none a-color-base a-text-normal")
        link_tag = product.find("a", class_="a-link-normal s-line-clamp-4 s-link-style a-text-normal")
        rating_tag = product.find("span", class_="a-size-base s-underline-text")
        
        if title_tag and link_tag and rating_tag:
            try:
                rating_count = int(rating_tag.text.replace(",", "").strip())
            except:
                rating_count = 0
            
            # Only include products with rating > 50
            if rating_count > 50:
                title = title_tag.get_text(strip=True)
                href = link_tag.get('href')
                full_link = f"https://www.amazon.com.au{href}"  # Full URL added here
                
                # Add product data to the list
                data.append({"Product Name": title, "Product URL": full_link})
    
    # Move to the next page
    page += 1

# Step 5: Save the results to Excel
df = pd.DataFrame(data)
df.to_excel("products_limited_7_pages.xlsx", index=False)

print(f"✅ Scraping completed and saved to products_limited_7_pages.xlsx")


