import pandas as pd


def convert_dates_to_iso8601(input_file, output_file, date_columns):
    """
    Convert dates in specified columns to ISO 8601 format

    Args:
        input_file (str): Path to input CSV file
        output_file (str): Path to output CSV file
        date_columns (list): List of column names containing dates
    """
    # Read the CSV file
    df = pd.read_csv(input_file)

    # Convert each date column to ISO 8601
    for column in date_columns:
        if column in df.columns:
            df[column] = pd.to_datetime(df[column]).dt.strftime("%Y-%m-%dT%H:%M:%SZ")

    # Save the converted data to a new CSV file
    df.to_csv(output_file, index=False)


if __name__ == "__main__":
    # Example usage
    input_file = "bills.csv"
    output_file = "bills_iso.csv"
    date_columns = [
        "bill_paid_at_local",
        "order_closed_at_local",
        "order_seated_at_local",
    ]  # Add your date column names here

    try:
        convert_dates_to_iso8601(input_file, output_file, date_columns)
        print(
            f"Successfully converted dates to ISO 8601 format. Output saved to {output_file}"
        )
    except Exception as e:
        print(f"An error occurred: {str(e)}")
