color_ex = pd.Series(["blue", "red", "green", "red"])

color_enc = pd.get_dummies(color_ex)
print(color_enc)

print(pd.concat([color_ex, color_enc], axis=1))

