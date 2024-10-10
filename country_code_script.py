import pandas as pd
import pycountry

# Function to convert country code to country name
def code_to_country_name(code):
    try:
        return pycountry.countries.get(alpha_2=code).name
    except:
        return None  # In case the code doesn't exist

# Load the CSV files
file_1 = 'path_to_your_first_file.csv'
file_2 = 'path_to_your_second_file.csv'

# Read the CSV files into pandas DataFrames
df1 = pd.read_csv(file_1)
df2 = pd.read_csv(file_2)

# Assuming the country codes are in a column named 'country_code'
df1['country_name'] = df1['country_code'].apply(code_to_country_name)
df2['country_name'] = df2['country_code'].apply(code_to_country_name)

# Save the DataFrames back to CSV
df1.to_csv('first_file_with_country_names.csv', index=False)
df2.to_csv('second_file_with_country_names.csv', index=False)

print("Country codes successfully converted and saved in new CSV files.")
