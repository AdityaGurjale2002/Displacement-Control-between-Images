#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np

def calculate_displacement(img1, img2):
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(gray1, gray2, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_local, max_local = cv2.minMaxLoc(result)

    displacement = (max_local[0] - min_local[0], max_local[1] - min_local[1])

    return displacement

if __name__ == "__main__":
    image1 = cv2.imread('F:/Police hackathon/c2.png')
    image2 = cv2.imread('F:/Police hackathon/c3.png')

    displacement = calculate_displacement(image1, image2)

    print(f"Displacement: {displacement}")


# In[ ]:




