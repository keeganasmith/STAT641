x <- c(5.8, 10.1, 12.0, 12.5, 16.0, 18.6, 18.9, 19.0, 19.2, 19.6, 21.5, 22.3, 23.2, 23.3,
23.7, 24.3, 24.8, 25.2, 25.5, 25.9, 26.2, 26.3, 26.7, 26.8, 27.0, 27.1, 27.1, 27.1,
27.2, 28.1, 28.1, 28.3, 28.4, 28.4, 28.6, 28.7, 29.5, 29.6, 29.7, 30.0, 30.2, 30.2,
30.6, 30.8, 31.2, 31.5, 31.6, 31.8, 32.3, 32.4, 32.8, 33.1, 34.4, 34.6, 35.5, 36.6,
36.7, 38.0, 38.9, 39.2)
n = length(x)
Y = sum(x < 30)
p = Y / n
p_hat = (Y + 2) / (n + 4)
n_hat = n + 4
lower = p_hat - 1.96 * sqrt(p_hat * (1 - p_hat)) / sqrt(n_hat)
upper = p_hat + 1.96 * sqrt(p_hat * (1 - p_hat)) / sqrt(n_hat)
lower
upper

L=.95
P=.5
s=ceiling(n*P)-1
r=floor(n*P)+1
cov=0
while(s<n-1 && r>1 && cov<L)
{s=s+1
cov=pbinom(s-1,n,P)-pbinom(r-1,n,P)
if(cov>=L) break;
r=r-1
cov=pbinom(s-1,n,P)-pbinom(r-1,n,P)
}
x[r]
x[s]
cov


y <- c(5.8, 10.1, 12.0, 12.5, 16.0, 18.6, 18.9, 19.0, 19.2, 19.6, 21.5, 22.3, 23.2, 23.3,
23.7, 24.3, 24.8, 25.2, 25.5, 25.9, 26.2, 26.3, 26.7, 26.8, 27.0, 27.1, 27.1, 27.1,
27.2, 28.1, 28.1, 28.3, 28.4, 28.4, 28.6, 28.7, 29.5, 29.6, 29.7, 30.0, 30.2, 30.2,
30.6, 30.8, 31.2, 31.5, 31.6, 31.8, 32.3, 32.4, 32.8, 33.1, 34.4, 34.6, 35.5, 36.6,
36.7, 38.0, 38.9, 39.2)
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

y = (y^thmax - 1) / thmax
G = .95
P = .95
Chi = qchisq(1-(1 - G) / 2,n-1)
z = qnorm((1+P)/2)
K2Side = sqrt(((n-1)*(n+1)*z^2)/(n*Chi))
lower = mean(y) - K2Side * sd(y)
upper = mean(y) + K2Side * sd(y)
lower_transform = (lower * thmax + 1)^(1 / thmax)
upper_transform = (upper * thmax + 1)^(1 / thmax)
lower_transform
upper_transform
