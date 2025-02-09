import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_numbeo_rankings():
    # URL of the page
    url = "https://www.numbeo.com/cost-of-living/region_rankings.jsp?title=2025&region=021"

    try:
        # Send request to the website
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the table
        table = soup.find("table", {"id": "t2"})

        # Lists to store the data
        cities = []
        states = []
        cost_of_living_indices = []
        rent_index = []
        cost_of_living_plus_rent_index = []
        groceries_index = []
        restaurant_price_index = []
        local_purchasing_power_index = []

        # Extract rows from table
        rows = table.find_all("tr")[1:]  # Skip header row

        for row in rows:
            cols = row.find_all("td")

            dma = cols[1].text.strip()
            print(dma)
            city, state = dma.split(",")[:2]
            cities.append(city)
            states.append(state)
            cost_of_living_indices.append(cols[2].text.strip())
            rent_index.append(cols[3].text.strip())
            cost_of_living_plus_rent_index.append(cols[4].text.strip())
            groceries_index.append(cols[5].text.strip())
            restaurant_price_index.append(cols[6].text.strip())
            local_purchasing_power_index.append(cols[7].text.strip())

        # Create DataFrame
        df = pd.DataFrame(
            {
                "City": cities,
                "State": states,
                "Cost of Living Index": cost_of_living_indices,
                "Rent Index": rent_index,
                "Cost of Living Plus Rent Index": cost_of_living_plus_rent_index,
                "Groceries Index": groceries_index,
                "Restaurant Price Index": restaurant_price_index,
                "Local Purchasing Power Index": local_purchasing_power_index,
            }
        )

        return df

    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None
    except Exception as e:
        print(f"Error processing the data: {e}")
        return None


# Run the scraper
if __name__ == "__main__":
    df = scrape_numbeo_rankings()
    if df is not None:
        print(df)
        # Optionally save to CSV
        df.to_csv("numbeo_rankings.csv", index=False)
