import time
start_time = time.time()
n = float(input("enter time sleep value:"))
time.sleep(n)
end_time = time.time()
print("Elapsed time:%0.2f"%(end_time-start_time))