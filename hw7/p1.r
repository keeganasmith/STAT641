n = 36
df = n-1
muo = 10
sigma = .27
mu = seq(9,11,.05)
delta = sqrt(n)*(mu-muo)/sigma
power = 1-pt(qt(.975,df),df,delta) + pt(qt(.025, df), df, delta)
#par(lab=c(15,20,4))
plot(mu,power,type="l",ylim=c(0,1),xlab=expression(mu),
ylab="POWER")
title("POWER FUNCTION FOR t - Test")
out = cbind(mu,delta,power)


result = pt(-qt(.05, 19), 19, 0.3727)
result