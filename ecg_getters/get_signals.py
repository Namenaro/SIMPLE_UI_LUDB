import numpy as np

from ecg_getters import LEADS_NAMES

def get_signals(patient_id, dataset, leads_names=LEADS_NAMES):
    signals = []
    for lead_name in leads_names:
        signal = dataset[patient_id]['Leads'][lead_name]['Signal']
        signal = [s / 1000 for s in signal]  # делим на 1000, т.к. хотим в мВ, а в датасете в мкВ
        signals.append(np.array(signal))
    return signals