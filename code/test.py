import numpy as np
import polars as pl

# Set seed, variable, and parameter values.
np.random.seed(42)
nobs = 500
beta0 = -5
beta1 = 5
beta2 = 2
beta3 = 0

# Simulate data.
sim_data = pl.DataFrame({
    'x1': np.round(np.random.uniform(0, 20, nobs)),
    'x2': np.random.choice(['level01', 'level02', 'level03'], nobs, p = [0.7, 0.2, 0.1]),
    'y': beta0 + beta1 * np.random.uniform(0, 20, nobs) + beta2 * (np.random.choice(['level01', 'level02', 'level03'], nobs, p=[0.7, 0.2, 0.1]) == 'level02') + beta3 * (np.random.choice(['level01', 'level02', 'level03'], nobs, p=[0.7, 0.2, 0.1]) == 'level03') + np.random.normal(0, 3, nobs)
})

print(sim_data)
