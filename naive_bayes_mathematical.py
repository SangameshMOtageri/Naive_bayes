import numpy as np
import math


def calculate_mean(x,a,c):
    variable=0
    for i in range(len(y)):
        if y[i] == c:
            variable +=x[i,a]
    print(variable)
    return variable
def calculate_variance(x,a,c,mean):
    variable=0
    for i in range(len(y)):
        if y[i] == c:
            variable += (x[i,a]-mean)**2
    return variable
def class_probability(y):
    c_probability={}
    c_length={}
    c=list()
    temp=y
    for item in temp:
        count=0
        if item not in c:
            for i in temp:
                if item == i:
                    count +=1
            c_probability[item]=float(count/len(y))
            c_length[item]=count
            c.append(item)
    return c_probability, c_length

def calculate_probability(mean, variance, x):
    return (((1/math.sqrt(2*3.14*variance))*math.exp((-0.5)*(((x-mean)**2)/variance))))

if __name__ == '__main__':

    x=np.array([[-3,7],[1,5],[1,2],[-2,0],[2,3],[-4,0],[-1,1],[1,1],[-2,2],[2,7],[-4,1],[-2,7]])
    y=np.array([3,3,3,3,4,3,3,4,3,4,4,4])

    n_class = 2
    n_attributes = 2

    mean_x = np.ndarray(shape=(n_class,n_attributes), dtype=float, order='C')
    variance_x = np.ndarray(shape=(n_class,n_attributes), dtype=float, order='C')
    #predict = np.ndarray(shape=(n_class,n_attributes), dtype=float, order='C')

    print('starting!!')
    c_probability, c_length=class_probability(y)
    print(c_probability)
    print(c_length)
    x_predict=[3,2]
    for n in c_probability:
        for a in range(n_attributes):
            print(n,a,c_length[n])
            mean=(calculate_mean(x,a,n)/c_length[n])
            variance=(calculate_variance(x,a,n,mean)/c_length[n])
            predict= calculate_probability(mean, variance, x_predict[a])   
            print(mean,variance,predict)
    print(predict)

    
