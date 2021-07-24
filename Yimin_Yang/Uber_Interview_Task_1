"""Q1"""
def maxMinSegment(arr, m):
    if m == 1:
        return max(arr)
    else:
        if len(set(arr)) == 1:
            return arr[0]
        else:
            list = []
            # for i in range(len(arr)):
            while len(arr) >= m:
                temp = []
                # for i in range(len(arr)):
                for j in range(m):
                    temp.append(arr[j])
                    if j + 1 == m:
                        del (arr[0])
                list.append(temp)
            min_num = []
            for i in list:
                min_num.append(min(i))
            return max(min_num)
            
            
 def maxmin(arr, m):
    if len(arr) == 1:
        return arr[0]
    if m == len(arr):
        return min(arr)
    min_value = []
    for i in range(0, len(arr) - m + 1):
        temp_arr = arr[i:i + m]
        min_value.append(min(temp_arr))
    return max(min_value)
