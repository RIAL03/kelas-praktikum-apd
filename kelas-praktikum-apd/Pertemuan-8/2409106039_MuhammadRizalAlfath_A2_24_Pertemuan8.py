# try :
#     angka = int(input("Masukan angka: "))    
# except ValueError:
#     print("input tidak sesuai (wajib angka)")
    
# pilihan = int(input("Pilihan: "))

# if pilihan == 1:
#     print("Menu 1")
# elif pilihan == 2:
#     print("Menu 2")
# else:
#     print("Menu tidak ada")
# while True:    
#     try:
#         angka = int(input("Masukkan angka: "))
#     except ValueError:
#         print("Input yang anda masukkan bukan angka")
#     finally:
#         print("Program selesai")
        
#2 fungsi yang pertama menu dan kedua tambah 

# def menu():    
#     while True:
#         print("""
# 1. Tambah
# 2. Exit""")
#         while True:
#             try:
#                 a = int(input("Masukan Angka: "))
#                 break
#             except ValueError:
#                 print("Hanya bisa memasukan angka")
#         if a == 1:
#             print(tambah())
#         elif a == 2:
#             print("Kamu Keluar")
#             break
#         else:
#             print("Pilihan hanya sampai 2")
 
# def tambah():
#     print("Masukan Angka 1 dan 2")
#     while True:
#         try:
#             d = int(input("Masukan angka 1:")) 
#             break
#         except ValueError:
#             print("angka yang dimasukan salah")
#     while True:
#         try:    
#             v = int(input("Masukan angka 2:"))
#             break 
#         except ValueError:
#             print("angka yang dimasukan salah")
#     hasil = d + v
#     return hasil 

# menu()