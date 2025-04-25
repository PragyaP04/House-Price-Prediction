import pickle
import json
import numpy as np
import os

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    # Input validation
    if sqft <= 0 or bhk <= 0 or bath <= 0:
        raise ValueError("Square footage, BHK, and bath must be positive numbers.")

    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1
        print(f"Warning: Location '{location}' not found in data columns.")

    # Create input array for the model
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    # Predict and return the estimated price
    return round(__model.predict([x])[0], 2)

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model

    # Use absolute paths to avoid path issues
    base_dir = os.path.dirname(__file__)
    columns_path = os.path.join(base_dir, "artifacts", "columns.json")
    model_path = os.path.join(base_dir, "artifacts", "banglore_home_prices_model.pickle")

    # Load data columns
    with open(columns_path, "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

    # Load the model
    if __model is None:
        with open(model_path, 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print("Available locations:", get_location_names())
    print("Estimated price (1st Phase JP Nagar, 1000 sqft, 3 BHK, 3 bath):",
          get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print("Estimated price (1st Phase JP Nagar, 1000 sqft, 2 BHK, 2 bath):",
          get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print("Estimated price (Kalhalli, 1000 sqft, 2 BHK, 2 bath):",
          get_estimated_price('Kalhalli', 1000, 2, 2))  # other location
    print("Estimated price (Ejipura, 1000 sqft, 2 BHK, 2 bath):",
          get_estimated_price('Ejipura', 1000, 2, 2))  # other location