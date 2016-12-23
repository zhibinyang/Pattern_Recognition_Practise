import numpy as np
# Algorithm: w(t+1) = w(t) + rho * x_t, if x_t in omega_1 and w^T(t)x_t <= 0
# Algorithm: w(t+1) = w(t) - rho * x_t, if x_t in omega_2 and w^T(t)x_t >= 0

def getTrainingDataSet_1():
    return np.array([[-1,0,1],[0,1,1],[1,-1,1]])

def getTrainingDataSet_2():
    return np.array([[0,-1,1],[1,0,1]])

def getInitW():
    return np.array([0,0,0])

def Perceptron(DataSet1, DataSet2, InitW, rho):
    W = InitW
    ok_count = 0
    recurring_count = 0
    total_count = DataSet1.shape[0] + DataSet2.shape[0]
    while True:
        for row in DataSet1:
            recurring_count += 1
            if row.dot(W) <= 0:
                W = W + row * rho
                ok_count = 0
            else:
                ok_count += 1
            #print ok_count
            #print W
        for row in DataSet2:
            recurring_count += 1
            if row.dot(W) >= 0:
                W = W - row * rho
                ok_count = 0
            else:
                ok_count += 1
        if ok_count >= total_count:
            break
        if recurring_count >= 10000:
            raise BaseException("Running more than 10000 time, aborting...")
    print "Final W:",W
    print "Recurring Count:",recurring_count/total_count

def main():
    DataSet1 = getTrainingDataSet_1()
    DataSet2 = getTrainingDataSet_2()
    InitW = getInitW()
    Perceptron(DataSet1=DataSet1, DataSet2=DataSet2, InitW=InitW, rho=1.0)
if __name__ == '__main__':
    main()