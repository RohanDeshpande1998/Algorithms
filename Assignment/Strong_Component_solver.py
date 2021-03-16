
def kosaraju(array):
    n = max(map(max, array))
    stack_arr = DFS(array,[False]*n,[i for i in range(n,0,-1)])
    answer = DFS(array,[False]*n, reversed(stack_arr),[], i = 1, answer = [])
    return(answer)

def DFS(array, bool_arr, start_vertex, stack_arr = [], i = 0, answer = []):
    for num in start_vertex:
        print(num)
        if bool_arr[num-1] == False:
            bool_arr[num-1] = True
            elements = [arr[i] for arr in array if arr[i-1]==num]
            [DFS(array,bool_arr,[ele],stack_arr, i) for ele in elements if bool_arr[ele-1] == False]
            stack_arr.append(num)
    if i == 1:
        return stack_arr
    else:
        return(stack_arr)
                     
with open("Assignment/Programming_Assignment_2_1.txt") as assignment:
    array = [tuple(map(int, line.split())) for line in assignment]
    set_arr = set(array)
#array = (map(str.strip, open("Assignment/kosaraju_test_case_1.txt")))
    print(kosaraju(array))
    #for arr in array:
    #    if arr[1] == 6:
    #        print(arr[0]) 