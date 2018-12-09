from sklearn.naive_bayes import GaussianNB
import numpy as np

x=np.array([[-1,4],[1,5],[0,2],[-2,0],[2,3],[-4,0],[-1,1],[1,1],[-2,2],[2,7],[-4,1],[-2,7]])
y=np.array([3,3,3,3,4,3,3,4,3,4,4,4])

model=GaussianNB()

model.fit(x,y)

print(model.predict([[3,2]]))
