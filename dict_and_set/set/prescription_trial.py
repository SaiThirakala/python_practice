from prescription_data import *

trial_patients = ['Denise', 'Eddie', 'Frank', 'Georgia', 'Kenny']

# Remove warfarin and add edoxaban
for patient in trial_patients:
    prescription = patients[patient]
    # if warfarin in prescription:
    #     prescription.remove(warfarin)
    #     prescription.add(edoxaban)
    # else:
    #     print(f'Patient {patient} is not taking Warfarin.\n'
    #           f'Remove {patient} from the trial.')
    try:
        prescription.discard(warfarin)
        prescription.add(edoxaban)
    except KeyError:
        print(f'Patient {patient} is not taking Warfarin.\n'
              f'Remove {patient} from the trial.')
    print(patient, prescription)