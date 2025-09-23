# Copy or change the name of this file to `config.py` and then edit the values.

# Input file paths
# Custom order for hospital codes
# Output file path
import os

custom_order = [
    'SHXX','SHXX','SHXX','SHXX','SHXX','SHXX','SHXX','SHXX','SHXX',
    'SHXX','SHXX','SHXX','SHXX','SHXX','SHXX','SHXX','SHXX','SHXX',
    'SHXX','SHXX','SHXX','SHXX','SHXX','SHXX','SHXX','SHXX','SHXX',
    'SHXX','SHXX','SHXX','SHXX','SHXX','SHXX','SHXX','SHXX','SHXX'
]
# Change this one variable only:
file_tag = "1-31Aug"  # e.g. "8Sep", "15Oct", etc.

base_folder = r"C:\\Users\\YourUser\\Projects\\Active\\semi_work\\AdoptionEMR_ED_All_Unit_Calculate"

triage_filename = f"Triage_{file_tag}.csv"
discharge_filename = f"Discharge_{file_tag}.csv"
output_filename = f"Final Triage & Discharge_{file_tag}_all_units.xlsx"

path_triage = os.path.join(base_folder, triage_filename)
path_discharge = os.path.join(base_folder, discharge_filename)
output_path = os.path.join(base_folder, output_filename)

