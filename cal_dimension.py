import numpy as np
import pandas as pd
#let received laser sensor as 1
#let not received laser sensor as 0
#data will be 2d array with shape (x,y) and (x,z)
#x is the horizontal length, y is the vertical length, z is the depth
#let the sameple data be 100x100
data_frame = np.zeros((100,100))
sample_data = np.random.randint(0,2,(100,100))
sample_data = pd.DataFrame(sample_data)
# for x in range(100):
#     data_frame[x][:x]=1
print(sample_data)
each_row_x = np.sum(sample_data,axis=1)
each_row_y = np.sum(sample_data,axis=0)
max_y = max(each_row_y)
max_x = max(each_row_x)
print(max_x,max_y)