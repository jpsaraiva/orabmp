from __future__ import division
from PIL import Image
import pandas as pd
import numpy as np
import os
from stat import ST_SIZE

#select segment_name "SEG",block_id "START",block_id+blocks "END" from dba_extents ext where tablespace_name='SYSTEM' and file_id=4 order by file_id,block_id;

def get_spaced_colors(n):
    max_value = 16581375 #255**3
    interval = int(max_value / n)
    colors = [hex(I)[2:].zfill(6) for I in range(0, max_value, interval)]
    return [(int(i[:2], 16), int(i[2:4], 16), int(i[4:], 16)) for i in colors]

df = pd.read_csv('source.csv')

size = 800

width = size  # defines the x of the image
height = int(round(df['END'].max()/size) +1)	# defines the y of the image

img = Image.new('RGB', (width, height), "white") #creates image with white background

tablespaces = df.SEG.unique()
rgb_list = get_spaced_colors(int(tablespaces.shape[0]))


pixels = img.load()
for index, row in df.iterrows():
	tbs=row['SEG']
	start=row['START']
	end=row['END']
	for i in range(start,end):
		x=(i%size)
		y=int(i/size)
		print str(x)+","+str(y) + " " + str(i) + " (" + str(width)+","+str(height)+")"
		if tbs in tablespaces:
			rgb = int([i for i,t in enumerate(tablespaces) if t == tbs][0])
			color = rgb_list[rgb]
			pixels[x,y] = color
		#else:
			#pixels[x,y]= (0, 0, 0) #blck

img.save("image.bmp")
