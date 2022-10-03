import numpy as np


taxi = np.genfromtxt('nyc_taxis.csv', delimiter = ',', skip_header =True )

speed = taxi[:, 7]/ (taxi[:,8]/3600)    # finding speed  of every vehicle

mean_speed = speed.mean()   # finding mean speed of all vehicle

print(mean_speed)


ridesInFeb = taxi[taxi[:, 1] == 2,1]      #number of trip in february

print(ridesInFeb.shape[0])


trip50 = taxi[taxi[:,-3]>50,-3]
print(trip50.shape[0])
