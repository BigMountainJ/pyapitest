# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 14:33:02 2023

@author: zmmaye
"""

import pickle
import numpy as np


def apply():
    X_te= np.genfromtxt('input.csv', delimiter=',')

    with open('model.pickle', 'rb') as f:
        net,scaler = pickle.load(f) 

    test_preds = net.predict(np.hstack([scaler.transform(X_te[:,:8]),X_te[:,8:]])) #predict using test features
    
    print(test_preds)
    np.savetxt("output.csv", test_preds, delimiter=",")


apply()