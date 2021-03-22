def two_sum(arr_que):
    answer = 0
    question = list(range(-10000, 10001,1))
    arr_que.sort()
    i = 0
    j = len(arr_que) - 1
    while(i<j):
        if arr_que[i]+arr_que[j]<-10000:
            i = i + 1
        elif arr_que[i]+arr_que[j]>10000:
            j = j - 1
        else:
            while(arr_que[i]+arr_que[j] > -10000):
                if arr_que[i]+arr_que[j] in question:
                    answer = answer + arr_que[i]+arr_que[j]
                    question.remove(arr_que[i]+arr_que[j])
                j = j - 1    
    return(answer)


with open("Assignment/Programming_Assignment_2_4.txt") as assignment:
    array = [int(line) for line in assignment]
    print(two_sum(array))

