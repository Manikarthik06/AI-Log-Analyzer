import pandas as pd

# Load parsed logs
df = pd.read_csv("parsed_logs.csv")

# 1. Total logs
total_logs = len(df)

# 2. Top services
top_services = df["service"].value_counts().head(10)

# 3. Failed logins
failed_logins = df["message"].str.contains(
    "authentication failure|failed password",
    case=False,
    na=False
).sum()
import re
from collections import Counter

# Extract IPv4 addresses from messages
ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

ips = []

for msg in df["message"]:
    if pd.notna(msg):
        found_ips = re.findall(ip_pattern, str(msg))
        ips.extend(found_ips)

# Count occurrences of each IP
ip_counts = Counter(ips)

print("\nTop 10 IP Addresses:")
for ip, count in ip_counts.most_common(10):
    print(f"{ip} -> {count}")

# ==========================
# LOG STATISTICS MODULE
# ==========================

print("\n===== LOG STATISTICS =====")

# Total logs
total_logs = len(df)
print(f"Total Logs: {total_logs}")

# Failed logins
failed_logins = df["message"].str.contains(
    "failed|failure|invalid", case=False, na=False
).sum()
print(f"Failed Logins: {failed_logins}")

# Successful logins
successful_logins = df["message"].str.contains(
    "accepted|success", case=False, na=False
).sum()
print(f"Successful Logins: {successful_logins}")

# Top services
print("\nTop Services:")
print(df["service"].value_counts().head(5))

# Most common log messages
print("\nMost Common Events:")
print(df["message"].value_counts().head(5))

# Suspicious events
suspicious_keywords = [
    "failed",
    "failure",
    "invalid",
    "denied",
    "attack",
    "scan",
    "timeout",
]

suspicious_logs = df[
    df["message"].str.contains(
        "|".join(suspicious_keywords),
        case=False,
        na=False
    )
]

print(f"\nSuspicious Events Found: {len(suspicious_logs)}")

# Severity calculation
if len(suspicious_logs) < 10:
    severity = "LOW"
elif len(suspicious_logs) < 50:
    severity = "MEDIUM"
else:
    severity = "HIGH"

print(f"Overall Severity: {severity}")
