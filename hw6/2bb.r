n = 100
B_sim = 50
true_mu = 100
count = 0
width_total = 0
for (i in 1:B_sim) {
    x_sim <- rexp(n, rate = 1/true_mu)
    thest = mean(x_sim)
    V = thest**2/n
    B = 9999
    W = numeric(B)
    W = rep(0,times =B)
    lambda_hat <- 1 / thest 
    for(i in seq_len(B)) {
    W[i] <- mean(rexp(n, rate = lambda_hat))
    }
    Z = sqrt(n)*(W-thest)/W
    Z = sort(Z)
    LZ = Z[250]
    UZ = Z[9750]
    thL <- thest - UZ * sqrt(V)
    thU <- thest - LZ * sqrt(V)
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