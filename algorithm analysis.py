import time
import random 
import matplotlib.pyplot as plt

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

    
arr = [1]
target = 30
result = linear_search(arr, target)
print("Linear Search Result:",result)

def binary_search(arr, target): 
    low, high = 0, len(arr) - 1
    while low <= high:

        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [1]
target = 30
result = linear_search(arr, target)
print("Binary Search Result:",result)

def measure_time(func, arr, target):
    start_time = time.perf_counter()
    func(arr, target)
    end_time = time.perf_counter()
    return end_time - start_time


#sorted_arr = sorted(arr)
#binary_time = measure_time(binary_search, sorted_arr, target)
#print("Binear Search Time:",binary_time)

input_size = [1000,50000,100000,500000,1000000]
linear_time = []
binary_time = []

for size in input_size:
    arr = [random.randint(1,100000) for _ in range(size)]
    target = random.choice(arr)
    sorted_arr = sorted(arr)

    linear_time.append(measure_time(linear_search, arr, target))
    binary_time.append(measure_time(binary_search, sorted_arr, target))
   

plt.figure(figsize=(10,6))
plt.plot(input_size, linear_time, label="Linear Search",marker="o")
plt.plot(input_size, binary_time, label="Binary_search",marker="x")
plt.title("Runtime Comparison : Linear Search vs Binary Search")
plt.xlabel("Input Sizr(n)")
plt.ylabel("Runtime (seccord)")
plt.legend()
plt.grid()
plt.show()
