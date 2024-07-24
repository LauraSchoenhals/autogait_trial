"""
convert phase files to be put into AutoGaitA DLC Table
"""
import pandas as pd
import os
import numpy as np

def phase_to_line(phase_df):
    swing_starts = phase_df['swing'].tolist()[0:-1]
    swing_stops = phase_df['stance'].tolist()[0:-1]
    stance_stops = phase_df['swing'].tolist()[1:]
    phase_array = np.array([swing_starts, swing_stops, stance_stops]).T
    trial_line = phase_array.flatten() #convert the
    return trial_line


#read phase file
phase_dir = "autogait_trial/WT_levelwalk_phase"
phase_files = sorted(os.listdir(phase_dir))

rows_list = []
for filename in phase_files:
    filepath = os.path.join(phase_dir, filename)
    trial = pd.read_csv(filepath)
    nsteps = len(trial) - 1 #-1 because the last line always has only swing listed
    trial_line = phase_to_line(trial)
    trial_line_with_steps = np.append(nsteps, trial_line)
    # Convert the flattened array to a Series, using the filename as the name attribute
    row_series = pd.Series(trial_line_with_steps, name=filename)
    # Append the Series to the list
    rows_list.append(row_series)

# Convert the list of Series into a DataFrame
flattened_df = pd.DataFrame(rows_list)

save_name = "flattened_phase_files.xlsx"
save_path = os.path.join(os.path.split(phase_dir)[0], save_name)
flattened_df.to_excel(save_path, header = False, index = True)
