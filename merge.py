def merge(list1, list2):
    i=0
    j=0
    merged = []
    while i<len(list1) and j<len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged
print(merge([1,3,5,7],[2,4,6]))
print(merge([1,2,3,5],[1,2,4,5,6]))
print(merge([1,5,9],[]))
