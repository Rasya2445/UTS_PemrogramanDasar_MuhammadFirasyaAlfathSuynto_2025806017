import csv
import json


def csv_to_json():
    data = []

    try:
        # Membaca file CSV
        with open("data_mahasiswa.csv", "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                mahasiswa = {
                    "nama": row["Nama"],
                    "nim": row["NIM"],
                    "nilai_akhir": float(row["NilaiAkhir"]),
                    "mutu": row["Mutu"]
                }
                data.append(mahasiswa)

        # Hitung rata-rata nilai akhir
        if data:
            rata_rata = sum(m["nilai_akhir"] for m in data) / len(data)
            print(f"Rata-rata nilai akhir: {rata_rata:.2f}")
        else:
            print("Data kosong.")

        # Tampilkan data
        print("\n=== DATA MAHASISWA ===")
        for mhs in data:
            print(
                f"{mhs['nama']} | "
                f"{mhs['nim']} | "
                f"{mhs['nilai_akhir']:.2f} | "
                f"{mhs['mutu']}"
            )

        # Simpan ke JSON
        with open("data_mahasiswa.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        print("\nData berhasil dikonversi ke data_mahasiswa.json")

    except FileNotFoundError:
        print("File data_mahasiswa.csv tidak ditemukan.")
    except Exception as e:
        print("Terjadi kesalahan:", e)


if __name__ == "__main__":
    csv_to_json()