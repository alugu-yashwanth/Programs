import time
times=time.strftime("%H:%M:%S")
print(time)
# times=
if(int(time.strftime('%H'))<12):
    print("Good Morning")
elif(int(time.strftime('%H'))<16):
    print("Good Afternoon")
elif(int(time.strftime('%H'))>=16 and int(time.strftime('%H'))<20):
    print("Good Evening")
else:
    print("Good Night")