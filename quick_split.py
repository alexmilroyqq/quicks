
def list_splitter(lis, points, points_seperate_split=False):
    out = [[]]
    for i,e in enumerate(lis):
        if i in points and ((i-1 in points) and points_seperate_split):
            out.append([])
            
        if i in points or ((i-1 in points) and points_seperate_split):
            out.append([e])
        else:
            out[-1].append(e)
    if isinstance(lis, str):
        out = [''.join(e) for e in out]
    return out

def split_into_batchs(lis, batch_length):
    out = []
    for i,e in enumerate(lis):
        if i%batch_length==0:
            out.append([])
        out[-1].append(e)
    return out 

def split_into_bins(lis, func_bin):
    out = {}
    for e in lis:
        bin = func_bin(lis)
        out = out.get(bin, []) +[e]
    return out

def split_into_nestedlist(lis, func_newlement):
    for i, e in enumerate(lis):
        if i==0:
            out = [[e]]
        else:
            if func_newlement(e):
                out.append([e])
            else:
                out[-1].append(e)      
    return out

def split_bianry_function(lis, function):
    good, bad = [], []
    for e in lis:
        if function(e):
            good.append(e)
        else:
            bad.append(e)
    return good, bad

def split_intersections(lisa, lisb):
    only_a, both_ab = [], []
    for e in lisa:
        if e in lisb:
            both_ab.append(e)
        else:
            only_a.append(e)
    only_b = [e for e in lisb if e not in both_ab]
    return only_a, both_ab, only_b
    







if __name__ == '__main__': 
    aa = split_bianry_function([1,2,3,4,5,6,7,8,9,10,11,12], lambda x:x%2==0)
    print(aa)
    print(split_intersections([9,1,2,3,4,], [2,4,5,9]))
    
    
        
    
    lis = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')  
    
    batchs = split_into_batchs(lis,5)
    
    
    [['A', 'B', 'C', 'D', 'E'],
     ['F', 'G', 'H', 'I', 'J'],
     ['K', 'L', 'M', 'N', 'O'],
     ['P', 'Q', 'R', 'S', 'T'],
     ['U', 'V', 'W', 'X', 'Y'],
     ['Z']]
    
    
    # when single speech marks
    # do this future
    #tests
    msg = "   date:'2023-09-11'"
    out = ["   date:","'","2023-09-11","'",""] # 
    
    #tests
    msg = "   date:''"
    out = ["   date:","'","","'",""] # 
    
    
    
    #split_by_index
    #split_by_filter
    #split_by_batch    
        
    
    
    
    
    
    
    
    
    
    
    
    
    