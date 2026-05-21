import re
from collections import Counter


def read_file(filename):
    """Membaca isi file teks."""
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def clean_words(text):
    """Membersihkan teks dan mengubah menjadi list kata."""
    text = text.lower()
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    return words


def count_lines(text):
    """Menghitung jumlah baris."""
    return len(text.splitlines())


def count_words(words):
    """Menghitung jumlah kata."""
    return len(words)


def top_words(words, n=5):
    """Mengambil n kata yang paling sering muncul."""
    counter = Counter(words)
    return counter.most_common(n)


def count_vowels_consonants(text):
    """Menghitung jumlah huruf vokal dan konsonan."""
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count


def generate_bar_chart(top_words_list):
    """Membuat grafik ASCII."""
    chart = ""
    for word, count in top_words_list:
        chart += f"{word:<15} {'#' * count}\n"
    return chart