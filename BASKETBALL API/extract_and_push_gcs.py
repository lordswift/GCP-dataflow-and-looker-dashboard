import requests
import csv
from google.cloud import storage

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
            # writer.writeheader()
            for entry in data:
                # Create a dictionary with the required fields
                row_data = {
                    'id': entry.get('id'),
                    'name': entry.get('name'),
                    'country_name': entry.get('country', {}).get('name')  # Access nested country name
                }
                writer.writerow(row_data)

        print(f"Data fetched successfully and written to '{csv_filename}'")

        # Upload the CSV file to GCS
        bucket_name = 'bkt-ranking-data-sk'
        storage_client = storage.Client(project='project001-440621')
        bucket = storage_client.bucket(bucket_name)
        destination_blob_name = f'{csv_filename}'  # The path to store in GCS

        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(csv_filename)