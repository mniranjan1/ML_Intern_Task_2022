"""Importing Libraries"""
import cv2
import numpy as np

"""Sorting Function"""
def sorted_list(x,lst1):
    lst2 = []
    for i in x:
        for j in lst1:
            if(j.shape == i):
                lst2.append(j)
    return(lst2)

"""Inputting the image"""
image = cv2.imread('shapes.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

"""Edge Detection"""
canny = cv2.Canny(gray, 130, 255,3)
cnts = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

"""Analayzing and manually detecting the lines with help of edge dectection"""
cnt = cnts[0][4]
cnts1 = cnts[0][10]
cnts2 = cnts[0][17]
cnts3 = cnts[0][22]

"""Sorting lines in terms of their length with help of their shapes """
lst1= [cnt,cnts1,cnts2,cnts3]
lst = [cnt.shape,cnts1.shape,cnts2.shape,cnts3.shape]
sorted_values =sorted(lst, key=lambda x: x[0], reverse=False)
lst2 = sorted_list(sorted_values,lst1)

"""Assigning numbers to the rectangles with respect to the length of lines inside the rectangle"""
for contours in lst2:
    cv2.drawContours(image,[contours], 0, (0,255,0), 3)
    index = lst2.index(contours) + 1
    average = contours.mean(axis=0)
    if index == 1:
        extend = -20
    elif index == 2:
        extend = 50
    elif index == 3:
        extend = -25
    else:
        extend = 30
    cv2.putText(img=image, text=str(index), org=(int(average[0][0]),int(average[0][1])+extend), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0,0,255),thickness=1)

"""Output Visualization"""
cv2.imshow("result", image)
cv2.waitKey(0)