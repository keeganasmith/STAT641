library(survival)

df <- data.frame(
  time   = c(2391, 2815, 1884, 1656, 2184, 2118, 1905, 1375, 259, 1790, 2413, 2761, 1823),
  status = c(1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1)
)

km.fit <- survfit(Surv(time, status) ~ 1, data = df)

print(km.fit)
png("treatment1_survival.png", width=800, height=600)

plot(km.fit,conf.int=FALSE,log=FALSE,
main="Kaplan-Meier Estimator of Survival Function (Treatment 1)",xlab="Recovery Time",
ylab="Survival Function")
summary(km.fit)
print(km.fit, print.rmean=TRUE, rmean="individual")

df <- data.frame(
  time   = c(2312, 2501, 2691, 1548, 3329, 2154, 766, 1405, 1117, 232, 206, 2079),
  status = c(0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1)
)

km.fit <- survfit(Surv(time, status) ~ 1, data = df)

print(km.fit)
png("treatment2_survival.png", width=800, height=600)

plot(km.fit,conf.int=FALSE,log=FALSE,
main="Kaplan-Meier Estimator of Survival Function (Treatment 2)",xlab="Recovery Time",
ylab="Survival Function")
summary(km.fit)
print(km.fit, print.rmean=TRUE, rmean="individual")
