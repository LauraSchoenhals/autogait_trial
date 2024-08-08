#gets joint positions from H5 into csv
#should then edit csv to match DLC output with scorer, bodypart, and coords headers, see AutoGaitA documentation

import pandas as pd
import os

def get_col_names(joints):
    joint_likelihood = []
    for joint in joints:
        likelihood_name = f'{joint}_likelihood'
        joint_likelihood. append(likelihood_name)
    return(joint_likelihood)

def add_likelihood(df, likelihood_cols):
    for col in likelihood_cols:
        df[col] = 1
    return df

def save_file(file, directory, filtered):
    filename = os.path.splitext(os.path.split(file)[1])[0]
    savename = os.path.join(directory, filename)
    filtered.to_csv(f'{savename}.csv')

def main():
    group = "WT_levelwalk"
    directory = f'mouse-V3-analysis/data/kinematics-modeling-v1/{group}/h5'
    joints = ['ToeTip', 'Metatarsal', 'Ankle', 'Knee', 'Hip', 'IliacCrest']
    likelihood_cols = get_col_names(joints)

    file_list = [os.path.join(directory, file) for file in os.listdir(directory)]

    for file in file_list:
        input_df = pd.read_hdf(file, "df_kinematics")
        likelihood_df = add_likelihood(input_df, likelihood_cols)
        selected_col = [ 'IliacCrest_x', 'IliacCrest_y', 'IliacCrest_likelihood',
                        'Hip_x', 'Hip_y','Hip_likelihood',
                        'Knee_x', 'Knee_y', 'Knee_likelihood',
                        'Ankle_x', 'Ankle_y', 'Ankle_likelihood',
                        'Metatarsal_x', 'Metatarsal_y', 'Metatarsal_likelihood',
                        'ToeTip_x', 'ToeTip_y', 'ToeTip_likelihood']
        filtered = likelihood_df.loc[:, selected_col]

        save_dir = f"autogait_trial/csv_files/{group}"
        save_file(file, save_dir, filtered)

if __name__ == '__main__':
    main()
