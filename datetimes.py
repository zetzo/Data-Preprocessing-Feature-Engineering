print(volunteer[["created_date", "start_date_date", "end_date_date"]].head())

volunteer["start_date_converted"] = pd.to_datetime(volunteer["start_date_date"])

volunteer["start_date_month"] = volunteer["start_date_converted"].apply(lambda row: row.month)

print(volunteer[["start_date_converted", "start_date_month"]].head())

print(volunteer["start_date_converted"].apply(lambda row: row.day).head())

print(volunteer["start_date_converted"].apply(lambda row: row.year).head())
