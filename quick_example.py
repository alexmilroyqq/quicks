# -*- coding: utf-8 -*-
"""Created on Sun Nov 19 16:53:28 2023@author: alexm"""


def __create_image():
    import numpy as np
    img = np.zeros([400,400,3])
    
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            #red square
            if 190>i>10:
                if 190>j>10:
                    img[i,j,0] = 1
                    
            #blue circle
            if (i-100)**2 +(j-300)**2 <90**2:
                img[i,j,2] = 1
                continue                 
            
            
            #Add Grid
            #white lines Horizontal
            if i in list(range(50,img.shape[0],50))+list(range(51,img.shape[0],100)):
                img[i,j,:] = 1                 
                continue
            #white lines Vertical            
            if j in range(50,img.shape[1],50):
                img[i,j,:] = 1
                continue                
                
                    
            #green traingle
            n = (3/2)**0.5
            i2, j2 = i-250, j-300        
            if i<350:
                if i2+(n*j2)>0:
                    if i2-(n*j2)>0:
                        img[i,j,1] = 1
                        continue
    
            #small colored boxs
            if 390>i>370 and 360>j>240:
                for ii,cc in enumerate([(1,1,0), (0,1,1), (1,0,1), (1,1,1),(1,0.5,0),(0,1,0.5)]):
                    if (j-240)//20==ii:
                        img[i,j,:]=cc
                        
            #black-white chess board spectrum
            if 219>i>205:        
                if 270>j>205:
                    img[i,j,:] = (i+j)%2==0 if j<240 else (j-240)/30 
                    continue                    
    
    
            # yellow point spread function
            z = 30/(30+(i-250)**2 +(j-245)**2)
            if z>0.01:
                img[i,j,:2] = z      
    
            # spectrum square
            if 110>i>90:        
                if 140>j>60:
                    img[i,j,:] = ((i-90)/(110-90), (j-60)/(140-60),0)                  
            
            #spectrum cross
            if 390>i>210 and 190>j>10:
                if abs((i-300)+(j-100))<10 or abs((i-300)-(j-100))<10:
                    a = max(0,(60-abs(j-10))/60)+max(0,(60-abs(j-190))/40)
                    b = max(0,(60-abs(j-70))/60) 
                    c = max(0,(60-abs(j-130))/60)
                    img[i,j,:] = (a,b,c)
                    
    return img

image = __create_image()


    
