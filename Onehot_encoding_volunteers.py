category_enc = pd.get_dummies(volunteer["category_desc"])
print(category_enc.head())

volunteer_enc = pd.concat([volunteer, category_enc], axis=1)

print(volunteer_enc[["category_desc", "Strengthening Communities", "Helping Neighbors in Need"]].tail())
