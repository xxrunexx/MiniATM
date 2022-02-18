import random, datetime
from customer import Customer

atm = Customer(id)

while True:

    pin = int(input("Masukkan Nomor Pin Anda : "))
    trial = 0

    while pin != atm.cek_custPin() and trial < 3:
        pin = int(input("Pin Anda Salah, Silahkan Masukkan Kembali : "))
        trial += 1

        if trial >= 3:
            print("Error. Silahkan Masukkan Ulang Kartu Anda")
            exit()

    while True:
        print("Selamat Datang Di ATM SuperBank")
        print("\n1. Cek Saldo \n2. Tarik Tunai \n3. Simpan \n4. Ganti Pin \n5. Keluar")
        menu = int(input("Silahkan Pilih Menu : "))
        # Cek Saldo
        if menu == 1:
            print("Saldo Anda Saat Ini : Rp. " + str(atm.cek_custBalance()) + "\n")
        # Tarik Tunai
        elif menu == 2:
            withdraw_amount = float(input("Silahkan Masukkan Nominal : "))
            verify_withdraw = input("Anda Akan Melakukan Transaksi Dengan Nominal Rp. " + str(withdraw_amount) + "? Y/N\n")
            if verify_withdraw == "y" or verify_withdraw == "Y":
                print("Saldo Awal Anda Rp. " + str(atm.cek_custBalance()))
            else:
                break
            if atm.cek_custBalance() > withdraw_amount:
                atm.withdrawBalance(withdraw_amount)
                print("Transaksi Berhasil, Saldo Anda Sekarang Rp. " + str(atm.cek_custBalance()))
            else:
                print("Saldo Anda Tidak Cukup Untuk Melakukan Transaksi Ini")
        # Deposit
        elif menu == 3:
            deposit_amount = float(input("Silahkan Masukkan Nominal : "))
            verify_deposit = input("Anda Akan Melakukan Transaksi Dengan Nominal Rp. " + str(deposit_amount) + "? Y/N\n")
            if verify_withdraw == "y" or verify_withdraw == "Y":
                atm.depositBalance(deposit_amount)
                print("Transaksi Berhasil. Saldo Anda Saat Ini Rp. " + str(atm.cek_custBalance()))
            else:
                break
        # Ganti Pin
        elif menu == 4:
            verify_pin = int(input("Silahkan Masukkan Pin Anda : "))
            while verify_pin != int(atm.cek_custPin()):
                verify_pin = int(input("Pin Anda Salah, Silahkan Masukkan Pin : "))
            updated_pin = int(input("Silahkan Masukkan Pin Baru Anda : "))
            while updated_pin == verify_pin:
                updated_pin = int(input("Pin Tidak Boleh Menggunakan Pin Lama, Silahkan Masukkan Pin Baru : "))
            while len(str(updated_pin)) != 4:
                updated_pin = int(input("Input Harus Berisi 4 Angka, Silahkan Masukkan Pin Baru : "))
            print("Pin Berhasil Diubah")
            verify_new_pin = int(input("Silahkan Masukkan Pin Anda : "))
            if verify_new_pin == updated_pin:
                print("Pin Anda Berhasil Diverifikasi!")
            else:
                print("Pin Anda Salah")
        # Exit
        elif menu == 5:
            print("===Resi Tercetak Otomatis Saat Anda Keluar.\nHarap Simpan Tanda Terima Ini Sebagai Bukti Transaksi===")
            print("No.\t\t: ", random.randint(100000, 999999))
            print("Tanggal\t\t: ", datetime.datetime.now())
            print("Saldo Akhir\t: ", atm.cek_custBalance())
            print("===Terima Kasih Telah Menggunakan ATM SuperBank===")
            exit()
        else:
            print("Harap Masukkan Angka Sesuai Pilihan Menu")
