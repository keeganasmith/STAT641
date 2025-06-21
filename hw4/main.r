b = seq(0.5, 5, .01)
LLK = b^(17) * exp(-7 * b) / 69120
plot(b, LLK, type="l")
LK_max = max(LLK)
bmax = which(LLK == LK_max)
print(LK_max)
print(bmax)
MLE = b[bmax]
print(MLE)