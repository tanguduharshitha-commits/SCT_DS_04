import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data
# If you have empty rows at the top, change '0' to the number of rows to skip
try:
    df = pd.read_csv('accidents.csv', skiprows=7)  # Adjust the number if needed

    # 2. Pattern: Time of Day Trend (Line Chart)
    # Ensure 'TIME' column is treated as a string then converted
    df['TIME'] = df['TIME'].astype(str)
    df['Hour'] = pd.to_datetime(df['TIME'], format='%H:%M', errors='coerce').dt.hour

    # Remove any rows where time couldn't be parsed
    df = df.dropna(subset=['Hour'])

    time_counts = df['Hour'].value_counts().sort_index()

    plt.figure(figsize=(10, 5))
    plt.plot(time_counts.index, time_counts.values, marker='o', color='blue', linestyle='-')
    plt.title('Accident Trends by Time of Day')
    plt.xlabel('Hour (24-hour format)')
    plt.ylabel('Number of Accidents')
    plt.xticks(range(0, 24))
    plt.grid(True)
    plt.savefig('time_trend.png')
    plt.show()

    print("Task 04: Line Chart Generated Successfully!")

except FileNotFoundError:
    print("Error: 'accidents.csv' not found. Make sure the file is in the same folder as this script.")