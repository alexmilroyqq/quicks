assert False "Not Finshed yet"


def quick_hash(filepath=None, data=None, quick=True, no_parts = 60, segment_size = 2_000_000, verbose=False):
    def vprint(*args, **kwargs):
        if verbose:
            print(*args, **kwargs)
    
    import os, hashlib
    
    def read_file_section(filepath, start=None, segment_size=-1):    
        with open(filepath, mode='rb') as fo:
            if start is not None:            
                fo.seek(start)
            return fo.read(segment_size)
    
    def get_data_generator(filepath, inds=None, segment_size=None):
        if inds is None:
            yield read_file_section(filepath)
        else:
            for s in inds:
                yield read_file_section(filepath, s, segment_size)
                
    def calcuate_start_of_each_part(no_parts, segment_size, file_size):
        def get_part_start(part_i, no_parts, segment_size, file_size):
            return int((file_size*(((1+2*part_i)/no_parts)) -segment_size)/2)
        return tuple([get_part_start(i, no_parts, segment_size, file_size) for i in range(no_parts)])
    
    assert calcuate_start_of_each_part(2, 0, 100) == (25, 75)
    assert calcuate_start_of_each_part(2, 10, 100) == (20, 70)   
    assert calcuate_start_of_each_part(4, 25, 100) == (0, 25, 50, 75)          
    assert (filepath, data).count(None)==1
    
    if filepath is not None:
        min_size = no_parts*segment_size
        file_size = os.path.getsize(filepath)
        if file_size<min_size or not quick:
            vprint('not quick if large, small')  
            datas = get_data_generator(filepath)
        else:
            vprint('large mode, quick if large, lots of blocks')          
            part_starts = calcuate_start_of_each_part(no_parts, segment_size, file_size)
            global inds_b
            inds_b = part_starts
            datas = get_data_generator(filepath, part_starts, segment_size)
            
    if data is not None:
        datas = [data]
        
    hasher = hashlib.sha256()             
    for data_segement in datas:
        hasher.update(data_segement)
    out = hasher.hexdigest()
    return out        
            

            
        

def quick_identical_files_check(fp1, fp2):
    return quick_hash(fp1)==quick_hash(fp2)






def quick_identical_files_find_all2(filepaths):
    import os    
    def group_items(items, function):
        out = {}
        for item in items:
            key = function(item)
            out[key] = out.get(key, [])+[item]
        return out    
    
    out = []
    for filesize, filepaths1 in group_items(filepaths, os.path.getsize).items():
        if len(filepaths1)>1:
            for hash_code, filespaths2 in group_items(filepaths1, quick_hash).items():
                if len(filespaths2)>1:
                    out.append(filespaths2)
    return out
        



def quick_identical_files_find_all(filepaths):
    import os
    out = {}
    for filepath in filepaths:
        size = os.path.getsize(filepath)
        out[size] = out.get(size, [])+[filepath]
    out2 = {k:v for k,v in out.items() if len(v)>1}
    out3 = []
    for k,vs in out2.items():
        out4 = {}
        for v in vs:
            hash_ = quick_hash(filepath=None)
            out4[hash_] = out4.get(hash_, [])+[v]  
        for k,v in out4.items():
            if len(v)>1:
                out3.append(v)
    return out3
        
        
folder = r"C:\Users\Alexm\Desktop\EasyImportPython"
filepaths0 = os.listdir(folder)
filepaths = [os.path.join(folder,e) for e in filepaths0]
          
    
 


