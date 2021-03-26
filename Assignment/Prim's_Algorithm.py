import heapq
def prim(arr, processed_vert, num_nodes):
    X = [processed_vert]
    total_length = 0
    while len(X) != num_nodes:
        v = []
        for nodes in X:
            arr_1 = []
            arr_1 = [[el[2], el[1], el[0]] for el in arr[1:] if el[0] == nodes and el[1] not in X]
            arr_1.extend([[el[2],el[0],el[1]] for el in arr[1:] if el[1] == nodes and el[0] not in X])
            heapq.heapify(arr_1)
            if arr_1 != []:
                heapq.heappush(v,arr_1[0])
            else:
                continue
        X.append(v[0][1])
        print(len(X))
        total_length = total_length + v[0][0]
    return(total_length)

with open("Assignment/Programming_Assignment_3_1_3.txt") as assignment:
    arr = [list(map(int, line.split())) for line in assignment]
    print(prim(arr[1:], 1, arr[0][0]))
    