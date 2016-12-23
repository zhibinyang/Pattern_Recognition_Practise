import numpy as np
import Perceptron


def getTrainDataSet():
    omega1 = np.array([[1,1,1],[2,2,1],[2,1,1]])
    omega2 = np.array([[1,-1,1],[1,-2,1],[2,-2,1]])
    omega3 = np.array([[-1,1,1],[-1,2,1],[-2,1,1]])
    DataSet = []
    DataSet.append(omega1)
    DataSet.append(omega2)
    DataSet.append(omega3)
    return DataSet

def getInitW():
    # w1 = np.array([0.5,0.5,0.5])
    # w2 = np.array([0.5,0.5,0.5])
    # w3 = np.array([0.5,0.5,0.5])
    w1 = np.array([5.13, 3.6, 1.0])
    w2 = np.array([-0.05, -3.16, -0.41])
    w3 = np.array([-3.84, 1.28, 0.69])
    # w = []
    # w.append(w1)
    # w.append(w2)
    # w.append(w3)
    w = np.hstack((w1,w2))
    w = np.hstack((w,w3))
    return w
    #return np.random.random(9)

def Kesler_Extender(DataSetVector):
    ResultDataSet = np.array([])
    for i in range(len(DataSetVector)):
        ResultDataSetRow = np.array([])
        omegaRowCount = DataSetVector[i].shape[0]
        for j in range(DataSetVector[i].shape[0]):
            for n in range(DataSetVector[i].shape[0]):
                if n != j:
                    #print "n=",n,"j=",j
                    if n < j:
                        if n == 0:
                            ResultDataSetRow = np.hstack((DataSetVector[i][j] * -1,np.array([0,0,0]).repeat(j-n-1)))
                            ResultDataSetRow = np.hstack((ResultDataSetRow,DataSetVector[i][j]))
                            ResultDataSetRow = np.hstack((ResultDataSetRow,np.array([0,0,0]).repeat(DataSetVector[i].shape[0]-j-1)))
                            #print ResultDataSetRow
                        else:
                            ResultDataSetRow = np.hstack((np.array([0,0,0]).repeat(n),DataSetVector[i][j] * -1))
                            ResultDataSetRow = np.hstack((ResultDataSetRow,np.array([0,0,0]).repeat(j-n-1)))
                            ResultDataSetRow = np.hstack((ResultDataSetRow,DataSetVector[i][j]))
                            ResultDataSetRow = np.hstack((ResultDataSetRow,np.array([0,0,0]).repeat(DataSetVector[i].shape[0]-j-1)))
                            #print ResultDataSetRow
                    else:
                        if j == 0:
                            ResultDataSetRow = np.hstack((DataSetVector[i][j],np.array([0,0,0]).repeat(n-j-1)))
                            ResultDataSetRow = np.hstack((ResultDataSetRow, DataSetVector[i][j] * -1))
                            ResultDataSetRow = np.hstack((ResultDataSetRow, np.array([0,0,0]).repeat(DataSetVector[i].shape[0]-n-1)))
                            #print ResultDataSetRow

                        else:
                            ResultDataSetRow = np.hstack((np.array([0, 0, 0]).repeat(j), DataSetVector[i][j]))
                            ResultDataSetRow = np.hstack((ResultDataSetRow,np.array([0,0,0]).repeat(n-j-1)))
                            ResultDataSetRow = np.hstack((ResultDataSetRow,DataSetVector[i][j] * -1))
                            ResultDataSetRow = np.hstack(
                                (ResultDataSetRow, np.array([0, 0, 0]).repeat(DataSetVector[i].shape[0] - n - 1)))
                            #print ResultDataSetRow
                    #print ResultDataSetRow
                    if ResultDataSet.shape[0] == 0: # if it's empty
                        ResultDataSet = ResultDataSetRow
                        #print ResultDataSet
                    else:
                        ResultDataSet = np.vstack((ResultDataSet,ResultDataSetRow))
    return ResultDataSet

def main():
    DataSetVector = getTrainDataSet()
    InitWVector = getInitW()
    extended_matrix = Kesler_Extender(DataSetVector=DataSetVector)
    print InitWVector
    print extended_matrix
    Perceptron.Perceptron(extended_matrix,np.array([]),InitWVector,0.5)
if __name__ == '__main__':
    main()