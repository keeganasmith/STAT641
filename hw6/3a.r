y <- c(10.75, 10.87, 10.92, 11.23, 11.26, 11.30, 11.31, 11.32, 11.39, 11.41, 11.52, 11.55,
11.58, 11.62, 11.62, 11.73, 11.77, 11.80, 11.88, 11.90, 11.93, 12.02, 12.10, 12.27)
n= length(y)
thest = 9 / 24
B = 9999
thestS = numeric(B)
thestS = rep(0,times =B)
for (i in 1:B)
thestS[i] = mean(sample(y,replace=T) > 11.7)
RS= sort(thestS-thest)
LRS = RS[250]
URS = RS[9750]
thL = thest-URS
thU = thest-LRS
thL
thU