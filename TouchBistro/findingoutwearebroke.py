us_min_wage = {
    "State": [
        "Alabama",
        "Alaska",
        "Arizona",
        "Arkansas",
        "California",
        "Colorado",
        "Connecticut",
        "Delaware",
        "Florida",
        "Georgia",
        "Hawaii",
        "Idaho",
        "Illinois",
        "Indiana",
        "Iowa",
        "Kansas",
        "Kentucky",
        "Louisiana",
        "Maine",
        "Maryland",
        "Massachusetts",
        "Michigan",
        "Minnesota",
        "Mississippi",
        "Missouri",
        "Montana",
        "Nebraska",
        "Nevada",
        "New Hampshire",
        "New Jersey",
        "New Mexico",
        "New York",
        "North Carolina",
        "North Dakota",
        "Ohio",
        "Oklahoma",
        "Oregon",
        "Pennsylvania",
        "Rhode Island",
        "South Carolina",
        "South Dakota",
        "Tennessee",
        "Texas",
        "Utah",
        "Vermont",
        "Virginia",
        "Washington",
        "West Virginia",
        "Wisconsin",
        "Wyoming",
    ],
    "Min_Wage_USD": [
        7.25,
        11.73,
        14.35,
        11.00,
        16.00,
        14.42,
        15.69,
        13.25,
        12.00,
        7.25,
        14.00,
        7.25,
        14.00,
        7.25,
        7.25,
        7.25,
        7.25,
        7.25,
        14.15,
        15.00,
        15.50,
        10.33,
        10.85,
        7.25,
        12.30,
        10.50,
        12.00,
        12.00,
        7.25,
        15.13,
        12.00,
        15.00,
        7.25,
        7.25,
        10.45,
        7.25,
        14.75,
        7.25,
        14.00,
        7.25,
        11.20,
        7.25,
        7.25,
        7.25,
        13.67,
        12.00,
        16.28,
        8.75,
        7.25,
        7.25,
    ],
}

# Canadian Provinces (as of 2024)
ca_min_wage = {
    "Province": [
        "Alberta",
        "British Columbia",
        "Manitoba",
        "New Brunswick",
        "Newfoundland and Labrador",
        "Northwest Territories",
        "Nova Scotia",
        "Nunavut",
        "Ontario",
        "Prince Edward Island",
        "Quebec",
        "Saskatchewan",
        "Yukon",
    ],
    "Min_Wage_CAD": [
        15.00,
        16.75,
        15.30,
        14.75,
        15.00,
        16.05,
        15.00,
        16.00,
        16.55,
        15.00,
        15.25,
        14.00,
        16.77,
    ],
}

import pandas as pd


def combine_min_wages():
    # Get exchange rate
    cad_to_usd = 0.7
    print(f"Current CAD to USD rate: {cad_to_usd}")

    # Create DataFrames
    us_df = pd.DataFrame(us_min_wage)
    ca_df = pd.DataFrame(ca_min_wage)

    # Convert Canadian wages to USD
    ca_df["Min_Wage_USD"] = ca_df["Min_Wage_CAD"] * cad_to_usd

    # Add country column
    us_df["Country"] = "USA"
    ca_df["Country"] = "Canada"

    # Rename columns for consistency
    us_df = us_df.rename(columns={"State": "Region"})
    ca_df = ca_df.rename(columns={"Province": "Region"})

    # Combine datasets
    combined_df = pd.concat(
        [
            us_df[["Region", "Country", "Min_Wage_USD"]],
            ca_df[["Region", "Country", "Min_Wage_USD"]],
        ],
        ignore_index=True,
    )

    # Sort by minimum wage
    combined_df = combined_df.sort_values("Min_Wage_USD", ascending=False)

    # Round to 2 decimal places
    combined_df["Min_Wage_USD"] = combined_df["Min_Wage_USD"].round(2)

    return combined_df


# Run the combination
if __name__ == "__main__":
    df = combine_min_wages()
    print(df)
    df.to_csv("combined_minimum_wages.csv", index=False)
