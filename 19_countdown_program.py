import time

# time.sleep(3)  #  It will start the program after 3 seconds passed.

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x /60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02} {seconds:02}")
    time.sleep(1)

print("Time is UP!")