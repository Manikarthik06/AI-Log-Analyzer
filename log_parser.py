import re
import pandas as pd

def parse_log_lines(log_lines):

    pattern = re.compile(
        r'(?P<month>\w+)\s+'
        r'(?P<day>\d+)\s+'
        r'(?P<time>\d+:\d+:\d+)\s+'
        r'(?P<host>\S+)\s+'
        r'(?P<service>[^\[]+)'
        r'\[(?P<pid>\d+)\]:\s+'
        r'(?P<message>.*)'
    )

    records = []

    for line in log_lines:

        match = pattern.match(line.strip())

        if match:

            records.append({
            "month": match.group("month"),
            "day": match.group("day"),
            "time": match.group("time"),
            "host": match.group("host"),
            "service": match.group("service").strip(),
            "pid": match.group("pid"),
            "message": match.group("message")
        })

    return pd.DataFrame(records)


# CHANGE THIS TO YOUR LOG FILE NAME
log_file = "/Users/manikarthikgarlapati/Documents/vs code/AILA/hi.log"
# Read the log file
with open(log_file, "r") as file:
    log_lines = file.readlines()

# Parse the logs
df = parse_log_lines(log_lines)

# Display the first few rows
print(df.head())

# Optional: Save parsed logs to CSV
df.to_csv("parsed_logs.csv", index=False)

print("\nParsing completed successfully!")
print(f"Total log entries parsed: {len(df)}")

    