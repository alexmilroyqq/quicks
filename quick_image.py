# -*- coding: utf-8 -*-
"""Created on Mon Oct  9 12:10:06 2023@author: alexm"""

import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

def image_show(*imgs, titles=None):
    def convert_to_image(arg):
        out = arg
        if isinstance(arg, str):
            fp1 = arg.lower()
            assert fp1.endswith('.jpg') or fp1.endswith('.png') 
            out = plt.imread(arg)
        assert not isinstance(arg, (int, dict, list, float))
        return out
    

    
    
    if isinstance(imgs, dict):  
        titles = list(imgs.keys())
        imgs = list(imgs.values())
        
    imgs = [convert_to_image(fp) for fp in imgs]  
    imgs = [img.squeeze() for img in imgs ]   
    
    ncols = len(imgs)    
    fig, axs = plt.subplots(nrows=1, ncols=ncols, gridspec_kw={'wspace':0, 'hspace':0},figsize=(8, 8), squeeze=True)
    
    if isinstance(titles, str) and len(imgs)>1:
        fig.suptitle(titles, fontsize=13)
        titles = None
    
    axs = axs if ncols>1 else [axs]
    for i, (image, ax) in enumerate(zip(imgs, axs)):
        ax.axis("off")
        if not titles is None:
            ax.set_title(titles[i])
        ax.imshow(image)

color_dict = {'red':(255,0,0), 'green':(0,255,0), 'blue':(0,0,255),
              True:(0,255,0), False:(255,0,0), 'white':(255, 255, 255),
              'yellow':(255,255,0), 
              'black':(0,0,0)}


def add_box_to_image(fimg, box, clr = 'red'):
    # (0,0) is top left (up-down, left-right)
    clr = color_dict.get(clr, clr)
    if isinstance(fimg, str):
        pimg = Image.open(fimg)
        data = np.asarray(pimg)
    elif isinstance(fimg, np.ndarray):
        data = fimg
    else:
        assert False, 'Bad type'
    data = data*(255/data.max())
    
    if len(data.shape)==2:
        data = np.stack([data]*3,2)
    data2 = data.copy()
    x1,x2,y1,y2 = box['x'], box['x']+box['w'], box['y'], box['y']+box['h']
    
    t = 1 # thickness
    data2[y1-t:y1+t,x1:x2,:]=clr
    data2[y2-t:y2+t,x1:x2,:]=clr
    data2[y1:y2,x1-t:x1+t,:]=clr
    data2[y1:y2,x2-t:x2+t,:]=clr
    return data2






def image_show_popout(img):
    from PIL import Image
    import numpy as np
    
    img = (img-img.min())/(img.max()-img.min())
    img = (255*img).astype(np.uint8)
    if len(img.shape)==2:
        img = np.stack((img,)*3, axis=2)
        
    pimg = Image.fromarray(img,'RGB')
    pimg.show()
   
    
    # #dont think i need this now
    # sz = img3.shape
    # new_img = Image.new('RGB', sz[:2])
    
    # for i in range(sz[0]):
    #     for j in range(sz[1]):
    #         r, g, b = img3[i,j,:]
    #         new_img.putpixel((i, j), (r, g, b))
    # new_img.show()
    
    
    







    