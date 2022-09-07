# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 18:29:14 2022

@author: G604291
"""
from PIL import Image
import numpy as np
import random as rand
from random import randrange
from random import randint, choice
 
%matplotlib qt 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2 as cv
 
 


class image:
    data=0
    
    def __init__(self, name, h, w):
        self.name = name
        self.h = h
        self.w = w
         

    def random_RGB(self):
        
        self.w, self.h = 256, 256
        
        self.name='random'
        global data
        data = np.zeros((self.h, self.w, 3), dtype=np.uint8)
        for i in range(self.w):
            for j in range(self.h):
                data[i,j ] = [randrange(255), randrange(255), randrange(255)] # red patch in upper left
        image_test = Image.fromarray(data, 'RGB')
        image_test.show()
        return data
         
        
    def random_grey(self):
        w, h = 256, 256
        self.name='random_grey'
        global data
        data = np.zeros((h, w, 2), dtype=np.uint8)
        for i in range(256):
            for j in range(256):
                data[i,j ] = [randint(0, 500) ] # red patch in upper left
        print(data[:])
        image_test = Image.fromarray(data)
        image_test.show()

        
        


plt.show()
image_test = image('image_test',1024,1024)

a=image_test.random_grey()
#image_test.random_RGB()

 
x=[]
y=[]
z=[]

# filter the noise image
kernel = np.ones((5,5),np.float32)/25
data = cv.filter2D(data,-1,kernel) 


# 2D to 3D 
for i in range(256):
     for j in range(256):
         
         x.append(i)
         y.append(j)
         z.append(data[i,j,0] )
#


        
      
        
          






fig = plt.figure()
ax = plt.axes(projection='3d')



# Data for a three-dimensional line
 

 
ax = plt.axes(projection='3d')

#ax.scatter(x, y, z, c=z,linewidth=0.1)


ax = plt.axes(projection='3d')
ax.plot_trisurf(x, y, z,
                cmap='viridis', edgecolor='none');
ax.set_title('surface');


ax.view_init(200, 35)
plt.show()
fig


# # test 3D
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot(data[i,j,0],data[i,j,1],z_map)

# plt.show()

 



# w, h = 1024, 1024
# data = np.zeros((h, w, 3), dtype=np.uint8)
# for i in range(1024):
#     for j in range(1024):
#         data[i,j ] = [randrange(255), randrange(255), randrange(255)] # red patch in upper left
# img = Image.fromarray(data, 'RGB')
# img.save('my.png')
# img.show()