#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "linked_list.h"

float hitungNilaiAkhir(float tugas, float uts, float uas) {
    return (0.3f * tugas) + (0.3f * uts) + (0.4f * uas);
}

char hitungMutu(float akhir) {
    if (akhir >= 85)
        return 'A';
    else if (akhir >= 70)
        return 'B';
    else if (akhir >= 60)
        return 'C';
    else if (akhir >= 50)
        return 'D';
    else
        return 'E';
}

void addMahasiswa(Mahasiswa **head) {
    Mahasiswa *baru = (Mahasiswa *)malloc(sizeof(Mahasiswa));

    if (baru == NULL) {
        printf("Gagal alokasi memori!\n");
        return;
    }

    printf("Nama         : ");
    getchar(); // membersihkan newline
    fgets(baru->nama, sizeof(baru->nama), stdin);
    baru->nama[strcspn(baru->nama, "\n")] = '\0';

    printf("NIM          : ");
    scanf("%s", baru->nim);

    printf("Nilai Tugas  : ");
    scanf("%f", &baru->tugas);

    printf("Nilai UTS    : ");
    scanf("%f", &baru->uts);

    printf("Nilai UAS    : ");
    scanf("%f", &baru->uas);

    baru->akhir = hitungNilaiAkhir(
        baru->tugas,
        baru->uts,
        baru->uas
    );

    baru->mutu = hitungMutu(baru->akhir);

    baru->next = *head;
    *head = baru;

    printf("\nData mahasiswa berhasil ditambahkan!\n");
}

void tampilMahasiswa(Mahasiswa *head) {
    if (head == NULL) {
        printf("\nData masih kosong.\n");
        return;
    }

    printf("\n====================================================================================\n");
    printf("%-20s %-15s %-8s %-8s %-8s %-12s %-5s\n",
           "Nama", "NIM", "Tugas", "UTS", "UAS", "Nilai Akhir", "Mutu");
    printf("====================================================================================\n");

    Mahasiswa *temp = head;
    while (temp != NULL) {
        printf("%-20s %-15s %-8.2f %-8.2f %-8.2f %-12.2f %-5c\n",
               temp->nama,
               temp->nim,
               temp->tugas,
               temp->uts,
               temp->uas,
               temp->akhir,
               temp->mutu);
        temp = temp->next;
    }

    printf("====================================================================================\n");
}

void cariMahasiswa(Mahasiswa *head) {
    char nim[20];
    printf("Masukkan NIM yang dicari: ");
    scanf("%s", nim);

    Mahasiswa *temp = head;
    while (temp != NULL) {
        if (strcmp(temp->nim, nim) == 0) {
            printf("\nData ditemukan:\n");
            printf("Nama        : %s\n", temp->nama);
            printf("NIM         : %s\n", temp->nim);
            printf("Nilai Akhir : %.2f\n", temp->akhir);
            printf("Mutu        : %c\n", temp->mutu);
            return;
        }
        temp = temp->next;
    }

    printf("Data tidak ditemukan.\n");
}

void hapusMahasiswa(Mahasiswa **head) {
    char nim[20];
    printf("Masukkan NIM yang akan dihapus: ");
    scanf("%s", nim);

    Mahasiswa *temp = *head;
    Mahasiswa *prev = NULL;

    while (temp != NULL && strcmp(temp->nim, nim) != 0) {
        prev = temp;
        temp = temp->next;
    }

    if (temp == NULL) {
        printf("Data tidak ditemukan.\n");
        return;
    }

    if (prev == NULL) {
        *head = temp->next;
    } else {
        prev->next = temp->next;
    }

    free(temp);
    printf("Data berhasil dihapus.\n");
}

void simpanCSV(Mahasiswa *head) {
    FILE *fp = fopen("data_mahasiswa.csv", "w");

    if (fp == NULL) {
        printf("Gagal membuat file CSV.\n");
        return;
    }

    fprintf(fp, "Nama,NIM,Tugas,UTS,UAS,NilaiAkhir,Mutu\n");

    Mahasiswa *temp = head;
    while (temp != NULL) {
        fprintf(fp,
                "%s,%s,%.2f,%.2f,%.2f,%.2f,%c\n",
                temp->nama,
                temp->nim,
                temp->tugas,
                temp->uts,
                temp->uas,
                temp->akhir,
                temp->mutu);
        temp = temp->next;
    }

    fclose(fp);
    printf("Data berhasil disimpan ke data_mahasiswa.csv\n");
}

void freeList(Mahasiswa *head) {
    Mahasiswa *temp;

    while (head != NULL) {
        temp = head;
        head = head->next;
        free(temp);
    }
}