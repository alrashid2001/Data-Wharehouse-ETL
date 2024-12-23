# Initialize Dir for Database
import os
import sys
import yaml
# Set the base directory relative to the script's location
MAIN_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))

print("Main" + str(MAIN_DIR))
os.makedirs(f"{MAIN_DIR}/database/archive", exist_ok=True)
os.makedirs(f"{MAIN_DIR}/database/sql", exist_ok=True)
os.makedirs(f"{MAIN_DIR}/database/trasformer_data", exist_ok=True)
os.makedirs(f"{MAIN_DIR}/database/csv_data", exist_ok=True)

os.makedirs(f"{MAIN_DIR}/visualize", exist_ok=True)

