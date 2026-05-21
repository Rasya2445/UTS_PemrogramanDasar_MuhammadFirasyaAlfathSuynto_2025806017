#ifndef LINKED_LIST_H
#define LINKED_LIST_H

typedef struct Mahasiswa {
    char nama[100];
    char nim[20];
    float tugas;
    float uts;
    float uas;
    float akhir;
    char mutu;
    struct Mahasiswa *next;
} Mahasiswa;

// Fungsi utama
void addMahasiswa(Mahasiswa **head);
void tampilMahasiswa(Mahasiswa *head);
void cariMahasiswa(Mahasiswa *head);
void hapusMahasiswa(Mahasiswa **head);
void simpanCSV(Mahasiswa *head);
void freeList(Mahasiswa *head);

// Fungsi bantu
float hitungNilaiAkhir(float tugas, float uts, float uas);
char hitungMutu(float akhir);

#endif