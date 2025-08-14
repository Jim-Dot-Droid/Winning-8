import streamlit as st
import pandas as pd
import numpy as np
import os

# File paths
HISTORY_FILE = "history.csv"
RESULTS_FILE = "results.csv"

# Base constants
INITIAL_BALANCE = 0.1
FLAT_BET = 0.01
FIXED_BET = 0.02
MARTINGALE_BASE_BET = 0.01

# Crash windows
WINDOWS = [20, 50, 100]

# Balance files
FLAT_FILES = {w: f"flat_{w}.txt" for w in WINDOWS}
FIXED_FILES = {w: f"fixe_
