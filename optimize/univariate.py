def dichotomous(objective,xL,xU,r=1/2,Nmax=50,tol=1e-3):
    
    for i in range(Nmax):

        x1 = xL+r*(xU-xL)
        x2 = xU-r*(xU-xL)
        
        f1 = objective(x1)
        f2 = objective(x2)

        if f1<f2:
            xL = x2
        else:
            xU = x1

        if abs(x1-x2)<tol:
            xopt = (x1+x2)/2
            break

    try:
        print("Converged result is: %.8f" %xopt)
        print("Number of iterations is: %d" %(i+1))
    except:
        print("Convergence could not be obtained with %d iterations" %(Nmax))