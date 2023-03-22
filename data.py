import pandas as pd

# Set the file path and read the CSV file into a DataFrame
file_path = "products.csv"
df = pd.read_csv(file_path)

# Remove the specified columns
columns_to_remove = ["product_of_the_day_date"]
df.drop(columns=columns_to_remove, inplace=True)

# Save the updated DataFrame as a new CSV file
output_file_path = "output.csv"
df.to_csv(output_file_path, index=False)
