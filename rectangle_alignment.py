"""Importing Libraries"""
import cv2
import numpy as np

"""Step 1 Transalating the contour to the orgin and Step 3 Translating back the contour to it's original place """

def rotate_contour(cnt, angle):
    M = cv2.moments(cnt)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])

    cnt_norm = cnt - [cx, cy]
    
    coordinates = cnt_norm[:, 0, :]
    xs, ys = coordinates[:, 0], coordinates[:, 1]
    thetas, rhos = cart2pol(xs, ys)
    
    thetas = np.rad2deg(thetas)
    thetas = (thetas + angle) % 360
    thetas = np.deg2rad(thetas)
    
    xs, ys = pol2cart(thetas, rhos)
    
    cnt_norm[:, 0, 0] = xs
    cnt_norm[:, 0, 1] = ys

    cnt_rotated = cnt_norm + [cx, cy]
    cnt_rotated = cnt_rotated.astype(np.int32)

    return cnt_rotated


"""Step 2 Rotating Each point of the contour"""
def cart2pol(x, y):
    theta = np.arctan2(y, x)
    rho = np.hypot(x, y)
    return theta, rho


def pol2cart(theta, rho):
    x = rho * np.cos(theta)
    y = rho * np.sin(theta)
    return x, y

"""Inputting Image"""
image = cv2.imread('shapes.png')

"""Creating White empty background"""
image_1 = np.zeros(image.shape, dtype = "uint8")
image_1.fill(255)

"""Edge Detection"""
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 130, 255,3)

"""Rotating the detected Edges of Rectangle into a Straight Alignment withe help of inputting contours to the rotating function"""
cnts = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for i in range(1,6):
    cnt_rotated = rotate_contour(cnts[0][i], -30)
    for c in cnts[0][i]:
        cv2.drawContours(image_1,[cnt_rotated], 0, (0,0,0), 3)

for i in range(6,12):
    cnt_rotated = rotate_contour(cnts[0][i], 30)
    for c in cnts[0][i]:
        cv2.drawContours(image_1,[cnt_rotated], 0, (0,0,0), 3)

for i in range(12,18):
    cnt_rotated = rotate_contour(cnts[0][i], -15)
    for c in cnts[0][i]:
        cv2.drawContours(image_1,[cnt_rotated], 0, (0,0,0), 3)

for i in range(18,24):
    cnt_rotated = rotate_contour(cnts[0][i], 15)
    for c in cnts[0][i]:
        cv2.drawContours(image_1,[cnt_rotated], 0, (0,0,0), 3)
    

"""Output Visualization"""
cv2.imshow('Rectangle Aligned Image',image_1)
cv2.imshow("Original Image", image)
cv2.waitKey(0)