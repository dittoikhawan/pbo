def garis():
    print("----------------------------")

#tampilan menu
print("---------HOTEL SMK JP ONE-------")
print("-- lama inap ---- superior ------ duluxe -------- premium --")
print("-1 s.d 2 hari - 100.000/night - 150.000/night - 200.000/night -")
print("-3 s.d 4 hari - 90.000/night -- 135.000/night - 180.000/night -")
print("-5 hari keatas- 80.000/night -- 120.000/night - 160.000/night -")

#input data
tipe_kamar = input ("Masukan Tipe Kamar : ")
lama_inap = int(input("Masukan Lama Menginap : "))

#tipe_superior
#jika memilih tipe superior
if tipe_kamar == "superior":
    #jika lama menginap kurang atau sama dengan 2 hari 
    if lama_inap <= 2:
        total_harga = 100000*lama_inap
    #jika lama menginap kurang atau sama dengan 4 hari
    elif lama_inap <= 4:
        total_harga = 90000*lama_inap
    #jika lama menginap lebih dari 4 hari
    else:
        total_harga = 80000*lama_inap
    
#tipe_deluxe
#jika memilih tipe deluxe
elif tipe_kamar == "deluxe":
    #jika lama menginap kurang atau sama dengan 2 hari
    if lama_inap <= 2:
        total_harga = 150000*lama_inap
    #jika lama meninap kurang atau sama dengan 4 hari
    elif lama_inap <= 4:
        total_harga = 135000*lama_inap
    #jika lama menginap lebih dari 4 hari
    else:
        total_harga = 120000*lama_inap
    
#tipe_premium
#jika memilih tipe premium
elif tipe_kamar == "premium":
    #jika lama menginap kurang atau sama dengan 2 hari
    if lama_inap <= 2:
        total_harga = 200000*lama_inap
    #jika lama menginap kurang atau sama dengan 4 hari
    elif lama_inap <= 4:
        total_harga = 180000*lama_inap
    #jika lama menginap lebih dari 4 hari
    else:
        total_harga = 160000*lama_inap
    
#total harga menginap
garis()
print(" Tipe kamar yang dipilih : ",(tipe_kamar))
print(" Lama Menginap : ",(lama_inap)," Hari")
print(" Total harga yang dibayar : Rp.",(total_harga))
Home = input ('kembali kemenu utama (Y/N)?) 
If home == ("y") 
Garis () 
Judul () / tampilan menu
Codingan () semua codingan awal akhir input proses ouput
Else : 
Back


print("|---------------------------------------------------------------|")
print("| Lama Menginap |   Superior    |    Deluxe     |    Premium    |")
print("|---------------|---------------|---------------|---------------|")
print("|  1 - 2 Hari   | 100.000/Night | 150.000/Night | 200.000/Night |")
print("|  3 - 4 Hari   | 90.000/Night  | 135.000/Night | 180.000/Night |")
print("|   >5 Hari     | 80.000/Night  | 120.000/Night | 160.000/Night |")
print("|---------------|---------------|---------------|---------------|")
