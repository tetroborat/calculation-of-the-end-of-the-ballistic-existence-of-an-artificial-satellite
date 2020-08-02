from math import cos,sin,pi,exp,acos,tan,asin,fmod,atan

def AgscToKeo(self,agsc):
    c1 = agsc[1]*agsc[5]-agsc[2]*agsc[4]
    c2 = agsc[2]*agsc[3]-agsc[0]*agsc[5]
    c3 = agsc[0]*agsc[4]-agsc[1]*agsc[3]
    c = (c1*c1+c2*c2+c3*c3)**0.5
    mu = 398600.4418
    M_PI = pi
    l1 = -mu*agsc[0]/pow(agsc[0]*agsc[0]+agsc[1]*agsc[1]+agsc[2]*agsc[2],0.5)+c3*agsc[4]-c2*agsc[5]
    l2 = -mu*agsc[1]/pow(agsc[0]*agsc[0]+agsc[1]*agsc[1]+agsc[2]*agsc[2],0.5)+c1*agsc[5]-c3*agsc[3]
    l3 = -mu*agsc[2]/pow(agsc[0]*agsc[0]+agsc[1]*agsc[1]+agsc[2]*agsc[2],0.5)+c2*agsc[3]-c1*agsc[4]
    l = (l1*l1+l2*l2+l3*l3)**0.5
    r = (agsc[0]*agsc[0]+agsc[1]*agsc[1]+agsc[2]*agsc[2])**0.5
    i = acos(c3/c)
    if (-c2/c/sin(i)>0):
        Om = (asin(c1/c/sin(i))+2*M_PI)%(2*M_PI)
    else:
        Om = M_PI-asin(c1/c/sin(i))
    if ((c1*l2-c2*l1)/l/c/sin(i)>0):
        om = (asin(l3/l/sin(i))+2*M_PI)%(2*M_PI)
    else:
        om = M_PI-asin(l3/l/sin(i))
    e = l/mu
    a = (c*c/mu)/(1-e*e)
    if (c*c-mu*r>0):
        tetta = (asin((c*(agsc[0]*agsc[3]+agsc[1]*agsc[4]+agsc[2]*agsc[5]))/(l*r))+2*M_PI)%(2*M_PI)
    else:
        tetta = M_PI-asin((c*(agsc[0]*agsc[3]+agsc[1]*agsc[4]+agsc[2]*agsc[5]))/(l*r))
    return a,e,180/pi*om,180/pi*Om,180/pi*i,180/pi*(tetta+om)
def ras(self,a,e,w,ww,i,u,sutki,cent,atm):
    mu,pi2,rz,wz = 398600.44,-1.7555 * 10 ** 10,6371,729211 / 10 ** 10
    ma, me, mw, mww, mi, mr, musut = [], [], [], [], [], [], []
    K,sh = 1,5
    SS, m, cx = 2, 935, 2
    c =  cx * SS / 2 / m
    sh,u,i,w,ww=map(lambda x:x*pi/180,[sh,u,i,w,ww])
    q,k,p = e * cos(w),e * sin(w),a * (1 - e ** 2)
    def ro(h):
        ii = 0
        a = [20, 60, 100, 150, 300, 600, 900], \
            [0.12522, 91907 / 10 ** 7, 31655 / 10 ** 9, 54733 / 10 ** 12,20474 / 10 ** 14, 19019 / 10 ** 16, 11495 / 10 ** 18,58038 / 10 ** 20],\
            [-20452 / 10 ** 13, 62669 / 10 ** 14,-86999 / 10 ** 14, 12870 / 10 ** 13, 10167 / 10 ** 14, 97266 / 10 ** 16,15127 / 10 ** 15, 0], \
            [90764 / 10 ** 9,16739 / 10 ** 8,12378 / 10 ** 8,17527 / 10 ** 8,45825 / 10 ** 9,19885 / 10 ** 9,14474 / 10 ** 9,39247 / 10 ** 10]
        for j in a[0]:
            if h <= j:    break
            if ii == 6:   break
            ii += 1
        return a[1][ii] * exp(a[2][ii] * (h - a[0][ii]) ** 2 - a[3][ii] * (h - a[0][ii]))
    def e(q, k):
        return (q ** 2 + k ** 2) ** 0.5
    def r(p, q, k, u, w):
        return p / (1 + e(q, k) * cos(u - w))
    def R(q, k, u):
        return 1 + q * cos(u) + k * sin(u)
    def vr(p, q, k, u, w):
        return (mu / p) ** 0.5 * e(q, k) * sin(u - w)
    def vt(p, q, k, u, w, i):
        return (mu / p) ** 0.5 * (1 + e(q, k) * cos(u - w)) - K * wz * r(p, q, k, u, w) * cos(i)
    def vw(p, q, k, u, w, i):
        return K * wz * r(p, q, k, u, w) * sin(i) * cos(u)
    def v(p, q, k, u, w, i):
        return (vr(p, q, k, u, w) ** 2 + vt(p, q, k, u, w, i) ** 2 + vw(p, q, k, u, w, i) ** 2) ** 0.5
    def S(p, q, k, u, w):
        return -c *atm* ro(r(p, q, k, u, w) - rz) * v(p, q, k, u, w, i) * vr(p, q, k, u, w) - cent * 1.5 * pi2 / r(p, q, k,u,w) ** 4 * (3 * sin(u) ** 2 * sin(i) ** 2 - 1)
    def T(p, q, k, i, u, w):
        return -c *atm* ro(r(p, q, k, u, w) - rz) * v(p, q, k, u, w, i) * vt(p, q, k, u, w, i) + cent * 1.5 * pi2 / r(p, q,k, u,w) ** 4 * sin(2 * u) * sin(i) ** 2
    def W(p, q, k, i, u, w):
        return -c *atm* ro(r(p, q, k, u, w) - rz) * v(p, q, k, u, w, i) * vw(p, q, k, u, w, i) + cent * 1.5 * pi2 / r(p, q,k, u,w) ** 4 * sin(u) * sin(2 * i)
    def gam(p, q, k, i, u):
        return 1 / (1 - p ** 2 / mu / R(q, k, u) * W(p, q, k, i, u, w) * sin(u) / tan(i))
    def dww(p, q, k, i, u):
        return gam(p, q, k, i, u) * p ** 2 / mu / R(q, k, u) ** 3 * sin(u) / sin(i) * W(p, q, k, i, u, w)
    def di(p, q, k, i, u):
        return gam(p, q, k, i, u) * p ** 2 / mu / R(q, k, u) ** 3 * cos(u) * W(p, q, k, i, u, w)
    def dp(p, q, k, i, u):
        return 2 * gam(p, q, k, i, u) * p ** 3 * T(p, q, k, i, u, w) / mu / R(q, k, u) ** 3
    def dq(p, q, k, i, u):
        return gam(p, q, k, i, u) * p ** 2 / mu / R(q, k, u) ** 2 * (S(p, q, k, u, w) * sin(u) + T(p, q, k, i, u, w) / R(q, k, u) * (q + cos(u) * (1 + R(q, k, u))) + W(p, q, k, i, u, w) * k * sin(u) / R(q, k,u) / tan(i))
    def dk(p, q, k, i, u):
        return gam(p, q, k, i, u) * p ** 2 / mu / R(q, k, u) ** 2 * (-S(p, q, k, u, w) * cos(u) + T(p, q, k, i, u, w) / R(q, k, u) * (k + sin(u) * (1 + R(q, k, u))) - W(p, q, k, i, u, w) * q * sin(u) / R(q, k,u) / tan(i))
    def cf(p, q, k, i, u):
        return dp(p, q, k, i, u) * sh, dq(p, q, k, i, u) * sh, dk(p, q, k, i, u) * sh, di(p, q, k, i, u) * sh, dww(p, q,k, i,u) * sh
    def runge(p, q, k, i, u):
        cf1 = cf(p, q, k, i, u)
        cf2 = cf(p + cf1[0] / 2, q + cf1[1] / 2, k + cf1[2] / 2, i + cf1[3] / 2, u + sh / 2)
        cf3 = cf(p + cf2[0] / 2, q + cf2[1] / 2, k + cf2[2] / 2, i + cf2[3] / 2, u + sh / 2)
        cf4 = cf(p + cf3[0], q + cf3[1], k + cf3[2], i + cf3[3], u + sh)
        A = [p, q, k, i, ww]
        for el in range(len(A)):
            A[el] += (cf1[el] + 2 * cf2[el] + 2 * cf3[el] + cf4[el]) / 6
        return A[0], A[1], A[2], A[3], A[4]
    while (u < sutki * 2 * pi):
        ma.append(p / (1 - e(q, k) ** 2))
        me.append(e(q, k))
        if q==k==0:
            mw.append(0)
        elif k / e(q, k) >= 0:
            mw.append(acos(q / e(q, k)) * 180 / pi)
        else:
            mw.append(360 - acos(q / e(q, k)) * 180 / pi)
        mww.append(ww * 180 / pi)
        mi.append(i * 180 / pi)
        mr.append(p / (1 + e(q, k) * cos(u - w)))
        musut.append(u/pi/2)
        p, q, k, i, ww = runge(p, q, k, i, u)
        if (p / (1 + e(q, k) * cos(u - w)) <= rz):
            return ma, me, mw, mww, mi, mr, musut
        u += sh
    return ma,me,mw,mww,mi,mr,musut