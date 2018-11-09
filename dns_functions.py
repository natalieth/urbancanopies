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


