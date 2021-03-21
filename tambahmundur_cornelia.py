def cekInput(userInput): #fungsi untuk validasi input (no string, no decimal, tidak melebihi nilai maksimal)
    def cek(huruf): #fungsi untuk cek string dan decimal ('.')  input
        listAlfabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
        'o','p','q','r','s','t','u','v','w','x','y','z','.',',',' '] #listAlfabet berfungsi untuk validasi string dan decimal('.') input
        d = [char for char in huruf] #untuk memisahkan karakter dalam user input, tujuannya untuk validasi string dan decimal ('.') input
        if huruf in listAlfabet: #jika character di user input ada di listAlfabet maka function cek akan mengeluarkan value Yes
            return 'Yes'
    e = list(map(cek,userInput)) #jika user input ada di alfabet maka tampil 'Yes' dan di konversi menjadi list
    if 'Yes' in e or int(userInput) >359999 or int(userInput)<0 :#validasi string&decimal(jika ada 'Yes' di list e,input-an user mengandung string,decimal), max, negatif input          
        return 'Invalid Input!' #error message
x = input('Masukkan angka 1: ') #user input 1
y=0 #value awal nilai y supaya tidak error saat fungsi pertama kali dijalankan, karena value y baru bs di input setelah x lolos validasi
def tambahMundur(x,y): #fungsi tambah mundur
    while True:
        if cekInput(x) == 'Invalid Input!': #cek apakah output cekInput user Input 1 = Invalid Input!
            print(cekInput(x)) #jika output = Invalid input maka akan keluar notifikasi Invalid Input!
            break #kemudian program akan berhenti
        else:
            y = input('Masukkan angka 2: ') #user input 2
            if cekInput(y) == 'Invalid Input!': #cek apakah output cekInput user Input 2 = Invalid Input!
                print(cekInput(y)) #jika output = Invalid input maka akan keluar notifikasi Invalid Input!
                break #kemudian program akan berhenti
        intX = int(x[::-1]) #merubah urutan user input 1(x) dari blkg jadi ke depan dan menjadikan data type = int
        intY = int(y[::-1]) #merubah urutan user input 2(y) dari blkg jadi ke depan dan menjadikan data type = int
        sumXy = str(intX+intY)#menjumlahkan angka yang sudah di balik dan merubah data type menjadi string
        revSumXy = sumXy[::-1]#membalik hasil penjumlahan
        print('Hasil tambah mundurnya :',revSumXy)#mencetak output
        break #supaya looping while true (line 14) berhenti
tambahMundur(x,y)