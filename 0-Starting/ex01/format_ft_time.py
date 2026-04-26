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

# segundos desdo Unix epoch
timestamp = time.time()

# ,: ativa a virgula na separação
# .4: devine a precisão
# f: inpede que ele seja convertido para a notação cientifica, forçando o formato decimal fixo
print(f"Seconds since January 1, 1970: {timestamp:,.4f}", end="")
# sem o f no final, .3 siginifca 3 algarismos significativos no total
print(f" or {timestamp:.3} in scientific notation")

#converte timestamp para uma struct_time
# time.struct_time(tm_year=2023, tm_mon=10, tm_mday=15, tm_hour=14, 
#                  tm_min=30, tm_sec=45, tm_wday=0, tm_yday=288, tm_isdst=1)
struct_time = time.localtime(timestamp)
print(months[struct_time.tm_mon - 1], struct_time.tm_mday, struct_time.tm_year)
