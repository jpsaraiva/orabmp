from __future__ import division
from PIL import Image
import pandas as pd
import numpy as np
import os
import datetime
from stat import ST_SIZE

#select segment_name "SEG",block_id "START",block_id+blocks "END" from dba_extents ext where tablespace_name='SYSTEM' and file_id=4 order by file_id,block_id;

colors = []
colors.append(['DB INCR','OK',(0,0,255)]) #blue
colors.append(['DB INCR','NOK',(139,0,0)]) #dark red
colors.append(['ARCHIVELOG','OK',(0,100,0)]) # dark green
colors.append(['ARCHIVELOG','NOK',(139,0,0)]) #dark red

df = pd.read_csv('rman.csv')

width = 310  # 31 days * 10
height = 240 # 24 hours * 10

img = Image.new('RGB', (width, height), "white") #creates image with white background

pixels = img.load()
for index, row in df.iterrows():
	start_day=int(datetime.datetime.strptime(row['START'],'%Y-%m-%d %H:%M:%S').strftime('%d'))
	end_day=int(datetime.datetime.strptime(row['END'],'%Y-%m-%d %H:%M:%S').strftime('%d'))
	start_hour=int(datetime.datetime.strptime(row['START'],'%Y-%m-%d %H:%M:%S').strftime('%H'))
	end_hour=int(datetime.datetime.strptime(row['END'],'%Y-%m-%d %H:%M:%S').strftime('%H'))
	# if (end_day == start_day):
		# for x in range (start_day * 10, start_day * 10 + 10 ):
			# for y in range ( start_hour * 10, end_hour * 10 + 10):
				# for c in colors:
					# if ( c[0] == row['TYPE'] ) and ( c[1] == row['STATUS'] ):
						# pixels[x,y] = c[2]
	# else
	for x in range (start_day * 10, end_day * 10 + 10 ):
		if (x/10 > start_day) and ( x/10 <= end_day):
			hr_start = 0
		else:
			hr_start = start_hour
		if ( x/10 < end_day ):
			hr_end = 23
		else:
			hr_end = end_hour
		for y in range(hr_start * 10, hr_end * 10 + 10):
			for c in colors:
				if ( c[0] == row['TYPE'] ) and ( c[1] == row['STATUS'] ):
					pixels[x,y] = c[2]
	
img.save("rman.bmp")

