from operator import itemgetter

def greedy_min_weighted_sum(arr):
    length = 0
    weight = 0
    weighted_answer = []
    temp = []
    new_list = [[el[0],el[1],el[0]/el[1]] for el in arr[1:]]     #change the way to schedule job(subtraction or division[currently division])
    final_list = []
    new_list.sort(key=itemgetter(2), reverse = True)
    first_el = new_list[0][2]
    for el in new_list:
        if el[2] == first_el:
            temp.append(el)
        else:
            final_list.extend(sorted(temp,key = itemgetter(0),reverse = True))
            temp = []
        first_el = el[2]
    for el in final_list:
        weight = el[0]
        length = length + el[1]
        weighted_answer.append(weight*length)
        
    return(sum(weighted_answer))


with open("Assignment/Programming_Assignment_3_1_1.txt") as assignment:
    array = [list(map(int, line.split())) for line in assignment]
    print(greedy_min_weighted_sum(array))