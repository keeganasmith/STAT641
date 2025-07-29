power_from_formula <- function(n, p0, p1, alpha = 0.05) {
  
  z_alpha <- qnorm(1 - alpha)
  
  inside_sqrt <- p0 * (1 - p0) / (p1 * (1 - p1))
  part_2 <- sqrt(n) * (p0 - p1) / sqrt(p1 * (1 - p1))
  1 - pnorm( z_alpha * sqrt(inside_sqrt) + part_2)
}

power_from_formula(200, .6, .55)
power_from_formula(200, .6, .6)
power_from_formula(200, .6, .65)
power_from_formula(200, .6, .7)
power_from_formula(200, .6, .75)
