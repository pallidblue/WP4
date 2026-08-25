import mne
import numpy as np
from scipy.linalg import eigh

# we have 4 classes: left hand, right hand, feet and rest (needed for 1 of the games)

# 1. Baseline features: mu & beta rhythm.
def extract_bandpower_features(epochs, bands={"mu": (8,12), "beta": (18,26)}, tmin=1.0, tmax=3.0): 
    ...
    
#2. Spatial filtering: Common Spatial Patterns (CSP)
def extract_csp_features(epochs: mne.Epochs, tmin=0.5, tmax=3.5, n_components=4):
    ...

#3. Explore MNE feature extraction

def extract_mne_features(epochs: mne.Epochs, tmin=0.5, tmax=3.5):
    ...

#4. Frequency-domain features: PSD, ERD/S

def extract_psd_features(epochs: mne.Epochs, fmin=8, fmax=30, tmin=0.5, tmax=3.5):
    ...

#5. Compare feature extraction methods for best discrimination. 
#feature extraction methods: bandpower, CSP, MNE features, PSD

