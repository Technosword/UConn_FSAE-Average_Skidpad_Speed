import pandas as pd


def calc_average(file_path):
    speed_data = pd.read_csv(file_path, delimiter='\t')
    print(speed_data.columns)
    num_to_input = int(input("Number of wheel speed columns: "))
    wheel_speed_cols = []
    for i in range(num_to_input):
        wheel_speed_cols.append(input(f"Column {i}: "))
    wheel_speed_cols.append("Time (s)")
    wheel_speeds_time = speed_data[wheel_speed_cols]
    print("Columns inputted!")
    wheel_speeds_time.set_index("Time (s)", inplace=True)
    wheel_speeds_time = wheel_speeds_time.astype(float)
    while True:
        print("Type exit to exit!")
        start_str = input("Input starting time interval: ")
        finish_str = input("Input ending time interval: ")
        if start_str == 'exit' or finish_str == 'exit':
            break
        start = float(start_str)
        finish = float(finish_str)
        sliced_wheel_speeds_time = wheel_speeds_time.loc[start:finish]
        print(f"Average speed of all columns during the time interval ({start}, {finish}): {sliced_wheel_speeds_time.mean(axis=None)}")


file_path = input("File path: ")
#file_path = "UCONN_FSAE_CT14_MichiganS_MI_Generic_testing_a_3145.xls"
# calc_average(file_path)
print(calc_average(file_path))

