import requests
import json
from datetime import datetime
import os

BASE_URL = 'https://v6.bvg.transport.rest'

def get_closest_stops(address):
    params = {'query': address, 'results': 5}
    try:
        response = requests.get(f'{BASE_URL}/locations', params=params)
        print(f'Request URL: {response.url}')  # Log the request URL
        response.raise_for_status()
        data = response.json()
        print(f'API response for address "{address}": {data}')  # Log the API response
        if isinstance(data, list):
            stops = [item for item in data if item['type'] in ['stop', 'station']]
            return stops if stops else None
        else:
            print(f"Unexpected response format: {data}")
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        print(f'Response content: {response.content}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    return None

def get_journey_data(from_station, to_station, date_time):
    url = f'{BASE_URL}/journeys?from={from_station}&to={to_station}&departure={date_time}&results=5&language=en'
    try:
        response = requests.get(url)
        print(f'Request URL: {response.url}')  # Log the request URL
        response.raise_for_status()
        data = response.json()
        print(f'API response for journey query: {data}')  # Log the API response
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        print(f'Response content: {response.content}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    return None

def read_existing_data(filename='data.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            try:
                data = json.load(f)
                # If the file contains a dictionary, convert it to a list
                if isinstance(data, dict):
                    return [data]
                return data
            except json.JSONDecodeError as e:
                print(f'Failed to decode JSON from file: {e}')
                return []
    return []

def append_data_to_file(data, filename='data.json'):
    existing_data = read_existing_data(filename)
    if not isinstance(existing_data, list):
        existing_data = []
    existing_data.append(data)
    try:
        with open(filename, 'w') as f:
            json.dump(existing_data, f, indent=4)
        print(f'Data successfully appended to {filename}')
    except Exception as e:
        print(f'Failed to save data to file: {e}')

def main():
    start_address = input('Enter the starting address: ')
    destination_address = input('Enter the destination address: ')

    date_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    print(f'Using date and time: {date_time}')

    try:
        from_stops = get_closest_stops(start_address)
        to_stops = get_closest_stops(destination_address)

        if from_stops and to_stops:
            from_station_ibnr = from_stops[0]['id']
            to_station_ibnr = to_stops[0]['id']

            print(f'From station IBNR: {from_station_ibnr}')
            print(f'To station IBNR: {to_station_ibnr}')

            journey_data = get_journey_data(from_station_ibnr, to_station_ibnr, date_time)
            if journey_data:
                # Prepare data for saving
                data_to_save = {
                    'startingAddress': start_address,
                    'destinationAddress': destination_address,
                    'dateTime': date_time,
                    'fromStops': from_stops,
                    'toStops': to_stops,
                    'journeyData': journey_data
                }
                append_data_to_file(data_to_save)
            else:
                print('Failed to retrieve journey data.')
        else:
            print('Failed to retrieve stops for the addresses.')
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    main()
