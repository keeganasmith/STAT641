y <- c(10.75, 10.87, 10.92, 11.23, 11.26, 11.30, 11.31, 11.32, 11.39, 11.41, 11.52, 11.55,
11.58, 11.62, 11.62, 11.73, 11.77, 11.80, 11.88, 11.90, 11.93, 12.02, 12.10, 12.27)
n = length(y)
yt0 = log(y)
s = sum(yt0)
varyt0 = var(yt0)
Lt0 = -1*s - .5*n*(log(2*pi*varyt0)+1)
th = 0
Lt = 0
t = -3.01
i = 0
while(t < 3)
{t = t+.001
i = i+1
th[i] = t
yt = (y^t -1)/t
varyt = var(yt)
Lt[i] = (t-1)*s - .5*n*(log(2*pi*varyt)+1)
if(abs(th[i])<1.0e-10)Lt[i]<-Lt0
if(abs(th[i])<1.0e-10)th[i]<-0
}
# The following outputs the values of the likelihood and theta and yields
# the value of theta where likelihood is a maximum
out = cbind(th,Lt)
Ltmax= max(Lt)
Ltmax
imax= which(Lt==max(Lt))
thmax= th[imax]
thmax

y = (y^3 - 1) / 3
#now do the thing
n = length(y)
G = .90
P = .95
za = qnorm(G)
zb = qnorm(P)
a = 1-za^2/(2*(n-1))
b = zb^2-za^2/n
K1Side = (zb+sqrt(zb^2-a*b))/a
lower = mean(y) - K1Side * sd(y)
lower

lower_transform = (lower * 3 + 1)^(1/3)
lower_transform
# upper_transform = (upper * 3 + 1)^(1/3)
# lower_transform
# upper_transform
