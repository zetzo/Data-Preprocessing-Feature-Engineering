running_dict = {"name": ["Sue", "Mark", "Sean", "Erin", "Jenny", "Russell"], 
                "run1": [20.1, 16.5, 23.5, 21.7, 25.8, 30.9], 
                "run2": [18.5, 17.1, 25.1, 21.1, 27.1, 29.6], 
                "run3": [19.6, 16.9, 25.2, 20.9, 26.1, 31.4], 
                "run4": [20.3, 17.6, 24.6, 22.1, 26.7, 30.4], 
                "run5": [18.3, 17.3, 23.9, 22.2, 26.9, 29.9]}

running_times_5k = pd.DataFrame(running_dict)
print(running_times_5k)

run_columns = ["run1", "run2", "run3", "run4", "run5"]

running_times_5k["mean"] = running_times_5k.apply(lambda row: row[run_columns].mean(), axis=1)

print(running_times_5k)
