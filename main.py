from ecg_getters import get_signals, get_diagnosis_str, LEADS_NAMES, get_T_starts, get_T_ends, get_T_peaks, get_QRS_starts, get_QRS_ends, get_QRS_peaks, get_P_starts, get_P_peaks, get_P_ends
from UI import UI

import json
from pathlib import Path


if __name__ == "__main__":
    path_to_dataset = Path('LUDB\\ecg_data_200.json')
    with open(path_to_dataset, 'r') as file:
        dataset = json.load(file)

        # возьмем i-того  пациента датасета
        i=15
        patient_ids = list(dataset.keys())
        patient_id = patient_ids[i]

        # какие отведения хотим показать
        leads_names = LEADS_NAMES[0:3]

        # получаем сигналы этих отведений данного пациента
        signals = get_signals(patient_id=patient_id, dataset=dataset, leads_names=leads_names)
        text = str(patient_id) + ": "
        diagnosis = get_diagnosis_str(patient_id=patient_id, dataset=dataset)

        # получаем разметки этих отведений данного пациента
        delineations = []
        for name in leads_names:

            delin1 = get_T_starts(patient_id, dataset, lead_name=name)
            delin2 = get_T_ends(patient_id, dataset, lead_name=name)
            delin3 = get_T_peaks(patient_id, dataset, lead_name=name)

            delin4 = get_QRS_starts(patient_id, dataset, lead_name=name)
            delin5 = get_QRS_ends(patient_id, dataset, lead_name=name)
            delin6 = get_QRS_peaks(patient_id, dataset, lead_name=name)

            delin7 = get_P_starts(patient_id, dataset, lead_name=name)
            delin8 = get_P_ends(patient_id, dataset, lead_name=name)
            delin9 = get_P_peaks(patient_id, dataset, lead_name=name)

            #delineations.append(delin1 + delin2 + delin3) #  начало, пик, конец T волны
            delineations.append(delin7 + delin8 + delin9) #  начало, пик, конец P волны
            #delineations.append(delin3 + delin6 + delin9)  # пики всех трех волн

        # запускаем пользовательский интерфейс
        ui = UI(leads_names=leads_names, signals=signals, diagnosis=text + diagnosis, delineations=delineations)
