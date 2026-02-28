# dates.py

from datetime import datetime, timedelta, timezone

# Current date and time
now = datetime.now()
print("Current Date and Time:", now)

# Create specific date
birthday = datetime(2007, 5, 15)
print("Birthday:", birthday)

# Format date
formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted Date:", formatted)

# Time difference
difference = now - birthday
print("Days since birthday:", difference.days)

# Timezone without pytz
almaty_time = datetime.now(timezone.utc)
print("UTC Time:", almaty_time)