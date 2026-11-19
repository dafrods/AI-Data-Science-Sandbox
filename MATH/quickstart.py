import matplotlib.pyplot as plt
import numpy as np

# import matplotlib as mpl
%matplotlib notebook

# gen = lambda a,b : [x for x in range(a,b+1)]

# fig, ax = plt.subplots()
# ax.plot(gen(1,4), [1,4,2,3])


# fig = plt.figure()  # an empty figure with no Axes
# fig, ax = plt.subplots()  # a figure with a single Axes
# fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
# # a figure with one axes on the left, and two on the right:
# fig, axs = plt.subplot_mosaic([['left', 'right_top'],
#                                ['left', 'right_bottom']])


# plt.show()

x = [0, 1, 2, 3] 
y = [0, 1, 4, 9]
plt.plot(x, y)
plt.show()