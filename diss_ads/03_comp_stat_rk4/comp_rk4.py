import numpy as np
import sys

if len(sys.argv)!=7:
  print("Usage: python %s tpts dt Nsite ra rd rk4_file" % sys.argv[0])
  sys.exit()

# Take in Time and lattice size 
tpts = float(sys.argv[1])
dt = float(sys.argv[2])      # dt is from simulation for calculating time
time = tpts*dt               # ex. tpts=3000, dt=0.1, time=300 units of time
Nsite = int(sys.argv[3])
ra = float(sys.argv[4])
rd = float(sys.argv[5])
outfile = sys.argv[6]
delta = 0.005                # delta is for rk4 approximation

# Set up CME and arrays using switch-case structure
def Nsite2():
    size = int(float(time/delta))
    x2_rk = np.zeros((2, size+1))
    surf_cov = np.zeros(size+1) 
    times = np.linspace(0, time, size+1)
    
    def f2(t,y):
        A = y[0]
        B = y[1]
    
        dAdt = -ra*A + rd*B
        dBdt = ra*A - rd*B
    
        return np.array([dAdt, dBdt])
    
    x2_rk[:,0] = [1, 0]
    for i in range(0, size):
        k1 = f2(times[i], x2_rk[:,i])
        k2 = f2(times[i] + delta/2, x2_rk[:,i] + (delta/2)*k1)
        k3 = f2(times[i] + delta/2, x2_rk[:,i] + (delta/2)*k2)
        k4 = f2(times[i] + delta, x2_rk[:,i] + delta*k3)
        x2_rk[:,i+1] = x2_rk[:,i] + (delta/6)*(k1 + 2*k2 + 2*k3 + k4)
    
    for i in range(0,size+1):
        surf_cov[i] = float(x2_rk[0,i]*0) + float(x2_rk[1,i])
    
    file_name = outfile + '{}'.format(Nsite)
    np.savetxt(file_name, np.transpose([times, surf_cov]), fmt=['%e', '%e'], delimiter='      ', header='Time   Surface Coverage')
    return "rk4_file generated"
    
def Nsite3():
    size = int(float(time/delta))
    x3_rk = np.zeros((2, size+1))
    surf_cov = np.zeros(size+1) 
    times = np.linspace(0, time, size+1)
    
    def f3(t,y):
        A = y[0]
        B = y[1]
    
        dAdt = -3*ra*A + rd*B
        dBdt = 3*ra*A - rd*B
    
        return np.array([dAdt, dBdt])

    x3_rk[:,0] = [1, 0]
    for i in range(0, size):
        k1 = f3(times[i], x3_rk[:,i])
        k2 = f3(times[i] + delta/2, x3_rk[:,i] + (delta/2)*k1)
        k3 = f3(times[i] + delta/2, x3_rk[:,i] + (delta/2)*k2)
        k4 = f3(times[i] + delta, x3_rk[:,i] + delta*k3)
        x3_rk[:,i+1] = x3_rk[:,i] + (delta/6)*(k1 + 2*k2 + 2*k3 + k4)
    
    for i in range(0,size+1):
        surf_cov[i] = float(x3_rk[0,i]*0) + float(x3_rk[1,i]*(0.6666666667))
    
    file_name = outfile + '{}'.format(Nsite)
    np.savetxt(file_name, np.transpose([times, surf_cov]), fmt=['%e', '%e'], delimiter='      ', header='Time   Surface Coverage')
    return "rk4_file generated"
    
def Nsite4():
    size = int(float(time/delta))
    x4_rk = np.zeros((3, size+1))
    surf_cov = np.zeros(size+1) 
    times = np.linspace(0, time, size+1)
    
    def f4(t,y):
        A = y[0]
        B = y[1]
        C = y[2]
    
        dAdt = -4*ra*A + rd*B
        dBdt = 4*ra*A - (ra + rd)*B + 4*rd*C
        dCdt = -4*rd*C + ra*B
    
        return np.array([dAdt, dBdt, dCdt])
        
    x4_rk[:,0] = [1, 0, 0]
    for i in range(0, size):
        k1 = f4(times[i], x4_rk[:,i])
        k2 = f4(times[i] + delta/2, x4_rk[:,i] + (delta/2)*k1)
        k3 = f4(times[i] + delta/2, x4_rk[:,i] + (delta/2)*k2)
        k4 = f4(times[i] + delta, x4_rk[:,i] + delta*k3)
        x4_rk[:,i+1] = x4_rk[:,i] + (delta/6)*(k1 + 2*k2 + 2*k3 + k4)
    
    for i in range(0,size+1):
        surf_cov[i] = float(x4_rk[0,i]*0) + float(x4_rk[1,i]*(0.5)) + float(x4_rk[2,i])
        
    file_name = outfile + '{}'.format(Nsite)
    np.savetxt(file_name, np.transpose([times, surf_cov]), fmt=['%e', '%e'], delimiter='      ', header='Time   Surface Coverage')
    return "rk4_file generated"
    
def Nsite5():
    size = int(float(time/delta))
    x5_rk = np.zeros((4, size+1))
    surf_cov = np.zeros(size+1) 
    times = np.linspace(0, time, size+1)
    
    def f5(t,y):
        A = y[0]
        B = y[1]
        C = y[2]
        D = y[3]
        
        dAdt = -5*ra*A + rd*B
        dBdt = 5*ra*A - (2*ra + rd)*B + 2*rd*D
        dCdt = -ra*C + rd*D
        dDdt = 2*ra*B + ra*C - 3*rd*D
    
        return np.array([dAdt, dBdt, dCdt, dDdt])
           
    x5_rk[:,0] = [1, 0, 0, 0]
    for i in range(0, size):
        k1 = f5(times[i], x5_rk[:,i])
        k2 = f5(times[i] + delta/2, x5_rk[:,i] + (delta/2)*k1)
        k3 = f5(times[i] + delta/2, x5_rk[:,i] + (delta/2)*k2)
        k4 = f5(times[i] + delta, x5_rk[:,i] + delta*k3)
        x5_rk[:,i+1] = x5_rk[:,i] + (delta/6)*(k1 + 2*k2 + 2*k3 + k4)
    
    for i in range(0,size+1):
        surf_cov[i] = float(x5_rk[0,i]*0) + float(x5_rk[1,i]*(0.4)) + float(x5_rk[2,i]*(0.4)) + float(x5_rk[3,i]*(0.8))
        
    file_name = outfile + '{}'.format(Nsite)
    np.savetxt(file_name, np.transpose([times, surf_cov]), fmt=['%e', '%e'], delimiter='      ', header='Time   Surface Coverage')
    return "rk4_file generated"
    
def Nsite6():
    size = int(float(time/delta))
    x6_rk = np.zeros((6, size+1))
    surf_cov = np.zeros(size+1) 
    times = np.linspace(0, time, size+1)
    
    def f6(t,y):
        A = y[0]
        B = y[1]
        C = y[2]
        D = y[3]
        E = y[4]
        F = y[5]

        dAdt = -6*ra*A + rd*B
        dBdt = 6*ra*A - (3*ra + rd)*B + 2*rd*D + 2*rd*E
        dCdt = -2*ra*C + rd*D
        dDdt = 2*ra*B + 2*ra*C - ra*D - 3*rd*D + 6*rd*F
        dEdt = ra*B - 2*rd*E
        dFdt = ra*D - 6*rd*F
    
        return np.array([dAdt, dBdt, dCdt, dDdt, dEdt, dFdt])
           
    x6_rk[:,0] = [1, 0, 0, 0, 0, 0]
    for i in range(0, size):
        k1 = f6(times[i], x6_rk[:,i])
        k2 = f6(times[i] + delta/2, x6_rk[:,i] + (delta/2)*k1)
        k3 = f6(times[i] + delta/2, x6_rk[:,i] + (delta/2)*k2)
        k4 = f6(times[i] + delta, x6_rk[:,i] + delta*k3)
        x6_rk[:,i+1] = x6_rk[:,i] + (delta/6)*(k1 + 2*k2 + 2*k3 + k4)
    
    for i in range(0,size+1):
        surf_cov[i] = float(x6_rk[0,i]*0) + float(x6_rk[1,i]*(0.33333333333)) + float(x6_rk[2,i]*(0.3333333333333)) + float(x6_rk[3,i]*(0.66666666667)) + float(x6_rk[4,i]*(0.66666666667)) + float(x6_rk[5,i])
        
    file_name = outfile + '{}'.format(Nsite)
    np.savetxt(file_name, np.transpose([times, surf_cov]), fmt=['%e', '%e'], delimiter='      ', header='Time   Surface Coverage')
    return "rk4_file generated"
    
def Nsite7():
    size = int(float(time/delta))
    x7_rk = np.zeros((10, size+1))
    surf_cov = np.zeros(size+1) 
    times = np.linspace(0, time, size+1)
    
    def f7(t,y):
        A = y[0]
        B = y[1]
        C = y[2]
        D = y[3]
        E = y[4]
        F = y[5]
        G = y[6]
        H = y[7]
        I = y[8]
        J = y[9]

        dAdt = -7*ra*A + rd*B
        dBdt = 7*ra*A - 4*ra*B - rd*B + 2*rd*E + 2*rd*H
        dCdt = -3*ra*C + rd*F + rd*G + rd*I
        dDdt = -3*ra*D + rd*E + rd*F + rd*G
        dEdt = 2*ra*B + ra*D - 2*ra*E - 3*rd*E + 2*rd*J
        dFdt = ra*C + ra*D - ra*F - 2*rd*F + rd*J
        dGdt = ra*C + ra*D - ra*G - 2*rd*G + rd*J
        dHdt = 2*ra*B - ra*H - 2*rd*H + rd*J
        dIdt = ra*C - rd*I
        dJdt = 2*ra*E + ra*F + ra*G + ra*H - 5*rd*J
    
        return np.array([dAdt, dBdt, dCdt, dDdt, dEdt, dFdt, dGdt, dHdt, dIdt, dJdt])
           
    x7_rk[:,0] = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, size):
        k1 = f7(times[i], x7_rk[:,i])
        k2 = f7(times[i] + delta/2, x7_rk[:,i] + (delta/2)*k1)
        k3 = f7(times[i] + delta/2, x7_rk[:,i] + (delta/2)*k2)
        k4 = f7(times[i] + delta, x7_rk[:,i] + delta*k3)
        x7_rk[:,i+1] = x7_rk[:,i] + (delta/6)*(k1 + 2*k2 + 2*k3 + k4)
    
    for i in range(0,size+1):
        surf_cov[i] = float(x7_rk[0,i]*0) + float(x7_rk[1,i]*(0.285714285714)) + float(x7_rk[2,i]*(0.285714285714)) + float(x7_rk[3,i]*(0.285714285714)) + float(x7_rk[4,i]*(0.571428571429)) + float(x7_rk[5,i]*(0.571428571429)) + float(x7_rk[6,i]*(0.571428571429)) + float(x7_rk[7,i]*(0.571428571429)) + float(x7_rk[8,i]*(0.571428571429)) + float(x7_rk[9,i]*(0.857142857143))
        
    file_name = outfile + '{}'.format(Nsite)
    np.savetxt(file_name, np.transpose([times, surf_cov]), fmt=['%e', '%e'], delimiter='      ', header='Time   Surface Coverage')
    return "rk4_file generated"
    
def Nsite8():
    size = int(float(time/delta))
    x8_rk = np.zeros((11, size+1))
    surf_cov = np.zeros(size+1) 
    times = np.linspace(0, time, size+1)
    
    def f8(t,y):
        A = y[0]
        B = y[1]
        C = y[2]
        D = y[3]
        E = y[4]
        F = y[5]
        G = y[6]
        H = y[7]
        I = y[8]
        J = y[9]
        K = y[10]

        dAdt = -8*ra*A + rd*B
        dBdt = 8*ra*A - rd*B - 5*ra*B + 2*rd*D + 2*rd*E + 2*rd*F
        dCdt = -4*ra*C + rd*D + 2*rd*G + rd*H
        dDdt = 2*ra*B + ra*C -3*rd*D - 3*ra*D + 2*rd*I + rd*J
        dEdt = 2*ra*B - 2*rd*E - 2*ra*E + 2*rd*J
        dFdt = ra*B - 2*rd*F - 2*ra*F + rd*I
        dGdt = 2*ra*C - 2*rd*G - 2*ra*G + 2*rd*I
        dHdt = ra*C - rd*H - ra*H + rd*J
        dIdt = 2*ra*D + 2*ra*F + 2*ra*G - 5*rd*I - ra*I + 8*rd*K
        dJdt = ra*D + 2*ra*E + ra*H - 4*rd*J
        dKdt = ra*I - 8*rd*K
    
        return np.array([dAdt, dBdt, dCdt, dDdt, dEdt, dFdt, dGdt, dHdt, dIdt, dJdt, dKdt])
           
    x8_rk[:,0] = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, size):
        k1 = f8(times[i], x8_rk[:,i])
        k2 = f8(times[i] + delta/2, x8_rk[:,i] + (delta/2)*k1)
        k3 = f8(times[i] + delta/2, x8_rk[:,i] + (delta/2)*k2)
        k4 = f8(times[i] + delta, x8_rk[:,i] + delta*k3)
        x8_rk[:,i+1] = x8_rk[:,i] + (delta/6)*(k1 + 2*k2 + 2*k3 + k4)
    
    for i in range(0,size+1):
        surf_cov[i] = float(x8_rk[0,i]*0) + float(x8_rk[1,i]*0.25) + float(x8_rk[2,i]*0.25) + float(x8_rk[3,i]*0.5) + float(x8_rk[4,i]*0.5) + float(x8_rk[5,i]*0.5) + float(x8_rk[6,i]*0.5) + float(x8_rk[7,i]*0.5) + float(x8_rk[8,i]*0.75) + float(x8_rk[9,i]*0.75) + float(x8_rk[10,i])
        
    file_name = outfile + '{}'.format(Nsite)
    np.savetxt(file_name, np.transpose([times, surf_cov]), fmt=['%e', '%e'], delimiter='      ', header='Time   Surface Coverage')
    return "rk4_file generated"

def default():
    return "Nsite is not in range of supported RK4 approximations"
    
switcher = {
    2: Nsite2,
    3: Nsite3,
    4: Nsite4,
    5: Nsite5,
    6: Nsite6,
    7: Nsite7,
    8: Nsite8,
}

def switch(site):
    return switcher.get(site, default)()

# Running code with Nsite value
print(switch(Nsite))

