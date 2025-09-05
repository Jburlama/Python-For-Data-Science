import time

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec"
]

timestamp = time.time()

print(f"Seconds since January 1, 1970: {timestamp: ,.4f}", end="")
print(f" or {timestamp:.3} in scientific notation")
localtime = time.localtime(timestamp)
print(months[localtime.tm_mon - 1], localtime.tm_mday, localtime.tm_year)
