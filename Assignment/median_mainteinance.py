import heapq
import time

def median_finder(array_input):
    min_arr = []
    max_arr = []
    answer = 0
    for num in array_input:
        if len(min_arr)<len(max_arr):
            heapq.heappush(min_arr, -heapq.heappushpop(max_arr, num))
            median = -min_arr[0]
        elif len(min_arr)>len(max_arr):
            heapq.heappush(max_arr, -heapq.heappushpop(min_arr, -num))
            median = -min_arr[0]
        else:
            heapq.heappush(max_arr, -heapq.heappushpop(min_arr, -num))
            median = max_arr[0]
        answer = answer + median
    
    return(answer%10000)
        

start_time = time.time()
with open("Assignment/Programming_Assignment_2_3.txt") as assignment:
    array = [int(line) for line in assignment]
print(median_finder(array))
print("ExecutionTime:",time.time()-start_time)