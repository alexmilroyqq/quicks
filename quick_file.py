# -*- coding: utf-8 -*-
"""Created on Tue Nov  7 14:18:58 2023@author: alexm

is_files_identical(fp1,fp2)
find_identical_files(fps)
remove_empty_folders(folderpaths)

"""
import os

# from quick_file import read_textfile, save_textfile, modify_textfile, get_files, get_subfiles, create_files_move_dic

def __get_file_extension(filepath):
    folder, filename = os.path.split(filepath)
    filename_parts = filename.rsplit('.',1)
    if len(filename_parts)==1:
        return ''
    return '.'+filename_parts[1]    

__function_type = type(lambda : None)


def read_textfile(fp):
    if isinstance(fp, (list, tuple)):
        return {f:read_textfile(f) for f in fp}
    elif isinstance(fp, str): 
        with open(fp) as fo:
             return fo.readlines()


def save_textfile(fp, text):
    if isinstance(text, (list, tuple)):
        if not all([('-'+l)[-1]=='\n' for l in text ]):
            text = [l+'\n' for l in text]
        text = ''.join(text)
    
    with open(fp, 'w') as fo:
        fo.write(text)


def modify_textfile(fp, func_line=None, func_text=None):
    text = read_textfile(fp)
    if func_line is not None:
        try:
            text = [func_line(i,l) for i,l in enumerate(text)]
        except:
            text = [func_line(l) for l in text]            
    if func_text is not None:
        text = func_text(text)
    save_textfile(fp, text)
    









def get_subfiles(folder, except_files = None, except_folders = None, just='files'):
    out = []
    for (dirpath, dirnames, filenames) in os.walk(folder):
        out.extend([os.path.join(dirpath,f) for f in filenames])

    if except_files is not None:
        out = [l for l in out if not os.path.split(l)[-1] in except_files]

    if except_folders is not None:
        out0 = []
        for filepath in out:
            _, *parents, fn = filepath.removeprefix(folder).split('\\')
            if not len(set(except_folders).intersection(parents))>0:
                out0.append(filepath)
        out = out0
    return out

def get_files(folder, include_folders=True):
    files = [os.path.join(folder, f) for f in os.listdir(folder)]
    if not include_folders:
        files = [f for f in files if os.path.isfile(f)]
    return files

#------------------------------------------------------------------------------
# def remove_empty_folders():
#     pass


# def remove_all_files_from_folder(path, except_files = None, except_folders = None):
#     # 
#     except_files = except_files if except_files is not None else []
#     except_folders = except_folders if except_folders is not None else []    
        
#     for (dirpath, dirnames, filenames) in os.walk(path):
#         dirpath2 = (dirpath.removeprefix(path)).strip('\\')
#         parents = dirpath2.split('\\')
#         _, parent = os.path.split(dirpath)
        
#         protected_parents = set(except_folders).intersection(parents)
#         if len(protected_parents)>0:
#             continue
        
#         for filename in filenames:
#             filepath = os.path.join(dirpath, filename)
#             if filename not in except_files:
#                 os.remove(filepath)


def create_files_move_dic(filepaths, dst_folder, prefix=''):
    out = {}
    for filepath in filepaths:
        filename = os.path.split(filepath)[-1]
        out[filepath] = os.path.join(dst_folder, prefix+filename)
    return out


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


def quick_shortcut_lnk_find(shortcut_fp):
    import win32com.client
    shell = win32com.client.Dispatch('WScript.Shell')
    shortcut = shell.CreateShortcut(shortcut_fp)
    return shortcut.Targetpath
 





















if False:
    fp = r"C:\Users\alexm\Desktop\sdfsadf sdf.txt"
    text = read_textfile(fp)
    text2 = ['>>'+l for l in text]
    fp2 = fp.replace('.', '(1).')
    save_textfile(fp2, text2)
if False:
    modify_textfile(r"C:\Users\alexm\Desktop\sdfsadf sdf.txt", lambda i,x: ('<< ' if i==0 else '>> ')+x)
    modify_textfile(r"C:\Users\alexm\Desktop\sdfsadf sdf.txt", lambda x: '-- '+x)
    modify_textfile(r"C:\Users\alexm\Desktop\sdfsadf sdf.txt", None, lambda x:[l for l in x if 'a' not in l])    

if False:
    files = get_files(r"C:\Users\alexm\Desktop\DATASETS")
    files2 = get_files(r"C:\Users\alexm\Desktop\DATASETS", False)
    files3 = get_subfiles(r"C:\Users\alexm\Desktop\DATASETS")
    files4 = files3[-10_000:]





def find_textfiles(filepaths, func=None, extension='.txt'):
    assert 'IN DEVELOPMENT'
    if isinstance(filepaths, str):
        filepaths = get_subfiles(filepaths)    
    elif not isinstance(filepaths, (list,tuple)):
        assert 'Unexpected filetype'
    if extension is not None:
        if isinstance(extension, str):
            extension = [extension]
        if not isinstance(extension, (tuple, list)):
            assert 'Unexpected filetype'
        filepaths = [filepath for filepath in filepaths if __get_file_extension(filepath) in extension]
    if isinstance(filepaths, __function_type):
        pass
           



if False:
    
    
    
    
    
    # Find all text files in desktop file, and read them in a dict
    print('Find all text files')

    folder = r"C:\Users\alexm\Desktop"
    files = get_subfiles(folder)
    files = [f for f in files if __get_file_extension(f) in ['.txt']]
    
    files2 = files
    files2 = [f for f in files2 if not f.startswith(r'C:\Users\alexm\Desktop\DATASETS\GRAZPEDWRI-DX-Wrist_Fractures\folder_structure\yolov5\labels') ]
    files2 = [f for f in files2 if not f.startswith(r'C:\Users\alexm\Desktop\delete after 2023-01-01\quick_wrist_run - Copy\labels\train') ]
    files2 = [f for f in files2 if not f.startswith(r'C:\Users\alexm\Desktop\delete after 2023-01-01\quick_wrist_run - Copy\labels\val') ]
    assert len(files2)<200, 'Too many files'
    
    text_files = read_textfile(files2)
    
    
    
















 
    
    