import numpy as np
import pandas as pd

def calculate_mci(data, kappa, alpha=1/np.log(2), beta=np.pi):
    # Note: alpha, beta derived for cavity QED; spin systems may vary
    I_mutual = data['entropy'].mean()  # From QDataSet
    return alpha * I_mutual * np.exp(-beta * np.abs(kappa - 1))

data = pd.read_csv('data/sample_qdataset.csv')
mci = calculate_mci(data, kappa=1.0)
print(f"MCI for qubits: {mci:.2f}")
