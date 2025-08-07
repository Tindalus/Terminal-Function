import math

def term(x_end,x_initial,T):
    """
    **Returns list of polinomial coefficients for the terminal function x(t) = ΣCi*t^i**
    \n At the end of the function user can uncomment polinomial visualization
    
    Args:
        x_end (list[float]): list (n,1) of end state, n element is the coordinate of the end point and n-i's element is i's derivative of that coordinate

        x_initial (list[float]): list (n,1) of initial state, n element is the coordinate of the initial point and n-i's element is i's derivative of that coordinate

        
        T (float): termial time when curve reaches its end coordinate
    Returns:
        Ci (list[float]): list (n^2,1) of polinomial coefficients where elemement i is the coefficient of the t^i term

    Example:
        Coefs = term([0,0,1],[1,0,0],10)
        \n print(Coefs)
        \n [0.0, 0.0, 0.5, -0.13999999999999999, 0.0135, -0.00044]
        
    """
    
    x_0 = x_initial
    x_k = x_end
    n = len(x_k)
    r = len(x_0)

    def d_v( v, r):
        d = -1*math.factorial((r + n - v - 1))/(math.factorial(n-1)*math.factorial(r-v)*math.factorial(v))
        return d
    def h_v( v, r):
        h = ((-1)**v) * math.factorial((r + n - v - 1))/(math.factorial(r)*math.factorial(n-v-1)*math.factorial(v))
        return h

    #Simulation Parameters
    Tstop = T
    Ts = 0.1
    N = int(Tstop/Ts) # Simulation length
    dv = []
    hv = []
    Cr1 = []
    Cr2 = []
    Ci = []
    Cl1 = []
    Cl2 = []
    x = []
    xt = []
    Dv = []
    Hv = []
    for j in range(r):
        dv1 = [0]
        Dv.append(dv1)
        Hv.append(dv1)
    for k in range(r+n):
        if k >= r:
            for v in range(r):
                d1 = d_v(v, k)
                dv.append(d1)
            for v in range(n):
                h1 = h_v(v, k)
                hv.append(h1)
            Dv.append(dv)
            Hv.append(hv)
            dv = []
            hv = []
            
    for k in range(r+n):
        if k <= r - 1:
            ci = x_0[k]/(math.factorial(k))
            Ci.append(ci)
        if k == r:
            for v in range(r):
                Cr_ = (Dv[r][v]*x_0[v])/(T**(r-v))
                Cr1.append(Cr_)
            for v in range(n):
                Cra = (Hv[r][v]*x_k[v])/(T**(r-v))
                Cr2.append(Cra)
            Cr = sum(Cr1) + sum(Cr2)
            Ci.append(Cr)
        if k > r:
            for v in range(r):
                if v == 0:
                    cl1 = 1/(k*T**(k-v))*(Dv[k-1][v]*(k-v-1) + Dv[k-1][r-1]*Dv[r][v]*math.factorial(r))*x_0[v]
                    Dv[k][v] = (1/k)*(Dv[k-1][v]*(k-v-1) + Dv[k-1][r-1]*Dv[r][v]*math.factorial(r))
                else:
                    cl1 = 1/(k*T**(k-v))*(Dv[k-1][v-1]+Dv[k-1][v]*(k-v-1) + Dv[k-1][r-1]*Dv[r][v]*math.factorial(r))*x_0[v]
                    Dv[k][v] = (1/k)*(Dv[k-1][v-1]+Dv[k-1][v]*(k-v-1) + Dv[k-1][r-1]*Dv[r][v]*math.factorial(r))
                Cl1.append(cl1)
            for v in range(n):
                cl2 = 1/(k*T**(k-v))*(Hv[k-1][v]*(k-v-1) + Dv[k-1][r-1]*Hv[r][v]*math.factorial(r))*x_k[v]
                Hv[k][v] = (1/k)*(Hv[k-1][v]*(k-v-1) + Dv[k-1][r-1]*Hv[r][v]*math.factorial(r))
                Cl2.append(cl2)
            Cl = sum(Cl1) + sum(Cl2)
            Ci.append(Cl)
            Cl2 = []
            Cl1 = []



    #Visualization in the form of x(t) = ΣCi*t**i
    x_0 = []
    x_k = []

    # for t in range(N):
    #     for i in range(r+n):
    #         x1 = Ci[i]*((t*Ts)**i)
    #         x.append(x1)
    #     X = sum(x)
    #     x = []
    #     xt.append(X)

    # for m in range(len(Ci)):
    #    if Ci[m] != 0 and m!=0:
    #        print(str(Ci[m]) +"t"+"^"+str(m), end="")
    #        break
    #    elif Ci[m] != 0 and m ==0:
    #        print(str(Ci[m]), end="")
    #        break

    # for j in range(m+1, len(Ci)):
    #    if Ci[j] > 0:
    #        print("+"+str(Ci[j])+"t"+"^"+str(j), end="")
    #    elif Ci[j] ==0:
    #        continue
    #    else:
    #        print("-"+str(Ci[j])[1:]+"t"+"^"+str(j), end="") 

    return Ci