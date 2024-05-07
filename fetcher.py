import requests
import json
import time

# Function to fetch satellite data
def get_satellite_data(catnrs):
    satellite_data = []
    for catnr in catnrs:
        req = requests.get(f'https://www.n2yo.com/sat/instant-tracking.php?s={catnr}&hlat=40.71427&hlng=-74.00597&d=300&r=547647090737.1928&tz=GMT-04:00&O=n2yocom&rnd_str=8fde3fd56c515d8fb110d5145c7df86b&callback=')
        data = json.loads(req.text)
        target = list(data[0].values())[-1][-1]
        dats = [item for item in list(target.values())[0].split('|')]
        latitude = float(dats[0])
        longitude = float(dats[1])
        satellite_data.append((longitude, latitude))
    return satellite_data

# Function to save satellite data to a JSON file
def save_satellite_data_to_json(satellite_data, identifier, filename_prefix="satellite_data_"):
    filename = f"{filename_prefix}{identifier}.json"
    with open(filename, 'w') as file:
        json.dump(satellite_data, file)

def main():
    # Fetch satellite data
    satellite_identifiers = ['S2A', 'S2B']
    satellite_norad_ids = [40697, 42063]    # NORAD IDs, you can get more IDs from N2YO.com
    satellite_data = get_satellite_data(satellite_norad_ids)

    # Save data to JSON
    for i, data in enumerate(satellite_data):
        save_satellite_data_to_json(data, satellite_identifiers[i])

if __name__ == "__main__":
    while True:
        main()
        time.sleep(10)
