def sort_dictionary(_dict):
    
    sorted_keys = sorted(_dict.keys(), key = lambda x: _dict[x][1])
    
    result = []
    
    for k in sorted_keys:
        
        _tuple = (k,_dict[k][0])
       
        result.append(_tuple)
        
    return result
    

#_dict = {'Tom': (5464512, 24), 'Sara': (5446987, 32), 'Mary': (1557896, 20)}

result = sort_dictionary(_dict)

print(result)
