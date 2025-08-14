# Crash Predictor — Multi-System Under Count Strategy

This Streamlit app predicts "Crash" multipliers using an under-count strategy and tracks SOL balances across three betting systems: Flat, Fixed, and Martingale. Each system runs on three crash windows: last 20, 50, and 100 rounds.

## Features

- Upload CSV of multipliers or manually input multipliers.
- Predict "Above" or "Under" for the next round using last 20, 50, and 100 rounds.
- Track three separate betting systems for each window:
  - **Flat Bet:** 0.01 SOL per "Above" prediction.
  - **Fixed Bet:** 0.02 SOL per "Above" prediction.
  - **Martingale:** Doubles the bet after each loss on "Above" predictions, resets after a win.
- Reset or clear history and balances easily.
- Track prediction accuracy.

## Installation

1. Clone or download this repository.
2. Ensure Python 3.10+ is installed.
3. Install dependencies:

```bash
pip install -r requirements.txt

