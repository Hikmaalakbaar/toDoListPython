import os

#file untuk menyimpan data
FILE_TODO = 'todo.txt'

#fungsi untuk load data dari file
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
    print("\n=== TO-DO LIST ===")
    print("1. Tambah Tugas")
    print("2. Lihat Semua Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Keluar")

# Menjalankan program
def main():
    todos = load_todos()
    while True:
        show_menu()
        choice = input('Pilih menu: ')

        if choice == '1':
            task = input('Masukkan nama tugas: ')
            todos.append(f'[ ] {task}')
            save_todos(todos)
            print('Tugas Berhasil ditambahkan.')

        elif choice == '2':
            print('\n=== Daftar Tugas ===')
            if not todos:
                print('Belum ada tugas.')
            else:
                for i, task in enumerate(todos, 1):
                    print(f"{i}. {task}")
        
        elif choice == '3':
            if not todos:
                print('Tidak ada tugas untuk ditandai.')
                continue
            for i, task in enumerate(todos, 1):
                print(f'{i}. {task}')
                index = int(input('Masukan nomor tugas yang selesai: ')) - 1
                if  todos[index].startswith('[ ]'):
                    todos[index] = todos[index].replace('[]', '[x]', 1)
                    save_todos(todos)
                    print('Tugas ditandai sebagai selesai.')
            else:
                print('Tugas sudah selesai sebelumnya.')

        elif choice == '4':
            if not todos:
                print('Tidak ada tugas untuk dihapus.')
                continue
            for i, task in enumerate(todos, 1):
                print(f'{i}. {task}')
            index = int(input('Masukkan nomor tugas yang ingin dihapus: ')) - 1
            deleted = todos.pop(index)
            save_todos(todos)
            print(f'Tugas "{deleted}" berhasil dihapus.')

        elif choice == '5':
            print('Terima kasih telah menggunakan To-Do List!')
            break

        else:
            print('Pilihan tidak valid. Silakan coba lagi.')

if __name__ == '__main__':
    main()