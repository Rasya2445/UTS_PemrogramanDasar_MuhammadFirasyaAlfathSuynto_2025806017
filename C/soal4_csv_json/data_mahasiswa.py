import csv
import json


def convert_csv_to_json():
    data = []

    try:
        # Membaca file CSV hasil dari program C (Soal 1)
        with open("data_mahasiswa.csv", "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                mahasiswa = {
                    "nama": row["Nama"],
                    "nim": row["NIM"],
                    "tugas": float(row["Tugas"]),
                    "uts": float(row["UTS"]),
                    "uas": float(row["UAS"]),
                    "nilai_akhir": float(row["NilaiAkhir"]),
                    "mutu": row["Mutu"]
                }
                data.append(mahasiswa)

        # Menghitung rata-rata nilai akhir
        if data:
            rata_rata = sum(m["nilai_akhir"] for m in data) / len(data)
            print(f"Rata-rata nilai akhir: {rata_rata:.2f}")
        else:
            print("Data kosong.")

        # Menampilkan data
        print("\n=== DATA MAHASISWA ===")
        for m in data:
            print(
                f"{m['nama']} | "
                f"{m['nim']} | "
                f"{m['nilai_akhir']:.2f} | "
                f"{m['mutu']}"
            )

        # Menyimpan ke file JSON
        with open("data_mahasiswa.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        print("\nData berhasil dikonversi ke data_mahasiswa.json")

    except FileNotFoundError:
        print("File data_mahasiswa.csv tidak ditemukan.")
        print("Jalankan Soal 1 terlebih dahulu dan pilih menu 'Simpan ke CSV'.")
    except Exception as e:
        print("Terjadi kesalahan:", e)


if __name__ == "__main__":
    convert_csv_to_json()