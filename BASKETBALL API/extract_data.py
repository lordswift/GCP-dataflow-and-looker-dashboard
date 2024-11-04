import requests
import csv

url = "https://api-basketball.p.rapidapi.com/teams"
querystring = {"league":"12","season":"2019-2020"}
headers = {
    "x-rapidapi-key": "",
    "x-rapidapi-host": "api-basketball.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

if response.status_code == 200:
    data = response.json().get('response', [])
    csv_filename = 'rankings.csv'

    if data:
        # Update field names to include country name
        field_names = ['id', 'name', 'country_name']

        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()
            for entry in data:
                # Create a dictionary with the required fields
                row_data = {
                    'id': entry.get('id'),
                    'name': entry.get('name'),
                    'country_name': entry.get('country', {}).get('name')  # Access nested country name
                }
                writer.writerow(row_data)

        print(f"Data fetched successfully and written to '{csv_filename}'")
    else:
        print("No data available from the API.")
else:
    print("Failed to fetch data:", response.status_code)
