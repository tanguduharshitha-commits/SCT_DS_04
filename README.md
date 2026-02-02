# SCT_DS_04
TASK:04 An exploratory data analysis project using Python to identify and visualize safety patterns in traffic accident data based on time, weather, and road conditions.
GitHub Project Description: Traffic Accident Data Analysis
📌 Project Overview
This project, completed as part of the SkillCraft Technology internship, focuses on analyzing traffic accident data to identify critical safety patterns. The primary goal is to visualize how external factors such as time of day, weather conditions, and road surfaces contribute to accident frequency.

🛠️ Technical Stack
Language: Python 3.14
Libraries: * Pandas: For data manipulation and cleaning.
Matplotlib: For generating data visualizations and trend charts.
IDE: PyCharm.
📊 Task Objectives
Data Cleaning: Processing raw accident datasets, including handling time-format conversions and managing missing or invalid entries.
Trend Analysis: Extracting temporal data (hours) to identify peak accident times.
Visualization: Creating line charts to represent accident "hotspots" and contributing factors throughout a 24-hour cycle.
🧩 Key Challenges & Solutions
During development, a ParserError was encountered due to the dataset being saved in .rtf (Rich Text Format) instead of a standard .csv.
Solution: The data was successfully re-tokenized by ensuring the source file was converted to a plain-text CSV format, allowing the Pandas engine to correctly parse the fields.
📈 Sample Insights
The analysis currently focuses on Time of Day Trend Analysis, utilizing a line chart to visualize accident frequency by the hour to help identify when road users are at the highest risk.
