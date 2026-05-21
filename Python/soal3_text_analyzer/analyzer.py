from utils import (
    read_file,
    clean_words,
    count_lines,
    count_words,
    top_words,
    count_vowels_consonants,
    generate_bar_chart
)


def analyze_text(input_file="input.txt", output_file="report.txt"):
    # Baca file
    text = read_file(input_file)

    # Proses kata
    words = clean_words(text)

    # Statistik
    total_lines = count_lines(text)
    total_words = count_words(words)
    top5 = top_words(words, 5)
    vowels, consonants = count_vowels_consonants(text)

    # Grafik
    chart = generate_bar_chart(top5)

    # Susun laporan
    report = f"""
===== LAPORAN ANALISIS TEKS =====

Jumlah Baris      : {total_lines}
Jumlah Kata       : {total_words}
Jumlah Vokal      : {vowels}
Jumlah Konsonan   : {consonants}

5 Kata Terbanyak:
"""

    for word, count in top5:
        report += f"- {word}: {count} kali\n"

    report += "\nGrafik Frekuensi Kata:\n"
    report += chart

    # Simpan ke file
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(report)

    # Tampilkan ke layar
    print(report)
    print(f"\nLaporan berhasil disimpan ke '{output_file}'")