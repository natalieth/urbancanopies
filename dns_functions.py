from scipy.io import loadmat
import numpy as np

def readvar(fi,var): 
    #
    # reads in a variable from a matlab file, 
    # specify Path+file and variable-string
    #
    F = loadmat(fi)
    var = F[var][:]
    return var

def readuvw(fi): 
    #
    # reads in a variable from a matlab file, 
    # specify Path+file and variable-string
    #
    F = loadmat(fi)
    u = F['U'][:]
    v = F['V'][:]
    w = F['W'][:]
    return u,v,w

def calc_lm(uw,vw,uwd,vwd,du,dv):
    #
    # Calculates mixing length excluding and
    # including dispersive stresses 
    #
    rho = 1.2
    dudz = np.sqrt(du**2 + dv**2)
    Uw = np.sqrt(uw**2 + vw**2)
    Uwd = np.sqrt(uwd**2 + vwd**2)
    
    lm_d = np.sqrt((Uw + Uwd)*1/rho)/dudz
    lm = np.sqrt(1/rho*Uw)/dudz
    
    return lm, lm_d

def disp_stress(u,w):
    #
    # Calculates the mean dispersive stresses profile
    # of a 3D array (x,y,z).
    # 
    nz = u.shape[2]
    umean = np.nanmean(u,axis=(0,1))
    wmean = np.nanmean(w,axis=(0,1))

    u_t = np.zeros(nz)
    w_t = np.zeros(nz)
    
    for z in range(nz):
        u_tx = 0
        w_tx = 0
        n = 0 
        for i in range(u.shape[0]):
            for j in range(u.shape[1]):
                u_tx =+ (u[i,j,z]-umean[z])
                w_tx =+ (w[i,j,z]-umean[z])
                n =+ 1 

        u_t[z] = u_tx/n
        w_t[z] = w_tx/n

    return u_t*w_t





       
