import json
import math

# Define emission factors (gCO2 per km) for each type of transport
EMISSION_FACTORS = {
    'Suburban': 100,  
    'Subway': 70,     
    'Tram': 50,       
    'Bus': 120,      
    'Ferry': 150,     
    'Express': 90,   
    'Regional': 110 
}

def load_json(filename):
    """ Load JSON data from a file """
    with open(filename, 'r') as file:
        return json.load(file)

def haversine_distance(lat1, lon1, lat2, lon2):
    """ Calculate the great-circle distance between two points on the Earth's surface """
    R = 6371  # Radius of the Earth in kilometers
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    
    a = math.sin(delta_phi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    distance = R * c
    return distance

def display_routes(data):
    """ Display the starting point, destination, and available routes, allowing user to select a route """
    if not isinstance(data, list):
        print("Error: JSON data is not a list")
        return

    for entry_idx, entry in enumerate(data):
        starting_address = entry.get('startingAddress', 'N/A')
        destination_address = entry.get('destinationAddress', 'N/A')
        print(f"\nStarting Point: {starting_address}")
        print(f"Destination: {destination_address}")

        print("\nAvailable Routes:")
        from_stops = entry.get('fromStops', [])
        if not from_stops:
            print("  No stops available.")
            continue
        
        for idx, stop in enumerate(from_stops):
            stop_name = stop.get('name', 'Unknown Stop')
            stop_id = stop.get('id', 'Unknown ID')
            print(f"\nStop {idx + 1}:")
            print(f"  Name: {stop_name}")
            print(f"  ID: {stop_id}")
            print(f"  Latitude: {stop['location']['latitude']}")
            print(f"  Longitude: {stop['location']['longitude']}")
            print(f"  Products: {', '.join([key.capitalize() for key, value in stop['products'].items() if value])}")

        # Ask user to select a route
        try:
            route_idx = int(input("\nSelect a route number (or 0 to skip): ")) - 1
            if 0 <= route_idx < len(from_stops):
                selected_stop = from_stops[route_idx]
                print(f"\nSelected Route Details:")
                print(f"  Name: {selected_stop['name']}")
                print(f"  ID: {selected_stop['id']}")
                print(f"  Latitude: {selected_stop['location']['latitude']}")
                print(f"  Longitude: {selected_stop['location']['longitude']}")
                print(f"  Products: {', '.join([key.capitalize() for key, value in selected_stop['products'].items() if value])}")

                # Ask user to select products
                selected_products = []
                print("\nAvailable Products:")
                for product, is_available in selected_stop['products'].items():
                    if is_available:
                        print(f"  {product.capitalize()}")
                        if input(f"Do you use {product.capitalize()}? (y/n): ").lower() == 'y':
                            selected_products.append(product.capitalize())

                # Calculate emissions
                if len(from_stops) > 1:
                    distance = calculate_distance_between_stops(from_stops)
                    print(f"\nCalculated Distance: {distance:.2f} km")
                else:
                    distance = float(input("Enter the distance of the route in km: "))

                emissions = calculate_emissions(selected_products, distance)
                print(f"\nEstimated CO2 emissions for the selected route: {emissions:.2f} grams")
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input.")

def calculate_distance_between_stops(stops):
    """ Calculate the total distance between consecutive stops """
    total_distance = 0
    for i in range(len(stops) - 1):
        lat1, lon1 = stops[i]['location']['latitude'], stops[i]['location']['longitude']
        lat2, lon2 = stops[i + 1]['location']['latitude'], stops[i + 1]['location']['longitude']
        distance = haversine_distance(lat1, lon1, lat2, lon2)
        total_distance += distance
    return total_distance

def calculate_emissions(products, distance):
    """ Calculate emissions based on selected products and distance """
    total_emissions = 0
    for product in products:
        emission_factor = EMISSION_FACTORS.get(product, 0)
        total_emissions += emission_factor * distance

    return total_emissions

def main():
    filename = 'data.json'
    data = load_json(filename)
    
    display_routes(data)

if __name__ == '__main__':
    main()
