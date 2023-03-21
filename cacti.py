def cacti_number(func):
    num = 0
    rows = range(len(func))
    cols = range(len(func[0]))
    
    
    for i in rows:
        for j in cols:
            if(func[i][j] != 1):
                if((i -1 >= 0 and func[i-1][j] == 0) or i -1 < 0):
                    if((j-1 >= 0 and func[i][j-1]==0) or j-1 < 0):
                        if((j+1 < len(func[0]) and func[i][j+1] == 0) or j+1 >= len(func[0])):
                            if((i+1<len(func[0]) and func[i+1][j] == 0) or i+1  >= len(func[0])):
                                func[i][j] = 1
                                num += 1
    return num
                     
