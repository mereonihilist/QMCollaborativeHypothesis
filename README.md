# QMCollaborativeHypothesis

Companion repository for "Systematizing Observer-Dependence in Quantum Mechanics: A Testable Collaborative Hypothesis" by Matthew Richard Hubbard (2025).

## Overview

This repository supports quantum mechanics (QM) experiments testing the κ and MCI (Material Collaboration Index) framework for resolving observer-dependence paradoxes, such as the measurement problem. It will provide scripts, sample data, and reanalysis for reproducibility of the manuscript’s predictions, including qubit fidelity, CHSH entanglement correlations, and double-slit interference collapse.

Manuscript: [Link to be added post-submission, e.g., arXiv or journal DOI]

## Table of Contents

- [Overview](#overview)
- [Files](#files)
- [Usage](#usage)
- [License](#license)

## Files

- **mci_calculations/**: MCI scripts for qubits, entanglement (to be added).
  - `mci_qubits.py`: Computes MCI (~3–6) for qubit experiments using QDataSet (planned).
  - `mci_entanglement.py`: Computes MCI (~5–7) for entanglement experiments (planned).
  - `data/`:
    - `sample_qm9.csv`: QM9 dataset for double-slit detectors (Ramakrishnan et al., 2014, planned).
    - `sample_qdataset.csv`: QDataSet two-qubit simulation data (Perrier et al., 2022, Scientific Data, 9, 582, planned).
    - `sample_detector_data.csv`: UV detector efficiencies for BDT gap (Zhang et al., 2007; Palik, 1998, planned).
- **reanalysis/**: Reanalysis of CHSH experiments (to be added).
  - `aspect1982_analysis.py`: Aspect et al., 1982 (S ≈ 2.4–2.6, planned).
  - `hensen2015_analysis.py`: Hensen et al., 2015 (S = 2.38 ± 0.14, planned).
  - `kim2023_analysis.py`: Kim et al., 2023 (S ≈ 2.76, κ = 1.02 ± 0.03, planned).
- **qiskit_experiments/**:
  - `qubit_fidelity.ipynb`: Qiskit notebook simulating qubit fidelity (F ≈ 0.91, planned).
- **figures/**:
  - `figure4_decoherence_plot.py`: Plots interaction vs. decoherence rates at κ = 0.8, 10, 1.2 (planned).
- **LICENSE**: CC0 1.0 Universal license file.

## Usage

1. Install Python 3.8+, NumPy, Pandas, Matplotlib, and Jupyter Notebook.
2. Clone the repository: `git clone https://github.com/mereonihilist/QMCollaborativeHypothesis.git`
3. Scripts and data will be added soon. Planned usage:
   - Run `python mci_calculations/mci_qubits.py` for MCI calculations.
   - Open `qiskit_experiments/qubit_fidelity.ipynb` in Jupyter for fidelity simulation.
   - Run `figures/figure4_decoherence_plot.py` to generate Figure 4.
4. Ensure data files in `mci_calculations/data/` are accessible for scripts (to be added).

## License

This repository is licensed under CC0 1.0 Universal, allowing unrestricted use, modification, and distribution without attribution. See LICENSE for details.


## License

This repository is licensed under CC0 1.0 Universal, allowing unrestricted use, modification, and distribution without attribution. See LICENSE for details.
