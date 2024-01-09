# -*- coding: utf-8 -*-
"""Created on Sun Nov 19 16:53:28 2023@author: alexm"""
from io import StringIO
import pandas as pd

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




 

 
def __create_dataframe():
    import pandas as pd
    csv_str = ''',Film,Genre,Lead Studio,Audience score %,Profitability,Rotten Tomatoes %,Worldwide Gross,Year,SEEN_(checkbox)
    0,Zack and Miri Make a Porno,Romance,The Weinstein Company,70,1.747541667,64,$41.94 ,2008,X
    1,Youth in Revolt,Comedy,The Weinstein Company,52,1.09,68,$19.62 ,2010,
    2,You Will Meet a Tall Dark Stranger,Comedy,Independent,35,1.211818182,43,$26.66 ,2010,
    3,When in Rome,Comedy,Disney,44,0.0,15,$43.04 ,2010,X
    4,What Happens in Vegas,Comedy,Fox,72,6.267647029,28,$219.37 ,2008,X
    5,Water For Elephants,Drama,20th Century Fox,72,3.081421053,60,$117.09 ,2011,X
    6,WALL-E,Animation,Disney,89,2.896019067,96,$521.28 ,2008,X
    7,Waitress,Romance,Independent,67,11.0897415,89,$22.18 ,2007,
    8,Waiting For Forever,Romance,Independent,53,0.005,6,$0.03 ,2011,
    9,Valentine's Day,Comedy,Warner Bros.,54,4.184038462,17,$217.57 ,2010,
    10,Tyler Perry's Why Did I get Married,Romance,Independent,47,3.7241924,46,$55.86 ,2007,X
    11,Twilight: Breaking Dawn,Romance,Independent,68,6.383363636,26,$702.17 ,2011,X
    12,Twilight,Romance,Summit,82,10.18002703,49,$376.66 ,2008,X
    13,The Ugly Truth,Comedy,Independent,68,5.402631579,14,$205.30 ,2009,X
    14,The Twilight Saga: New Moon,Drama,Summit,78,14.1964,27,$709.82 ,2009,X
    15,The Time Traveler's Wife,Drama,Paramount,65,2.598205128,38,$101.33 ,2009,X
    16,The Proposal,Comedy,Disney,74,7.8675,43,$314.70 ,2009,X
    17,The Invention of Lying,Comedy,Warner Bros.,47,1.751351351,56,$32.40 ,2009,X
    18,The Heartbreak Kid,Comedy,Paramount,41,2.129444167,30,$127.77 ,2007,X
    19,The Duchess,Drama,Paramount,68,3.207850222,60,$43.31 ,2008,X
    20,The Curious Case of Benjamin Button,Fantasy,Warner Bros.,81,1.78394375,73,$285.43 ,2008,X
    21,The Back-up Plan,Comedy,CBS,47,2.202571429,20,$77.09 ,2010,X
    22,Tangled,Animation,Disney,88,1.365692308,89,$355.01 ,2010,X
    23,Something Borrowed,Romance,Independent,48,1.719514286,15,$60.18 ,2011,
    24,She's Out of My League,Comedy,Paramount,60,2.4405,57,$48.81 ,2010,
    25,Sex and the City Two,Comedy,Warner Bros.,49,2.8835,15,$288.35 ,2010,
    26,Sex and the City 2,Comedy,Warner Bros.,49,2.8835,15,$288.35 ,2010,X
    27,Sex and the City,Comedy,Warner Bros.,81,7.221795791,49,$415.25 ,2008,
    28,Remember Me,Drama,Summit,70,3.49125,28,$55.86 ,2010,
    29,Rachel Getting Married,Drama,Independent,61,1.384166667,85,$16.61 ,2008,X
    30,Penelope,Comedy,Summit,74,1.382799733,52,$20.74 ,2008,X
    31,P.S. I Love You,Romance,Independent,82,5.103116833,21,$153.09 ,2007,
    32,Over Her Dead Body,Comedy,New Line,47,2.071,15,$20.71 ,2008,X
    33,Our Family Wedding,Comedy,Independent,49,0.0,14,$21.37 ,2010,X
    34,One Day,Romance,Independent,54,3.682733333,37,$55.24 ,2011,X
    35,Not Easily Broken,Drama,Independent,66,2.14,34,$10.70 ,2009,X
    36,No Reservations,Comedy,Warner Bros.,64,3.307180357,39,$92.60 ,2007,X
    37,Nick and Norah's Infinite Playlist,Comedy,Sony,67,3.3527293,73,$33.53 ,2008,X
    38,New Year's Eve,Romance,Warner Bros.,48,2.536428571,8,$142.04 ,2011,X
    39,My Week with Marilyn,Drama,The Weinstein Company,84,0.8258,83,$8.26 ,2011,X
    40,Music and Lyrics,Romance,Warner Bros.,70,3.64741055,63,$145.90 ,2007,X
    41,Monte Carlo,Romance,20th Century Fox,50,1.9832,38,$39.66 ,2011,X
    42,Miss Pettigrew Lives for a Day,Comedy,Independent,70,0.2528949,78,$15.17 ,2008,X
    43,Midnight in Paris,Romence,Sony,84,8.744705882,93,$148.66 ,2011,X
    44,Marley and Me,Comedy,Fox,77,3.746781818,63,$206.07 ,2008,X
    45,Mamma Mia!,Comedy,Universal,76,9.234453864,53,$609.47 ,2008,X
    46,Mamma Mia!,Comedy,Universal,76,9.234453864,53,$609.47 ,2008,X
    47,Made of Honor,Comdy,Sony,61,2.64906835,13,$105.96 ,2008,X
    48,Love Happens,Drama,Universal,40,2.004444444,18,$36.08 ,2009,X
    49,Love & Other Drugs,Comedy,Fox,55,1.817666667,48,$54.53 ,2010,X
    50,Life as We Know It,Comedy,Independent,62,2.530526316,28,$96.16 ,2010,X
    51,License to Wed,Comedy,Warner Bros.,55,1.9802064,8,$69.31 ,2007,X
    52,Letters to Juliet,Comedy,Summit,62,2.639333333,40,$79.18 ,2010,X
    53,Leap Year,Comedy,Universal,49,1.715263158,21,$32.59 ,2010,X
    54,Knocked Up,Comedy,Universal,83,6.636401848,91,$219 ,2007,X
    55,Killers,Action,Lionsgate,45,1.245333333,11,$93.40 ,2010,X
    56,Just Wright,Comedy,Fox,58,1.797416667,45,$21.57 ,2010,X
    57,Jane Eyre,Romance,Universal,77,0.0,85,$30.15 ,2011,X
    58,It's Complicated,Comedy,Universal,63,2.642352941,56,$224.60 ,2009,X
    59,I Love You Phillip Morris,Comedy,Independent,57,1.34,71,$20.10 ,2010,X
    60,High School Musical 3: Senior Year,Comedy,Disney,76,22.91313646,65,$252.04 ,2008,X
    61,He's Just Not That Into You,Comedy,Warner Bros.,60,7.1536,42,$178.84 ,2009,X
    62,Good Luck Chuck,Comedy,Lionsgate,61,2.36768512,3,$59.19 ,2007,X
    63,Going the Distance,Comedy,Warner Bros.,56,1.3140625,53,$42.05 ,2010,X
    64,Gnomeo and Juliet,Animation,Disney,52,5.387972222,56,$193.97 ,2011,X
    65,Gnomeo and Juliet,Animation,Disney,52,5.387972222,56,$193.97 ,2011,X
    66,Ghosts of Girlfriends Past,Comedy,Warner Bros.,47,2.0444,27,$102.22 ,2009,X
    67,Four Christmases,Comedy,Warner Bros.,52,2.022925,26,$161.83 ,2008,X
    68,Fireproof,Drama,Independent,51,66.934,40,$33.47 ,2008,X
    69,Enchanted,Comedy,Disney,80,4.005737082,93,$340.49 ,2007,X
    70,Dear John,Drama,Sony,66,4.5988,29,$114.97 ,2010,X
    71,Beginners,Comedy,Independent,80,4.471875,84,$14.31 ,2011,X
    72,Across the Universe,romance,Independent,84,0.652603178,54,$29.37 ,2007,X
    73,A Serious Man,Drama,Universal,64,4.382857143,89,$30.68 ,2009,X
    74,A Dangerous Method,Drama,Independent,89,0.44864475,79,$8.97 ,2011,X
    75,27 Dresses,Comedy,Fox,71,5.3436218,40,$160.31 ,2008,X
    76,(500) Days of Summer,comedy,Fox,81,8.096,87,$60.72 ,2009,X'''

    df = pd.read_csv(StringIO(csv_str),index_col=0)
    df.iloc[:,-1] = df.iloc[:,-1].fillna('')
    return df

    

image = __create_image()
film_df = __create_dataframe()









    
