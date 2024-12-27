import pandas as pd
from ydata_profiling import ProfileReport

# Load the Excel file
df = pd.read_excel('flight_price.xlsx')

# Generate the profile report
profile = ProfileReport(df)
profile.to_file(output_file="flight.html")

print("Profile report generated successfully!")
