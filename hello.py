from datetime import datetime

now = datetime.now()
current_date = now.strftime('%d.%m.%Y')
current_time = now.strftime('%H:%M:%S')

message = f'Hello world, the current date is => {current_date} and the time is => {current_time}'
print(message)