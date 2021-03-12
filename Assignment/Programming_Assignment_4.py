import random

def random_contraction(arr):
    if len(arr) == 2:
        return(len(arr[0])-1)
    arr_indices = [i[0] for i in arr]
    
    #Choose two random points(u,v) which are connected to each other
    first_arr = arr[arr_indices.index(random.choice(arr_indices))]
    second_arr = arr[arr_indices.index(random.choice(first_arr[1:]))]
    first_point = first_arr[0]
    second_point = second_arr[0]
    
    #Merging the above two points together naming it first point 
    third_arr = [first_point]
    third_arr.extend(el for el in first_arr + second_arr if (el != first_point and el != second_point))
    
    #Changing the name of second point to first point in all arrays and thereby creating new array
    new_arr = [[first_point if el == second_point else el for el in x] for x in arr]
    new_arr[arr_indices.index(first_point)] = third_arr
    
    #Since the two point are merged deleteing the second point array
    del new_arr[arr_indices.index(second_point)]
    return(random_contraction(new_arr))
    


with open("Assignment/Programming_Assignment_4.txt") as assignment:
    array = [list(map(int, line.split())) for line in assignment] 

print(random_contraction(array))