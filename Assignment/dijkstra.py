def dijkstra(input_dict, processed_vert, A, question):
    X = [processed_vert]
    A[processed_vert] = 0
    while len(X) != len(input_dict):
        min_calc_array = []
        for node in X:
            v = node
            w_tentative = [items[0] for items in input_dict[node] if items[0] not in X]
            length_values = [items[1] for items in input_dict[node] if items[0] not in X]
            if len(length_values):
                min_length_value = min(length_values)
                w = w_tentative[length_values.index(min_length_value)]
                min_calc_array.append([v,w,min_length_value])
            else:
                continue
        greedy_values = [A[el[0]]+el[2] for el in min_calc_array]
        min_greedy_value = min(greedy_values)
        min_greedy_value_index = greedy_values.index(min_greedy_value)
        w_star = min_calc_array[min_greedy_value_index][1]
        X.append(w_star)
        A[w_star] = min_greedy_value
    return([A[i] for i in question])

question  = [7,37,59,82,99,115,133,165,188,197]
with open("Assignment/Programming_Assignment_2_2.txt") as assignment:
    split_lines = [line.split() for line in assignment]
    array = [[[int(a) for a in item.split(",")] for item in items] for items in split_lines]
    dict_items = [[items for items in array[i]] for i in range(len(array))]
    input_dict = {array[i][0][0]:dict_items[i][1:] for i in range(len(array))}
    A = [1000000]*(len(input_dict)+1)
    print(dijkstra(input_dict,1,A,question))
#print(dict.keys())