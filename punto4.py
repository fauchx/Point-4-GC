# -*- coding: utf-8 -*-
"""Punto4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E9xKm662yytfAijhztYEa0jMsVNy9cZP
"""

import colorsys

#CONVERTIR RGB A HSV
def convert1(r,g,b):
  (r1,g1,b1) = (r/255.0,g/255.0,b/255.0)
  (h,s,v) = colorsys.rgb_to_hsv(r1,g1,b1)
  print("HSV :",h,",",s,",",v)

#CONVERTIR HSV A RGB
def convert2(h,s,v):
  (h1,s1,v1) = (h/255.0,s/255.0,v/179.0)
  (r,g,b) = colorsys.hsv_to_rgb(h1,s1,v1)
  (r,g,b) = (int(r*255), int(g*255), int(b*255))
  print("RGB :",r,",",g,",",b)

#CONVERTIR RGB A HLS
def convert3(r,g,b):
  (r1,g1,b1) = (r/255.0,g/255.0,b/255.0)
  (h,l,s) = colorsys.rgb_to_hls(r1,g1,b1)
  print("HLS :",h,",",l,",",s)

#CONVERTIR HLS A RGB
def convert4(h,l,s):
  (r,g,b) = colorsys.hls_to_rgb(h,l,s)
  (r,g,b) = (int(r*255), int(g*255), int(b*255))
  print("RGB :",r,",",g,",",b)