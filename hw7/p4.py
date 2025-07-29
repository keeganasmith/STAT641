import numpy as np
from scipy.stats import rankdata

def wilcoxon_signed_ranks(Y, mu0):
    """
    Computes Wilcoxon signed-rank components:
    1. Differences Xi = Yi - mu0
    2. Discard zeros and get n*
    3. Rank |Xi| with average ranks for ties
    4. Sum ranks for positive (W+) and negative (W-) Xi
    
    Parameters:
    -----------
    Y : array-like
        Observed values.
    mu0 : float
        Hypothesized median (or mean under H0).
    
    Returns:
    --------
    dict
        {
          'n_star': int,   # Number of nonzero differences
          'ranks': array,  # Ranks of |Xi| (only nonzero)
          'W_plus': float, # Sum of ranks where Xi > 0
          'W_minus': float # Sum of ranks where Xi < 0
        }
    """
    # Step 1: Compute differences
    X = np.asarray(Y) - mu0
    
    # Step 2: Keep only non-zero differences
    mask = X != 0
    X_nz = X[mask]
    n_star = X_nz.size
    
    # Step 3: Rank absolute differences
    abs_X = np.abs(X_nz)
    ranks = rankdata(abs_X, method='average')
    
    # Step 5: Sum ranks by sign
    W_plus = ranks[X_nz > 0].sum()
    W_minus = ranks[X_nz < 0].sum()
    
    return {
        'n_star': n_star,
        'ranks': ranks,
        'W_plus': W_plus,
        'W_minus': W_minus
    }

# Example usage:
Y = [10.14, 11.38, 10.93, 11.99, 10.15, 10.07, 10.02, 9.44, 9.39, 10.15,
9.94, 9.79, 10.24, 10.06, 11.63, 11.34, 9.88, 9.17, 9.80, 8.70]

def execute(mu0):
    result = wilcoxon_signed_ranks(Y, mu0)
    print(result["W_plus"], result["W_minus"])
Y = sorted(Y)
print(Y)
execute(10.24)

