# -*- coding: utf-8 -*-
"""Created on Tue Nov  7 14:18:58 2023@author: alexm"""
import os

# from quick_file import read_textfile, save_textfile, modify_textfile, get_files, get_subfiles, create_files_move_dic

def read_textfile(fp):
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

def create_files_move_dic(filepaths, dst_folder, prefix=''):
    out = {}
    for filepath in filepaths:
        filename = os.path.split(filepath)[-1]
        out[filepath] = os.path.join(dst_folder, prefix+filename)
    return out

def get_subfiles(folder, except_files = None, except_folders = None):
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

# def get_subfiles(folder):
#     out = []
#     for (dirpath, dirnames, filenames) in os.walk(folder):
#         out.extend([os.path.join(dirpath,f) for f in filenames])  
#     return out
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



    
    
    