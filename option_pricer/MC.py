'''
created by @ Qiangyu YAN
'''
import closed_form_formulas as form
import numpy as np
from scipy.stats import norm
import random as rd
rd.seed(10)

##########################################
# Arith Call Option, return 2 number
# as interval begin and end
# m is the number of paths
# control is bool, false - no control
##########################################
def Arith_Call_Option(S_0, sigma, r, T, K, n, m, control, seed):
    Dt = T/n
    geo = form.geom_asian_call_option(S_0, sigma, r, T, K, n, t=0)
    np.random.seed(seed)
    mu = np.exp((r - 0.5*sigma*sigma) * Dt)
    arithPayoff, geoPayoff = [], []
    for i in range(m):
        growthFactor = mu * np.exp(sigma * np.sqrt(Dt) * np.random.standard_normal())
        Spath = []
        Spath.append(S_0 * growthFactor)
        for j in range(n-1):
            # from lecture 4, page 16
            growthFactor = mu * np.exp(sigma * np.sqrt(Dt)*np.random.standard_normal())
            Spath.append(Spath[-1] * growthFactor)
        # Arithmetic mean
        arithMean = np.mean(Spath)
        arithPayoff.append(np.exp(-r*T) * max(arithMean - K, 0))
        # Geometric mean
        if(control):
            geoMean = np.exp( (1/n) * np.sum(np.log(Spath)))
            geoPayoff.append(np.exp(-r*T) * max(geoMean - K, 0))
    if(control):
        covXY = np.mean(np.multiply(arithPayoff,geoPayoff)) \
            - np.mean(arithPayoff) * np.mean(geoPayoff)
        theta = covXY / np.var(geoPayoff)
        Z = arithPayoff + theta * (geo - geoPayoff)
        Zmean = np.mean(Z)
        Zstd = np.std(Z)
        return Zmean-1.96*Zstd/np.sqrt(m), Zmean+1.96*Zstd/np.sqrt(m)
    else:
        Pmean = np.mean(arithPayoff)
        Pstd = np.std(arithPayoff)
        return Pmean-1.96*Pstd/np.sqrt(m), Pmean+1.96*Pstd/np.sqrt(m)



##########################################
# Arith Put Option, return 2 number
# as interval begin and end
# m is the number of paths
# control is bool, false - no control
##########################################
def Arith_Put_Option(S_0, sigma, r, T, K, n, m, control, seed):
    Dt = T/n
    geo = form.geom_asian_put_option(S_0, sigma, r, T, K, n, t=0)
    np.random.seed(seed)
    mu = np.exp((r - 0.5*sigma*sigma) * Dt)
    arithPayoff, geoPayoff = [], []
    for i in range(m):
        growthFactor = mu * np.exp(sigma * np.sqrt(Dt) * np.random.standard_normal())
        Spath = []
        Spath.append(S_0 * growthFactor)
        for j in range(n-1):
            # from lecture 4, page 16
            growthFactor = mu * np.exp(sigma * np.sqrt(Dt)*np.random.standard_normal())
            Spath.append(Spath[-1] * growthFactor)
        # Arithmetic mean
        arithMean = np.mean(Spath)
        arithPayoff.append(np.exp(-r*T) * max(K - arithMean, 0))
        # Geometric mean
        if(control):
            geoMean = np.exp( 1/n * np.sum(np.log(Spath)))
            geoPayoff.append(np.exp(-r*T) * max(K - geoMean, 0))
    if(control):
        covXY = np.mean(np.multiply(arithPayoff,geoPayoff)) \
            - np.mean(arithPayoff) * np.mean(geoPayoff)
        theta = covXY / np.var(geoPayoff)
        Z = arithPayoff + theta * (geo - geoPayoff)
        Zmean = np.mean(Z)
        Zstd = np.std(Z)
        return Zmean-1.96*Zstd/np.sqrt(m), Zmean+1.96*Zstd/np.sqrt(m)
    else:
        Pmean = np.mean(arithPayoff)
        Pstd = np.std(arithPayoff)
        return Pmean-1.96*Pstd/np.sqrt(m), Pmean+1.96*Pstd/np.sqrt(m)




##########################################
# Arith Mean Call Basket, return 2 number
# as interval begin and end
# m is the number of paths
# control is bool, false - no control
##########################################
def Arith_Call_Basket(S_0_1, S_0_2, sigma_1, sigma_2, r, T, K, rho, m, control, seed):
    geo = form.geom_basket_call_option(S_0_1, S_0_2, sigma_1, sigma_2, r, T, K, rho, t=0)
    print(geo)
    np.random.seed(seed)
    arithPayoff, geoPayoff = [], []
    for i in range(m):
        Z1 = np.random.standard_normal()
        Z2 = rho*Z1 + np.sqrt(1 - rho*rho)*np.random.standard_normal()
        S_1 = S_0_1 * np.exp( (r - 0.5*sigma_1*sigma_1)*T \
            + sigma_1 * np.sqrt(T) * Z1 )
        S_2 = S_0_2 * np.exp( (r - 0.5*sigma_2*sigma_2)*T \
            + sigma_2 * np.sqrt(T) * Z2 )
        Spath = [S_1, S_2]
        # Arithmetic mean
        arithMean = np.mean(Spath)
        arithPayoff.append(np.exp(-r*T) * max(arithMean - K, 0))
        # Geometric mean
        if(control):
            geoMean = np.exp( 0.5 * np.sum(np.log(Spath)))
            geoPayoff.append(np.exp(-r*T) * max(geoMean - K, 0))
    if(control):
        covXY = np.mean(np.multiply(arithPayoff,geoPayoff)) \
            - np.mean(arithPayoff) * np.mean(geoPayoff)
        theta = covXY / np.var(geoPayoff)
        Z = arithPayoff + theta * (geo - geoPayoff)
        Zmean = np.mean(Z)
        Zstd = np.std(Z)
        return Zmean-1.96*Zstd/np.sqrt(m), Zmean+1.96*Zstd/np.sqrt(m)
    else:
        Pmean = np.mean(arithPayoff)
        Pstd = np.std(arithPayoff)
        return Pmean-1.96*Pstd/np.sqrt(m), Pmean+1.96*Pstd/np.sqrt(m)



##########################################
# Arith Mean Put Basket, return 2 number
# as interval begin and end
# m is the number of paths
# control is bool, false - no control
##########################################
def Arith_Put_Basket(S_0_1, S_0_2, sigma_1, sigma_2, r, T, K, rho, m, control, seed):
    geo = form.geom_basket_put_option(S_0_1, S_0_2, sigma_1, sigma_2, r, T, K, rho, t=0)
    np.random.seed(seed)
    arithPayoff, geoPayoff = [], []
    for i in range(m):
        Z1 = np.random.standard_normal()
        Z2 = rho*Z1 + np.sqrt(1 - rho*rho)*np.random.standard_normal()
        S_1 = S_0_1 * np.exp( (r - 0.5*sigma_1*sigma_1)*T \
            + sigma_1 * np.sqrt(T) * Z1 )
        S_2 = S_0_2 * np.exp( (r - 0.5*sigma_2*sigma_2)*T \
            + sigma_2 * np.sqrt(T) * Z2 )
        Spath = [S_1, S_2]
        # Arithmetic mean
        arithMean = np.mean(Spath)
        arithPayoff.append(np.exp(-r*T) * max(K - arithMean, 0))
        # Geometric mean
        if(control):
            geoMean = np.exp( 0.5 * np.sum(np.log(Spath)))
            geoPayoff.append(np.exp(-r*T) * max(K - geoMean, 0))
    if(control):
        covXY = np.mean(np.multiply(arithPayoff,geoPayoff)) \
            - np.mean(arithPayoff) * np.mean(geoPayoff)
        theta = covXY / np.var(geoPayoff)
        Z = arithPayoff + theta * (geo - geoPayoff)
        Zmean = np.mean(Z)
        Zstd = np.std(Z)
        return Zmean-1.96*Zstd/np.sqrt(m), Zmean+1.96*Zstd/np.sqrt(m)
    else:
        Pmean = np.mean(arithPayoff)
        Pstd = np.std(arithPayoff)
        return Pmean-1.96*Pstd/np.sqrt(m), Pmean+1.96*Pstd/np.sqrt(m)


r = 0.05
T = 3
S = 100
m = 100000

# Arith_Call_Option(S_0, sigma, r, T, K, n, m, control, seed):
print( Arith_Call_Option(S, 0.3, r, T, 100, 50, m, False, 10) )
# print( Arith_Call_Option(S, 0.3, r, T, 100, 100, m, False, 10) )
# print( Arith_Call_Option(S, 0.4, r, T, 100, 50, m, False, 10) )

print( Arith_Call_Option(S, 0.3, r, T, 100, 50, m, True, 10) )
# print( Arith_Call_Option(S, 0.3, r, T, 100, 100, m, True, 10) )
# print( Arith_Call_Option(S, 0.4, r, T, 100, 50, m, True, 10) )


# # # Arith_Put_Option(S_0, sigma, r, T, K, n, m, control, seed):
print( Arith_Put_Option(S, 0.3, r, T, 100, 50, m, False, 10) )
# print( Arith_Put_Option(S, 0.3, r, T, 100, 100, m, False, 10) )
# print( Arith_Put_Option(S, 0.4, r, T, 100, 50, m, False, 10) )

print( Arith_Put_Option(S, 0.3, r, T, 100, 50, m, True, 10) )
# print( Arith_Put_Option(S, 0.3, r, T, 100, 100, m, True, 10) )
# print( Arith_Put_Option(S, 0.4, r, T, 100, 50, m, True, 10) )


# # Arith_Call_Basket(S_0_1, S_0_2, sigma_1, sigma_2, 
# #                   r, T, K, rho, m, control, seed)
# print(Arith_Call_Basket(S, S, 0.3, 0.3, r, T, 100, 0.5, m, False, 10))
# print(Arith_Call_Basket(S, S, 0.3, 0.3, r, T, 100, 0.9, m, False, 10))
# print(Arith_Call_Basket(S, S, 0.1, 0.3, r, T, 100, 0.5, m, False, 10))
# print(Arith_Call_Basket(S, S, 0.3, 0.3, r, T, 80, 0.5, m, False, 10))
# print(Arith_Call_Basket(S, S, 0.3, 0.3, r, T, 120, 0.5, m, False, 10))
# print(Arith_Call_Basket(S, S, 0.5, 0.5, r, T, 100, 0.5, m, False, 10))

# print(Arith_Call_Basket(S, S, 0.3, 0.3, r, T, 100, 0.5, m, True, 10))
# print(Arith_Call_Basket(S, S, 0.3, 0.3, r, T, 100, 0.9, m, True, 10))
# print(Arith_Call_Basket(S, S, 0.1, 0.3, r, T, 100, 0.5, m, True, 10))
# print(Arith_Call_Basket(S, S, 0.3, 0.3, r, T, 80, 0.5, m, True, 10))
# print(Arith_Call_Basket(S, S, 0.3, 0.3, r, T, 120, 0.5, m, True, 10))
# print(Arith_Call_Basket(S, S, 0.5, 0.5, r, T, 100, 0.5, m, True, 10))

# # Arith_Call_Basket(S_0_1, S_0_2, sigma_1, sigma_2, 
# #                   r, T, K, rho, m, control, seed)
# print(Arith_Put_Basket(S, S, 0.3, 0.3, r, T, 100, 0.5, m, False, 10))
# print(Arith_Put_Basket(S, S, 0.3, 0.3, r, T, 100, 0.9, m, False, 10))
# print(Arith_Put_Basket(S, S, 0.1, 0.3, r, T, 100, 0.5, m, False, 10))
# print(Arith_Put_Basket(S, S, 0.3, 0.3, r, T, 80, 0.5, m, False, 10))
# print(Arith_Put_Basket(S, S, 0.3, 0.3, r, T, 120, 0.5, m, False, 10))
# print(Arith_Put_Basket(S, S, 0.5, 0.5, r, T, 100, 0.5, m, False, 10))

# print(Arith_Put_Basket(S, S, 0.3, 0.3, r, T, 100, 0.5, m, True, 10))
# print(Arith_Put_Basket(S, S, 0.3, 0.3, r, T, 100, 0.9, m, True, 10))
# print(Arith_Put_Basket(S, S, 0.1, 0.3, r, T, 100, 0.5, m, True, 10))
# print(Arith_Put_Basket(S, S, 0.3, 0.3, r, T, 80, 0.5, m, True, 10))
# print(Arith_Put_Basket(S, S, 0.3, 0.3, r, T, 120, 0.5, m, True, 10))
# print(Arith_Put_Basket(S, S, 0.5, 0.5, r, T, 100, 0.5, m, True, 10))