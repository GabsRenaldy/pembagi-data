import pandas as pd
import random
from collections import defaultdict

def bagi_kelompok(file_excel, jumlah_kelompok):
    all_sheets = pd.read_excel(file_excel, sheet_name=None)
    df = pd.concat(all_sheets.values(), ignore_index=True) 
      
    if not {"NIM", "Nama", "Fakultas", "Program Studi"}.issubset(df.columns):
        raise ValueError("Kolom tidak lengkap")

    df['Nama'] = df['Nama'].fillna('').astype(str)
    data_maba = df.to_dict("records")

    kelompok = [[] for _ in range(jumlah_kelompok)]
    grouped_students = defaultdict(lambda: defaultdict(list))

    for maba in data_maba:
        grouped_students[maba["Fakultas"]][maba["Program Studi"]].append(maba)

    group_index = 0
    for fakultas in grouped_students:
        for prodi in grouped_students[fakultas]:
            random.shuffle(grouped_students[fakultas][prodi])
            for maba in grouped_students[fakultas][prodi]:
                kelompok[group_index].append(maba)
                group_index = (group_index + 1) % jumlah_kelompok

    output = []
    for i, anggota in enumerate(kelompok, start=1):
        for maba in anggota:
            output.append({
                "Kelompok": i,
                "NIM": maba["NIM"],
                "Nama": maba["Nama"],
                "Program Studi": maba["Program Studi"],
            })

    output_df = pd.DataFrame(output)
    output_file = "hasil_kelompok_terdistribusi.xlsx"
    output_df.to_excel(output_file, index=False)

    return output_file
