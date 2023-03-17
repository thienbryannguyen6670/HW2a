def merge(list1, list2):
    #initialize 2 pointers to start of both lists
    i=0
    j=0
    #created an empty list to store the merged list.
    merged = []
    #while both pointers are within their respectve lists
    while i<len(list1) and j<len(list2):
        #if the current element in list1 is smaller or equal to the one in list2
        if list1[i] <= list2[j]:
            #add it to the merged list
            merged.append(list1[i])
            #now,move the pointer to the next element in list1
            i += 1
        #else if the current element in list2 is smaller
        else:
            #adding it to the merged list
            merged.append(list2[j])
            j += 1
    #at this point, one of tge pointers has reached the end of its list
    #now, we need to add the remaining elements from the other list to the merged list
    #adding the remaining elements of list1 and list2 if any
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    #finally return the merged list
    return merged
#sample run
print(merge([1,3,5,7],[2,4,6]))
print(merge([1,2,3,5],[1,2,4,5,6]))
print(merge([1,5,9],[]))
