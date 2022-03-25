import numpy as np

import matplotlib.pyplot as plt

from scipy.optimize import minimize
from scipy.optimize import Bounds
from scipy.optimize import LinearConstraint

##def objective(xx):
##    x = xx[0]
##    y = xx[1]
##    return (x-y)**2+1/3*(x+y-10)**2

def objective(production_rate,profit_per_product):

    return -np.sum(production_rate*profit_per_product)

profit_per_product = np.array([90,60,45])

lb = [0,0,0]
ub = [np.inf,np.inf,np.inf]

B = Bounds(lb,ub)

A = np.zeros((5,3))

A[0,:] = np.array([1.5 , 1.0 , 0.0 ])
A[1,:] = np.array([2.0 , 0.0 , 1.5 ])
A[2,:] = np.array([0.75, 3.0 , 0.0 ])
A[3,:] = np.array([1.25, 0.75, 1.0 ])
A[4,:] = np.array([1.0 , 0.0 , 2.0 ])

lb = [0, 0, 0, 0, 0]
ub = [450, 250, 800, 450, 600]

C = LinearConstraint(A,lb,ub)

H = lambda x, v: np.zeros((3,3))

T = minimize(objective,np.zeros(3),args=(profit_per_product,),
             method='trust-constr',constraints=C,bounds=B,hess=H)
    
##xL = 0
##xU = 8
##
##yL = 0
##yU = 8
##
##x = np.linspace(xL,xU)
##y = np.linspace(yL,yU)
##
##S = minimize(objective,(0,0),method="Powell")
##
##X,Y = np.meshgrid(x,y)
##
##Z = objective((X,Y))
##
##fig = plt.figure()
##
##ax = fig.add_subplot(111, projection='3d')
##
##ax.plot_surface(X,Y,Z)
##
##ax.set_xlabel('x-axis')
##ax.set_ylabel('y-axis')
##
##plt.show()
