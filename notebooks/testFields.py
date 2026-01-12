import numpy as np

def peninsula():
    """ Create 2D velocity field around a peninsula for test purposes
    Following the "Manual of recommended practices for modelling physical – biological interactions during fish early life" (Bjørn Ådlandsvik et al.) we consider a straight coast at y = 0 with ocean in the upper half plane (y > 0) and with a half‐circular peninsula with centre (x0, 0) and radius R. A domain of length L (100 km) along the coast and width W (50 km) is considered. The peninsula centre is at x = 0.5 L and the radius R = 0.32 W.
    u0 = along-coast velocity = 1 m.s-1 
    """
    u0 = 1
    L = 500
    W = 100
    R = 0.32*W
    x0 = 0.5*L

    x = np.arange(0,500,1)
    y = np.arange(0,100,1)
    psi = np.zeros((500,100))
    u = np.zeros((500,100))
    v = np.zeros((500,100))

    for i in range(500):
        for j in range(100):
            psi[i,j] = (u0*R**2*y[j]/((x[i]-x0)**2 + y[j]**2)) - u0*y[j]

    psi[psi>0] = np.nan
    xx = np.tile(x,[100,1])
    xx = xx.T
    yy = np.tile(y,[500,1])
    u[0:500,1:100] = -np.diff(psi,n=1,axis = 1)/np.diff(yy,n=1,axis=1)
    v[1:500,0:100] = np.diff(psi,n=1,axis=0)/np.diff(xx,n=1,axis=0)

    field = {'lon':xx,'lat':yy,'psi':psi,'u':u,'v':v,'dates':'2022-09-10'}
    return field