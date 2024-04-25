import datetime

info = datetime.datetime.now()
date = info.strftime('%d/%m/%Y')
hour = info.strftime('%H:%M')
print(f"Data:", date)
print(f"Hora:", hour)