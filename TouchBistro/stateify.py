import pandas as pd
from typing import Dict

# Define province/state mappings
ca_provinces: Dict[str, str] = {
    "ON": [
        "Toronto",
        "Ottawa",
        "Hamilton",
        "Mississauga",
        "Brampton",
        "London",
        "Windsor",
        "Kitchener",
        "Kingston",
        "Vaughan",
        "Markham",
        "Scarborough",
        "Oshawa",
        "Burlington",
        "Barrie",
        "St. Catharines",
        "Guelph",
        "Cambridge",
        "Whitby",
        "Ajax",
        "Milton",
    ],
    "BC": [
        "Vancouver",
        "Victoria",
        "Burnaby",
        "Surrey",
        "Richmond",
        "Kelowna",
        "Nanaimo",
        "Delta",
        "Kamloops",
        "White Rock",
        "North Vancouver",
        "Langford",
        "Squamish",
    ],
    "AB": [
        "Calgary",
        "Edmonton",
        "Red Deer",
        "Lethbridge",
        "St. Albert",
        "Medicine Hat",
        "Grande Prairie",
        "Airdrie",
        "Spruce Grove",
        "Leduc",
        "Sherwood Park",
    ],
    "QC": [
        "Montreal",
        "Quebec City",
        "Laval",
        "Gatineau",
        "Longueuil",
        "Sherbrooke",
        "Saguenay",
        "Levis",
        "Trois-Rivieres",
    ],
    "NS": [
        "Halifax",
        "Dartmouth",
        "Sydney",
        "Truro",
        "New Glasgow",
        "Kentville",
        "Yarmouth",
    ],
    "MB": [
        "Winnipeg",
        "Brandon",
        "Steinbach",
        "Thompson",
        "Portage la Prairie",
        "Selkirk",
    ],
    "SK": [
        "Saskatoon",
        "Regina",
        "Prince Albert",
        "Moose Jaw",
        "Swift Current",
        "Yorkton",
    ],
    "NB": [
        "Saint John",
        "Fredericton",
        "Moncton",
        "Bathurst",
        "Miramichi",
        "Edmundston",
    ],
    "NL": ["St. Johns", "Mount Pearl", "Corner Brook", "Gander", "Grand Falls-Windsor"],
    "PE": ["Charlottetown", "Summerside", "Stratford", "Cornwall"],
}

us_states: Dict[str, str] = {
    "AL": ["Birmingham", "Montgomery", "Mobile", "Huntsville", "Tuscaloosa"],
    "AK": ["Anchorage", "Fairbanks", "Juneau", "Sitka", "Wasilla"],
    "AZ": [
        "Phoenix",
        "Tucson",
        "Mesa",
        "Chandler",
        "Scottsdale",
        "Glendale",
        "Gilbert",
    ],
    "AR": ["Little Rock", "Fort Smith", "Fayetteville", "Springdale", "Jonesboro"],
    "CA": [
        "Los Angeles",
        "San Francisco",
        "San Diego",
        "San Jose",
        "Sacramento",
        "Oakland",
        "Santa Ana",
        "Fresno",
        "Long Beach",
        "Bakersfield",
    ],
    "CO": [
        "Denver",
        "Colorado Springs",
        "Aurora",
        "Fort Collins",
        "Lakewood",
        "Boulder",
    ],
    "CT": ["Bridgeport", "New Haven", "Hartford", "Stamford", "Waterbury"],
    "DE": ["Wilmington", "Dover", "Newark", "Middletown", "Smyrna"],
    "FL": [
        "Miami",
        "Orlando",
        "Tampa",
        "Jacksonville",
        "Fort Lauderdale",
        "Tallahassee",
        "Gainesville",
    ],
    "GA": ["Atlanta", "Augusta", "Columbus", "Savannah", "Athens"],
    "HI": ["Honolulu", "Pearl City", "Hilo", "Kailua", "Kaneohe"],
    "ID": ["Boise", "Meridian", "Nampa", "Idaho Falls", "Pocatello"],
    "IL": ["Chicago", "Aurora", "Rockford", "Joliet", "Naperville", "Springfield"],
    "IN": ["Indianapolis", "Fort Wayne", "Evansville", "South Bend", "Carmel"],
    "IA": ["Des Moines", "Cedar Rapids", "Davenport", "Sioux City", "Iowa City"],
    "KS": ["Wichita", "Overland Park", "Kansas City", "Olathe", "Topeka"],
    "KY": ["Louisville", "Lexington", "Bowling Green", "Owensboro", "Covington"],
    "LA": ["New Orleans", "Baton Rouge", "Shreveport", "Lafayette", "Lake Charles"],
    "ME": ["Portland", "Lewiston", "Bangor", "South Portland", "Auburn"],
    "MD": ["Baltimore", "Frederick", "Rockville", "Gaithersburg", "Annapolis"],
    "MA": ["Boston", "Worcester", "Springfield", "Cambridge", "Lowell"],
    "MI": ["Detroit", "Grand Rapids", "Warren", "Sterling Heights", "Ann Arbor"],
    "MN": ["Minneapolis", "St. Paul", "Rochester", "Duluth", "Bloomington"],
    "MS": ["Jackson", "Gulfport", "Southaven", "Hattiesburg", "Biloxi"],
    "MO": ["Kansas City", "St. Louis", "Springfield", "Columbia", "Independence"],
    "MT": ["Billings", "Missoula", "Great Falls", "Bozeman", "Butte"],
    "NE": ["Omaha", "Lincoln", "Bellevue", "Grand Island", "Kearney"],
    "NV": ["Las Vegas", "Reno", "Henderson", "North Las Vegas", "Sparks"],
    "NH": ["Manchester", "Nashua", "Concord", "Dover", "Rochester"],
    "NJ": ["Newark", "Jersey City", "Paterson", "Elizabeth", "Trenton"],
    "NM": ["Albuquerque", "Las Cruces", "Rio Rancho", "Santa Fe", "Roswell"],
    "NY": ["New York", "Buffalo", "Rochester", "Yonkers", "Syracuse", "Brooklyn"],
    "NC": ["Charlotte", "Raleigh", "Greensboro", "Durham", "Winston-Salem"],
    "ND": ["Fargo", "Bismarck", "Grand Forks", "Minot", "West Fargo"],
    "OH": ["Columbus", "Cleveland", "Cincinnati", "Toledo", "Akron"],
    "OK": ["Oklahoma City", "Tulsa", "Norman", "Broken Arrow", "Edmond"],
    "OR": ["Portland", "Salem", "Eugene", "Gresham", "Hillsboro", "Bend"],
    "PA": ["Philadelphia", "Pittsburgh", "Allentown", "Erie", "Reading"],
    "RI": ["Providence", "Warwick", "Cranston", "Pawtucket", "East Providence"],
    "SC": ["Columbia", "Charleston", "North Charleston", "Mount Pleasant", "Rock Hill"],
    "SD": ["Sioux Falls", "Rapid City", "Aberdeen", "Brookings", "Watertown"],
    "TN": ["Nashville", "Memphis", "Knoxville", "Chattanooga", "Clarksville"],
    "TX": [
        "Houston",
        "Dallas",
        "Austin",
        "San Antonio",
        "Fort Worth",
        "El Paso",
        "Arlington",
    ],
    "UT": ["Salt Lake City", "West Valley City", "Provo", "West Jordan", "Orem"],
    "VT": ["Burlington", "South Burlington", "Rutland", "Barre", "Montpelier"],
    "VA": ["Virginia Beach", "Norfolk", "Chesapeake", "Richmond", "Newport News"],
    "WA": ["Seattle", "Spokane", "Tacoma", "Vancouver", "Bellevue"],
    "WV": ["Charleston", "Huntington", "Parkersburg", "Morgantown", "Wheeling"],
    "WI": ["Milwaukee", "Madison", "Green Bay", "Kenosha", "Racine"],
    "WY": ["Cheyenne", "Casper", "Laramie", "Gillette", "Rock Springs"],
}


def get_province(city: str) -> str:
    for province, cities in ca_provinces.items():
        if any(city.lower() == c.lower() for c in cities):
            return province
    return ""


def get_state(city: str) -> str:
    for state, cities in us_states.items():
        if any(city.lower() == c.lower() for c in cities):
            return state
    return ""


def add_state_province(df: pd.DataFrame) -> pd.DataFrame:
    # Add new column
    df["state_province"] = ""

    # Process each row
    for idx, row in df.iterrows():
        if row["country"] == "CA":
            df.at[idx, "state_province"] = get_province(row["city"])
        elif row["country"] == "US":
            df.at[idx, "state_province"] = get_state(row["city"])

    # Reorder columns to put state_province after city
    cols = df.columns.tolist()
    city_idx = cols.index("city")
    cols.remove("state_province")
    cols.insert(city_idx + 1, "state_province")
    df = df[cols]

    return df


# Read the CSV
df = pd.read_csv("venues.csv")

# Add state/province information
df = add_state_province(df)

# Save the updated dataset
df.to_csv("venues_with_states.csv", index=False)

# Print first few rows to verify
print(df.head())
