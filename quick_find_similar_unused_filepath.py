

def quick_find_similar_unused_filepath(fp, maker=None, limit=100 ):
    import os

    if maker is None:
        # add maker in before . in filename if it has one or stick it on the end
        marker= '<>' 
        folder, filename = os.path.split(fp)
        fpa = filename.rsplit('.', 1)
        if len(fpa)<2:
            fpa.append('')
        else:
            fpa[1]='.'+fpa[1]
        fp = os.path.join(folder, marker.join(fpa))

    assert fp.count(marker)==1
    import itertools
    for i in itertools.count():
        replacement = '' if i == 0 else f'({i})'
        new_fp = fp.replace(marker, replacement)
        if not os.path.isfile(new_fp):
            return new_fp
        if i ==limit:
            return



 

