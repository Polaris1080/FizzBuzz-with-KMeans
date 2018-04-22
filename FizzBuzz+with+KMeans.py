import numpy as np
from sklearn.cluster import KMeans
result=KMeans(n_clusters=4,n_jobs=-1).fit_predict(np.array([np.tile([0,0,1],30),np.tile([0,0,0,0,1],18)]).T)
print(['FizzBuzz' if t == result[14] else 'Fizz' if t == result[2] else 'Buzz' if t == result[4] else 0 for t in result])