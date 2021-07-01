import numpy as np
import matplotlib.pyplot as plt
import math

# np ndarray of random numbers [0, 1)
rand_nums = np.random.rand(5, 5)

# change the default open intervals [a, b)
a = 10
b = 20

changed_interval = rand_nums * (b - a) + a
# print(changed_interval)

# random numbers from standard normal and normal distributions
size = 100
standard_norm_rand = np.random.standard_normal(size)

# set mean (loc) and standard deviation (scale) to be 50 and 10
normal_rand = np.random.normal(loc=50, scale=10, size=size)

# plot the random standard normal and normal numbers
fig, ((ax1, ax2)) = plt.subplots(ncols=2, nrows=1)
ax1.hist(standard_norm_rand, bins=25)
ax1.set_title('standard normal')
ax2.hist(normal_rand, bins=25)
ax2.set_title(f'normal({math.ceil(normal_rand.mean())}, {math.ceil(normal_rand.std())})')

plt.show()
