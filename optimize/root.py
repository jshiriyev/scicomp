

def newton(x_0,epd,Re):
    x_old = x_0
    tol = 1
    while tol>1e-10:
        x_new = x_old-obj(x_old,epd,Re)/obj_der(x_old,epd,Re)
        tol = np.abs(x_new-x_old)
        x_old = x_new
##        print(tol)
    return x_new

def secant(x_0,x_1,epd,Re):
    x0 = x_0
    x1 = x_1
    tol = 1
    while tol>1e-10:
        y0 = obj(x0,epd,Re)
        y1 = obj(x1,epd,Re)
        x2 = x1-y1*(x1-x0)/(y1-y0)
        tol = np.abs(x2-x1)
        x0 = x1
        x1 = x2
##        print(tol)
    return x2

def bisect():

    pass
