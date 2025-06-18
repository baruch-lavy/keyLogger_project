import time
from time import ctime

print(time.time())
print(ctime())
print(type(ctime()))

# timer=''
# for char in ctime():
#     if char in '1234567890: ':
#         timer+=char
# print(timer)

def list_of_time_changes(amount_of_minutes):
    running=True
    t=int(time.time())
    minute_list=[ctime()]
    while running:
        if t+60 <= int(time.time()):
            minute_list.append(ctime())
            t = int(time.time())
        if len(minute_list)==amount_of_minutes:
            running=False
    return minute_list
#testing def
time_list=list_of_time_changes(3)
print(time_list)