import numpy as np
# Algorithm: omega_min = (X^T * X)^-1 * X^T * Y

def getTrainingDataSet():
    return np.array([[0.2,0.7,1],[0.3,0.3,1],[0.4,0.5,1],[0.6,0.5,1],[0.1,0.4,1],[0.4,0.6,1],[0.6,0.2,1],[0.7,0.4,1],[0.8,0.6,1],[0.7,0.5,1]])

def getGroupDataSet():
    return np.array([1,1,1,1,1,-1,-1,-1,-1,-1])

def LMS(TrainingDataSet, GroupDataSet):
    X = TrainingDataSet
    y = GroupDataSet
    omega = np.linalg.inv(X.T.dot(X)).dot(X.T.dot(y))
    return omega

def main():
    TrainingDataSet = getTrainingDataSet()
    GroupDataSet = getGroupDataSet()
    print LMS(TrainingDataSet,GroupDataSet)

if __name__ == '__main__':
    main()