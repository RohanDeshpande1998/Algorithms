def greedy_min_weighted_sum(jobs):
    finish_time = 0
    weighted_sum = 0
    priority = [(item[0]/item[1], item[0]) for item in jobs]
    order = sorted(range(len(priority)), key = priority.__getitem__)
    order.reverse()
    for i in order:
        
        finish_time += jobs[i][1]
        weighted_sum += finish_time*jobs[i][0]
        
    return weighted_sum


with open("Assignment/Programming_Assignment_3_1_1.txt") as assignment:
    array = [list(map(int, line.split())) for line in assignment]
    print(greedy_min_weighted_sum(array[1:]))