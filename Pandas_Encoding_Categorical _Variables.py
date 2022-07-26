hiking["Accessible_enc"] = hiking["Accessible"].apply(lambda val: 1 if val == "Y" else 0)

print(hiking[["Accessible", "Accessible_enc"]].head())

