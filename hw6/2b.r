n = 100
B_sim = 50
true_mu = 100
count = 0
width_total = 0
for (i in 1:B_sim) {
  x_sim <- rexp(n, rate = 1/true_mu)
  thest = mean(x_sim)
  B = 9999
  thestS = numeric(B)
  thestS = rep(0,times =B)
  for (i in 1:B)
  thestS[i] = mean(sample(x_sim,replace=T))
  RS= sort(thestS-thest)
  LRS = RS[250]
  URS = RS[9750]
  thL = thest-URS
  thU = thest-LRS
  width = thU - thL
  width_total = width_total + width
  if (thL <= true_mu && true_mu <= thU) {
    count <- count + 1
  }
}

cov <- count / B_sim
cov
width_avg = width_total / B_sim
width_avg