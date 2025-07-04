library(survival)

df <- data.frame(
  time   = c(2391, 2815, 1884, 1656, 2184, 2118, 1905, 1375, 259, 1790, 2413, 2761, 1823),
  status = c(1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1)
)

km.fit <- survfit(Surv(time, status) ~ 1, data = df)

print(km.fit)
plot(km.fit,conf.int=FALSE,log=FALSE,
main="Kaplan-Meier Estimator of Survival Function",xlab="Strength of Cord",
ylab="Survival Function")
summary(km.fit)
print(km.fit, print.rmean=TRUE, rmean="individual")
# plot(
#   km.fit,
#   xlab = "Time",
#   ylab = "Survival Probability",
#   main = "Kaplan–Meier Survival Curve",
#   mark.time = TRUE,       # puts tick‐marks at censored observations
#   conf.int = FALSE         # draws the 95% confidence band
# )