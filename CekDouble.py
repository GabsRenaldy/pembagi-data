import pandas as pd

def cek_duplikat_nim(file_excel):
    df = pd.read_excel(file_excel, header=None)
    semua_data = pd.Series(df.values.flatten()).dropna().astype(str).str.strip()
    nim_data = semua_data[semua_data.str.match(r"^\d{10,13}$")]
    duplikat_nim = nim_data.value_counts()
    return duplikat_nim[duplikat_nim > 1]
