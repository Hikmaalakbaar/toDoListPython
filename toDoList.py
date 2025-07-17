import os
from datetime import datetime
from colorama import init, Fore, Style

#Inisialisasi colorama
init(autoreset=True)

#file untuk menyimpan data
FILE_TODO = 'todo.txt'

#fungsi untuk memuat daftar tugas dari file
def load_todos():
    if not os.path.exists(FILE_TODO):
        return[]
    with open(FILE_TODO, 'r') as file:
        lines = file.readlines()
        return [line.strip() for line in lines]

#fungsi untuk simpan data ke file
def save_todos(todos):
    with open(FILE_TODO, 'w') as file:
        for todo in todos:
            file.write(todo + '\n')

# Menampilkan menu utama
def show_menu():
    print( Fore.CYAN + "\n=== TO-DO LIST ===")
    print("1. Tambah Tugas")
    print("2. Lihat Semua Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Keluar")

# Menjalankan program
def main():
    todos = load_todos() #Load data saat program pertama dijalankan

    while True:
        show_menu()
        choice = input('Pilih menu: ')

        if choice == '1':
            # Tambah tugas baru
            task = input('Masukkan nama tugas: ')
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            todos.append(f'[ ] {task} (ditambahkan pada {timestamp})')
            save_todos(todos)
            print( Fore.GREEN + 'Tugas Berhasil ditambahkan.')

        elif choice == '2':
            #Lihat semua tugas
            print( Fore.YELLOW +'\n=== Daftar Tugas ===')
            if not todos:
                print('Belum ada tugas.')
            else:
                for i, task in enumerate(todos, 1):
                    color = Fore.RED if "[x]" in task else Fore.WHITE
                    print(color + f"{i}. {task}")
        
        elif choice == '3':
            # Tandai tugas selesai
            if not todos:
                print('Tidak ada tugas untuk ditandai.')
                continue
            for i, task in enumerate(todos, 1):
                print(f'{i}. {task}')
            try:
                index = int(input('Masukan nomor tugas yang selesai: ')) - 1
                if  "[ ]" in todos[index]:  
                    todos[index] = todos[index].replace('[ ]', '[x]', 1)
                    save_todos(todos)
                    print( Fore.GREEN + 'Tugas ditandai sebagai selesai.')
                else:
                    print(Fore.YELLOW + 'Tugas sudah selesai sebelumnya.')
            except:
                print(Fore.RED + "Input Tidak Valid.")

        elif choice == '4':
            #Hapus Tugas
            if not todos:
                print('Tidak ada tugas untuk dihapus.')
                continue
            for i, task in enumerate(todos, 1):
                print(f'{i}. {task}')
            try:
                index = int(input('Masukkan nomor tugas yang ingin dihapus: ')) - 1
                deleted = todos.pop(index)
                save_todos(todos)
                print(Fore.GREEN + f'Tugas "{deleted}" berhasil dihapus.')
            except:
                print(Fore.RED + "Input Tidak Valid atau Nomor salah.")

        elif choice == '5':
            #Keluar dari program
            print(Fore.CYAN + 'Terima kasih telah menggunakan To-Do List!')
            break

        else:
            print(Fore.RED + 'Pilihan tidak valid. Silakan coba lagi.')

if __name__ == '__main__':
    main()