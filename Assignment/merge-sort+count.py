def sort(arr, count=0):
    if len(arr) == 1:               #End Case
        return(arr, count)
    elif len(arr) == 2:             #End Case
        if arr[0]<arr[1]:
            return(arr, count)
        else:
            temp = arr[0]
            arr[0] = arr[1]
            arr[1] = temp
            count = count + 1
            return(arr, count)
    elif len(arr)>2:                #Merge Sort Algorithm
        A, count_left = sort(arr[0:len(arr)//2])
        B, count_right = sort(arr[len(arr)//2:len(arr)])
        count = count + count_left + count_right
        i = 0
        j = 0
        arr_length = len(arr)
        temp_arr = []
        for n in range(arr_length):
            if i == len(A):
                temp_arr.append(B[j])
                count = count + len(A) - i
                j = j + 1
            elif j == len(B):
                temp_arr.append(A[i])
                i = i + 1
            elif A[i] > B[j]:           #Comparing elements in two arrays, advancing one step for the smaller array
                temp_arr.append(B[j])
                count = count + len(A) - i
                j = j+1
            else:       
                temp_arr.append(A[i])
                i = i + 1            
        return(temp_arr, count)

assignment =  open("Assignment/Programming_Assignment_2.txt", "r")
array = assignment.read().splitlines()
array_int = [int(a) for a in array]
print(sort(array_int))
assignment.close()