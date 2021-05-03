#!/usr/bin/env python3
# Auhor Dario Clavijo 2021

import math


def mean(L):
    """ mean or average of all values in list"""

    tmp = sum(L) * 1.0
    l = len(L)
    return tmp/l

avg = mean

def stddev(X):
    """ standar deviation calculaion of all values in the list """

    l = len(X)
    def F(X):
      x = mean(X)
      s = 0
      for i in range(0,l):
          s += (X[i] - x) ** 2
      return s
    return math.sqrt((1.0 / l) * F(X))


def MAD(X):
    """ Median Absolute deviation calculaion of all values in the list """

    l = len(X)
    def F(X):
        x = mean(X)
        s = 0
        for i in range(0,l):
            s += abs(X[i] - x) 
        return s
    return (1.0 / l) * F(X)


def bounds(X):
    """ Upper and lower bounds """

    SD = stddev(X)
    m = mean(X)
    return m - SD, SD + m


def simple_anonaly_detection(X):
    """ A simple check if a value in a list is outside the bounds
    It sould return tuples of (index,value) """

    B = bounds(X)
    for i in range(0,len(X)):
         if X[i] < B[0] or X[i] > B[1]:
             yield (i,X[i])


def zvalue(X):
    """ zvalue calculation """

    SD = stddev(X)
    m = mean(X)
    for i in range(0,len(X)):
        yield (X[i] - m) / SD


def zvalue_anomaly_detection(X,treshold = [-1,1]):
    """ zvalue anomaly detection 
    It sould return tuples of (index,value,score) """

    Z = list(zvalue(X))
    for i in range(0,len(X)):
        if Z[i] < treshold[0] or Z[i] > treshold[1]:
            yield (i,X[i],Z[i])
       

def MAD_anomaly_detection(X,treshold = 1.5):
    """ Median absoute value anomaly detection 
    It should return a tuple of (index,value,score) """

    M = MAD(X)
    m = mean(X)
    for i in range(0,len(X)):
        v = abs(X[i] - m) / M 
        if v > treshold:
            yield (i,X[i],v)


def test():
    """
    Expected output:
    Series: [2, 3, 5, 2, 3, 12, 5, 3, 4]
    Mean: 4.333333333333333
    StdDev: 2.9059326290271157
    Bounds: (1.4274007043062173, 7.239265962360449)
    simple anomaly detection: [(5, 12)]
    zvalues: [-0.8029550685469661, -0.45883146774112343, 0.22941573387056186, -0.8029550685469661, -0.45883146774112343, 2.6382809395114606, 0.22941573387056186, -0.45883146774112343, -0.11470786693528078]
    zvalue anomaly detection: [(5, 12, 2.6382809395114606)]
    MAD anomaly detection: [(5, 12, 3.8333333333333344)]
    """
    S = [2,3,5,2,3,12,5,3,4]
    print("Series:",S)
    print("Mean:",mean(S))
    print("StdDev:",stddev(S))
    print("Bounds:",bounds(S))
    print("simple anomaly detection:",list(simple_anonaly_detection(S)))
    print("zvalues:",list(zvalue(S)))
    print("zvalue anomaly detection:",list(zvalue_anomaly_detection(S)))
    print("MAD anomaly detection:",list(MAD_anomaly_detection(S)))
    

if __name__ == "__main__":
    test()
