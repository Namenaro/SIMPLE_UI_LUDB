######################### T - волна ####################################
def get_T_starts(patient_id, dataset, lead_name):
    points= []
    points_triplets = dataset[patient_id]['Leads'][lead_name]['Delineation']['t']
    for triplet in points_triplets:
        points.append(triplet[0])
    return points

def get_T_peaks(patient_id, dataset, lead_name):
    points = []
    points_triplets = dataset[patient_id]['Leads'][lead_name]['Delineation']['t']
    for triplet in points_triplets:
        points.append(triplet[1])
    return points

def get_T_ends(patient_id, dataset, lead_name):
    points = []
    points_triplets = dataset[patient_id]['Leads'][lead_name]['Delineation']['t']
    for triplet in points_triplets:
        points.append(triplet[2])
    return points

######################### P - волна ####################################
def get_P_starts(patient_id, dataset, lead_name):
    points= []
    points_triplets = dataset[patient_id]['Leads'][lead_name]['Delineation']['p']
    for triplet in points_triplets:
        points.append(triplet[0])
    return points

def get_P_peaks(patient_id, dataset, lead_name):
    points = []
    points_triplets = dataset[patient_id]['Leads'][lead_name]['Delineation']['p']
    for triplet in points_triplets:
        points.append(triplet[1])
    return points

def get_P_ends(patient_id, dataset, lead_name):
    points = []
    points_triplets = dataset[patient_id]['Leads'][lead_name]['Delineation']['p']
    for triplet in points_triplets:
        points.append(triplet[2])
    return points

######################### QRS - комплекс ####################################
def get_QRS_starts(patient_id, dataset, lead_name):
    points= []
    points_triplets = dataset[patient_id]['Leads'][lead_name]['Delineation']['qrs']
    for triplet in points_triplets:
        points.append(triplet[0])
    return points

def get_QRS_peaks(patient_id, dataset, lead_name):
    points = []
    points_triplets = dataset[patient_id]['Leads'][lead_name]['Delineation']['qrs']
    for triplet in points_triplets:
        points.append(triplet[1])
    return points

def get_QRS_ends(patient_id, dataset, lead_name):
    points = []
    points_triplets = dataset[patient_id]['Leads'][lead_name]['Delineation']['qrs']
    for triplet in points_triplets:
        points.append(triplet[2])
    return points