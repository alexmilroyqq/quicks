
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
            

if False:
        #old version
    def hashfile(filename, parts = 60, seg_len = 2_000_000):
        '''
        Parameters
        ----------
        filename : Srt
            filepath of the file to find sha256[256],
            if file bigger than 120Mb finds hash of 60 
            smaller evenly spaced parts of it
    
        Returns
        -------
        out : Str
            hash string.
        '''
        import os, hashlib
        
        # def find_location_of_small_segemnts(parts, seg_len, data_len):
        #     parts2 = 2*parts
        #     value2 = data_len/parts2
        #     out = []
        #     for e in range(parts2+1):
        #         mid_float = e*value2
        #         start = int(mid_float - (seg_len*e/(parts2)))
        #         if e%2==1:
        #             out.append(start)
        #     return out
    
            
        def find_location_of_small_segemnts(parts, seg_len, data_len):
            parts2 = 2*parts
            value2 = data_len/parts2
            out = []
            for e in range(parts2+1):
                mid_float = e*value2
                #start = int(mid_float - (seg_len*e/(parts2)))
                start = int(mid_float - (seg_len/2)     )   
                if e%2==1:
                    out.append(start)
            return out
        
        size = os.path.getsize(filename)
        hasher = hashlib.sha256()
        
        if size<parts*seg_len:
            inds = [[0, size]]
        else:
            inds = find_location_of_small_segemnts(parts, seg_len, size)
        global inds_a
        inds_a = inds
        for s in inds:
            with open(filename, mode='rb') as fin:
                fin.seek(s)
                data_small = fin.read(seg_len)
                hasher.update(data_small)
        out = hasher.hexdigest()
        return out



