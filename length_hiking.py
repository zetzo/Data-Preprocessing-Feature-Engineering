def return_mileage(length):
    if isinstance(length, str):
        pattern = re.compile(r"\d+\.\d+")
        mile = re.findall(pattern, length)
        if len(mile) == 1:
            return float(mile[0])
    else:
        return 0

hiking["Length Mileage"] = hiking["Length"].apply(lambda row: return_mileage(row))

print(hiking[["Length", "Length Mileage"]].head())
