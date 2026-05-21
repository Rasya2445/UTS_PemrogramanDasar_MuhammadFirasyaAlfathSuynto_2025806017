#include <stdio.h>
#include "linked_list.h"

int main() {
    Mahasiswa *head = NULL;
    int pilihan;

    do {
        printf("\n===== MENU DATA MAHASISWA =====\n");
        printf("1. Tambah Mahasiswa\n");
        printf("2. Tampilkan Mahasiswa\n");
        printf("3. Cari Mahasiswa\n");
        printf("4. Hapus Mahasiswa\n");
        printf("5. Simpan ke CSV\n");
        printf("0. Keluar\n");
        printf("Pilih menu: ");
        scanf("%d", &pilihan);

        switch (pilihan) {
            case 1:
                addMahasiswa(&head);
                break;
            case 2:
                tampilMahasiswa(head);
                break;
            case 3:
                cariMahasiswa(head);
                break;
            case 4:
                hapusMahasiswa(&head);
                break;
            case 5:
                simpanCSV(head);
                break;
            case 0:
                freeList(head);
                printf("Program selesai.\n");
                break;
            default:
                printf("Pilihan tidak valid!\n");
        }

    } while (pilihan != 0);

    return 0;
}