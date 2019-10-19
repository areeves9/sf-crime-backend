import csv
import os
import seed_db
import requests
from requests import HTTPError

direc = os.path.dirname(os.path.abspath(__file__))


# download CSV file and save to directory
def download_csv():
    try:
        print("Starting download...")
        url = "https://data.sfgov.org/api/views/wg3w-h783/rows.csv?accessType=DOWNLOAD&amp;api_foundry=true"
        r = requests.get(url)
        r.raise_for_status()
        data = r.text.splitlines()
        c1 = csv.reader(data)
        with open(f'{direc}/sf_crime_2018.csv', 'w') as f:
            writer = csv.writer(f)
            for row in c1:
                writer.writerow(row[0:26])
            print(f"Saved to directory {direc}")
        return seed_db.seed_db()
    except HTTPError as e:
        return print(f'HTTP error has occured: {e}')