def sort(arr):
    if len(arr) == 1:               #End Case
        return(arr)
    elif len(arr) == 2:             #End Case
        if arr[0]<arr[1]:
            return(arr)
        else:
            temp = arr[0]
            arr[0] = arr[1]
            arr[1] = temp
            return(arr)
    elif len(arr)>2:                #Merge Sort Algorithm
        A = sort(arr[0:len(arr)//2])
        B = sort(arr[len(arr)//2:len(arr)])
        i = 0
        j = 0
        arr_length = len(arr)
        temp_arr = []
        for n in range(arr_length):
            if i == len(A):
                temp_arr.append(B[j])
                j = j + 1
            elif j == len(B):
                temp_arr.append(A[i])
                i = i + 1
            elif A[i] < B[j]:       #Comparing elements in two arrays, advancing one step for the smaller array
                temp_arr.append(A[i])
                i = i + 1
            else:
                temp_arr.append(B[j])
                j = j+1
        return(temp_arr)