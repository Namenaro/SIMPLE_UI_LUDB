from ecg_getters import get_signals, get_diagnosis_str, LEADS_NAMES
from UI import UI

import json
from pathlib import Path

if __name__ == "__main__":
    path_to_dataset = Path('LUDB\\ecg_data_200.json')
    with open(path_to_dataset, 'r') as file:
        dataset = json.load(file)
        patient_ids =list(dataset.keys())

        patient_id = patient_ids[0]
        leads_names=LEADS_NAMES[6:]

        signals = get_signals(patient_id=patient_id, dataset=dataset, leads_names=leads_names)
        diagnosis = get_diagnosis_str(patient_id=patient_id, dataset=dataset)

        ui = UI(leads_names=leads_names, signals=signals, diagnosis=diagnosis)