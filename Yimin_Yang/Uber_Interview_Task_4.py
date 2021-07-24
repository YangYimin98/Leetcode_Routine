def transformed_markers(arr):
    begin_index = arr[0]
    end_index = arr[-1]
    markers = {i for i in range(begin_index, end_index+1)}
    print(markers)
    return markers


def easyCountUber(coordinates):
    markers_set = set()
    for arr in coordinates:
        markers_set = markers_set | transformed_markers(arr)
    return len(markers_set)
    
    
 """My approach"""


def approach3(coordinates):
    coordinates = sorted(coordinates, key=lambda x: x[0])
    union = []
    for coordinate in coordinates:
        # empty list or no interval between two connected list
        if not union or union[-1][1] < coordinate[0]:
            # compare the right value of the last list with left value of next list
            union.append(coordinate)

        else:
            union[-1][1] = max(union[-1][1], coordinate[1])  # interval, get union
            print(union[-1][1])
    list_width = []
    for i in union:
        sum1 = i[1] - i[0] + 1  # find all the width for each list
        list_width.append(sum1)
    return sum(list_width)


coords = [[2, 4], [60, 80], [1, 3]]
print(approach3(coords))
