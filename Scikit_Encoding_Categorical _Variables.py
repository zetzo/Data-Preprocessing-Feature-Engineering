from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
hiking["Accessible_enc_le"] = le.fit_transform(hiking["Accessible"])

print(hiking[["Accessible", "Accessible_enc", "Accessible_enc_le"]].head())
