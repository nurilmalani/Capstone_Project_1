from tabulate import tabulate

data_dokter=[
    {'nama': 'dr. Farahi Inezwari','poli': 'umum', 'gender': 'Wanita', 'jadwal': 'senin,rabu,jumat' }, # Kode poli umum 11
    {'nama': 'dr. Greycia Winardi Sp.A, M.Sc, IBCLC. Sp. Anak','poli': 'anak', 'gender': 'Wanita', 'jadwal': 'rabu,kamis,jumat' }, # Kode poli anak 12
    { 'nama': 'dr. Steven Widjaya, Sp.PD-KKV. Sp. Penyakit Dalam','poli': 'penyakit dalam', 'gender':'Pria', 'jadwal':'senin,selasa,kamis' }, # Kode poli penyakit dalam 13
    { 'nama': 'dr. Michael Silalahi, Sp.OG','poli': 'obgyn', 'gender': 'Pria', 'jadwal': 'selasa,kamis,sabtu' }, ## Kode poli obgyn 14
    { 'nama': ' Prof. dr. Bambang Wiranata, SpTHT-KL','poli': 'THT-KL', 'gender': 'Pria', 'jadwal': 'senin,selasa,sabtu' },  # Kode poli THT 15
]

daftar_antrian={
    'senin':[{'no.rekam medis':110501,'nama':'Eko Triana','poli':'poli umum','antrian':1},{'no.rekam medis':144006,'nama':'Jessica Lara','poli':'poli penyakit dalam','antrian':2}],
    'selasa':[{'no.rekam medis':143402,'nama':'Diana Santa','poli':'poli obgyn','antrian':1}],
    'rabu':[{'no.rekam medis':111003,'nama':'Januar Dirganta','poli':'poli umum','antrian':1}],
    'kamis':[{'no.rekam medis':120104,'nama':'Asep Cahyono','poli':'poli anak','antrian':1}],
    'jumat':[{'no.rekam medis':123205,'nama':'Bellanita Rianda','poli':'poli anak','antrian':1}],
    'sabtu':[]
}


def duplikat(nomor):#Untuk melihat no.rekam medis yg ditambahkan/diupdate apakah duplikat
    empty_list=[]     
    for total_pasien in daftar_antrian.values():
        for pasien in total_pasien:
            if 'no.rekam medis' in pasien:
                empty_list.append(pasien['no.rekam medis'])
    if nomor in empty_list:
        return True
    return False

def update_values_antrian():#untuk mengupdate urutan antrian setelah mengubah jadwal hari/membatalkan janji
    for total_pasien in daftar_antrian.values():
        for idx in range(len(total_pasien)):
            total_pasien[idx]['antrian'] = idx +1

def submenu_1():
    while True:
        submenu=input('''\n    =============================
    \tData dokter & Antrian\n     Alexander Fleming Hospital
    =============================
    List Pilihan :
    1. Tampilkann Jadwal dokter
    2. Tampilkan Jadwal Hari 
    3. Tampilkan daftar Antrian
    4. Mencari antrian              
    5. Kembali ke Menu Utama 
    =============================
    Masukkan pilihan yang ingin dijalankan (1-5):''')
        if submenu.isdigit():
            submenu=int(submenu)
            if submenu >= 1 and submenu <=5:
                if submenu == 1:
                    menampilkan_jadwal_dokter()
                elif submenu == 2:
                    mencari_jadwal_hari()
                elif submenu == 3:
                    Memunculkan_daftar_antrian()
                elif submenu == 4:
                    memanggil_key_daftar_antrian()
                elif submenu == 5:
                    break
            else:
                print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t  = Hanya Masukan Angka 1-5 =\n\t=================================')
        else:
            print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t     = Hanya Masukan Angka =\n\t=================================')

def submenu_2():
    while True:
        submenu=input('''\n    =======================================
     Layanan Pendaftaran Registrasi Online\n\t   Alexander Fleming Hospital
    =======================================
    List Pilihan :
    1. Tambah Antrian Baru             
    2. Kembali ke Menu Utama 
    =======================================
    Masukkan pilihan yang ingin dijalankan (1-2):''')
        if submenu.isdigit():
            submenu=int(submenu)
            if submenu >= 1 and submenu <=2:
                if submenu == 1:
                    menambah_daftar_antrian()
                elif submenu == 2:
                    break
            else:
                print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t  = Hanya Masukan Angka 1-5 =\n\t=================================')
        else:
            print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t     = Hanya Masukan Angka =\n\t=================================')

def submenu_3():
    while True:
        submenu=input('''\n    =============================
     Layanan Perubahan Registrasi\n     Alexander Fleming Hospital
    =============================
    List Pilihan :
    1. Mengupdate Data Antrian            
    2. Kembali ke Menu Utama 
    =============================
    Masukkan pilihan yang ingin dijalankan (1-2):''')
        if submenu.isdigit():
            submenu=int(submenu)
            if submenu >= 1 and submenu <=2:
                if submenu == 1:
                    mengupdate_daftar_antrian()
                elif submenu == 2:
                    break
            else:
                print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t  = Hanya Masukan Angka 1-5 =\n\t=================================')
        else:
            print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t     = Hanya Masukan Angka =\n\t=================================')

def submenu_4():
    while True:
        submenu=input('''\n    ==============================
    Layanan Pembatalan Registrasi\n      Alexander Fleming Hospital
    ==============================
    List Pilihan :
    1. Membatalkan Antrian            
    2. Kembali ke Menu Utama 
    ==============================
    Masukkan pilihan yang ingin dijalankan (1-2):''')
        if submenu.isdigit():
            submenu=int(submenu)
            if submenu >= 1 and submenu <=2:
                if submenu == 1:
                    membatalkan_jadwal_antrian()
                elif submenu == 2:
                    break
            else:
                print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t  = Hanya Masukan Angka 1-5 =\n\t=================================')
        else:
            print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t     = Hanya Masukan Angka =\n\t=================================')

def menampilkan_jadwal_dokter(): #Menu -Read (Keseluruhan) - untuk jadwal dokter
    print('\n\t\t\t\tDaftar dokter Rumah Sakit Alexander Fleming Hospital\n') 
    empty_list=[] #sebagai wadah kosong untuk memasukkan data yang akan di append menggunakan for loop
    for i in range(len(data_dokter)):
        empty_list.append([i+1, data_dokter[i]['nama'], data_dokter[i]['poli'], data_dokter[i]['gender'], data_dokter[i]['jadwal']])
    print(tabulate(empty_list,headers=['No','Nama dokter','Poli','Jenis Kelamin','Jadwal'],tablefmt='double_outline',numalign='right',stralign='left'))
    return

def Memunculkan_daftar_antrian(): #Menu -Read (Keseluruhan) - untuk melihat daftar antrian
    data=[]
    for hari,pasien in daftar_antrian.items():
        x={}
        for i in range(len(pasien)):
            x=(pasien[i])
            x['Hari']= hari #untuk menambahkan data hari ke dalam dictionary pasien
            data.append(x)
    print(tabulate(data, headers="keys", tablefmt="double_outline"))
    return

def memanggil_key_daftar_antrian(): #Menu - Read (Key Value) - mencari data antrian berdasarkan no.rekam medis
    while True:
        nomor= (input('Masukan nomor rekam medis pasien:'))
        if nomor.isdigit():
            nomor=int(nomor)
            data={}
            for hari,list_pasien in daftar_antrian.items():
                for pasien in list_pasien:
                    if pasien['no.rekam medis'] == nomor: #Memanggil value rekam medis dalam data apakah sama dengan inputan
                        data=pasien.copy()
                        data['Hari']= hari
                        print('\nNomor rekam medis sudah terdaftar:')
                        print(tabulate([data], headers="keys", tablefmt="double_outline"))
                        return
            print('\n\t=================================\n\t=      No.Rekam Medis Anda      =\n\t     =   Belum Terdaftar   =\n\t=================================')     
        else:
            print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t     = Hanya Masukan Angka =\n\t=================================')

def mencari_jadwal_hari(): #Menu - read (Mencari berdasarkan hari) -melihat jadwal dokter berdasarkan ketersediaan hari
    while True:
        cari_hari=input('\nAnda ingin melihat jadwal di hari apa? (senin-sabtu)').lower()
        if cari_hari.isalpha():
            data=[]
            daftar_hari =['senin','selasa','rabu','kamis','jumat','sabtu']
            if cari_hari in daftar_hari:
                for i in range(len(data_dokter)):
                    nama_dokter={}
                    for key,val in data_dokter[i].items():
                        nama_dokter[key]=val #sebagai wadah untuk menambah key & val
                        check=[]
                        if key == 'jadwal':
                            check=val.split(',') #untuk memisah jadwal hari menjadi value satuan
                            if cari_hari in check:
                                data.append(nama_dokter)
                print(f'\nJadwal dokter di hari {cari_hari}')
                print(tabulate(data, headers="keys", tablefmt="double_outline"))
                return
                                   
            elif cari_hari == 'minggu':
                print('\n\t=================================\n\t=   Tidak ada poli yang buka   =\n\t     =   di Hari Minggu   =\n\t=================================')
            else:
                print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t     = Hanya Masukan Hari =\n\t=================================')
        else:
            print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t     = Hanya Masukan Huruf =\n\t=================================')
        
def menambah_daftar_antrian(): #Menu create - Menambahkan jadwal antrian/regist konsultasi bagi pasien
    daftar_hari =['senin','selasa','rabu','kamis','jumat','sabtu']
    for i in range(len(daftar_antrian)):
        regist_hari=input('\nPasien akan mendaftar di hari apa? (senin - sabtu) ').lower()
        if regist_hari.isalpha():
            if regist_hari in daftar_hari:
                while True:
                    nomor=input('\nMasukan nomor rekam medis pasien:')
                    if nomor.isdigit() == True:
                        nomor=int(nomor)
                        if duplikat(nomor) == False:
                            while True:
                                nama_depan=(input('\nMasukan nama depan pasien:')).capitalize()
                                if nama_depan.isalpha():
                                    while True:
                                        nama_belakang=(input('\nMasukan nama belakang pasien:')).capitalize()
                                        if nama_belakang.isalpha():
                                            while True:
                                                regist_poli=(input('''\n==================
Pilih Poli
==================
List Pilihan :
1. Poli Umum
2. Poli Penyakit Dalam
3. Poli Obgyn
4. Poli Anak
5. Poli THT
==================
Masukkan pilihan yang ingin dijalankan (1-5):'''))
                                                if regist_poli.isdigit():
                                                        regist_poli=int(regist_poli)
                                                        if regist_poli == 1:
                                                            regist_poli='umum'
                                                            data=[]
                                                            for dokter in data_dokter:
                                                                if 'jadwal' in dokter:
                                                                        jadwal_harian = dokter['jadwal'].split(',') #Memisahkan jadwal hari di data_dokter
                                                                        tersedia = {dokter['poli']: jadwal_harian}
                                                                        data.append(tersedia)
                                                            for item in data:
                                                                if regist_poli in item:#untuk check apakah poli tersedia di hari tersebut
                                                                    if regist_hari in item[regist_poli]:
                                                                        temporary={}
                                                                        antrian_baru=len(daftar_antrian[regist_hari][:])+1 #update nomor antrian
                                                                        temporary['no.rekam medis']=nomor
                                                                        temporary['nama']=(f'{nama_depan} {nama_belakang}')
                                                                        temporary['poli']=(f'poli {regist_poli}')
                                                                        temporary['antrian']=int(antrian_baru)
                                                                        temporary['hari']=regist_hari
                                                                        print(tabulate([temporary], headers="keys", tablefmt="double_outline"))
                                                                    else:
                                                                        print(f'Poli {regist_poli} Tidak tersedia di hari {regist_hari}')
                                                                        return
                                                            while True:
                                                                checker=input('Berikut data yang sudah anda input, lanjutkan menambahkan data? (y/t) ').lower()
                                                                if checker.isalpha():
                                                                    if checker == 'y':
                                                                        del temporary['hari'] #menghapus key hari sehingga ketika di print dalam table tidak terjadi duplikasi kolom
                                                                        daftar_antrian[regist_hari].append(temporary) #menambah data yg diperbaharui
                                                                        Memunculkan_daftar_antrian()
                                                                        print('Data Sudah berhasil ditambahkan')
                                                                        return
                                                                    elif checker.lower() == 't':
                                                                        print('Menambahkan Data Dibatalkan.')
                                                                        return
                                                                    else:
                                                                        print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')
                                                                else:
                                                                    print('pilihan yang anda masukan tidak valid, hanya masukan huruf')
                                                        elif regist_poli == 2:
                                                            regist_poli='penyakit dalam'
                                                            data=[]
                                                            for dokter in data_dokter:
                                                                if 'jadwal' in dokter:
                                                                        jadwal_harian = dokter['jadwal'].split(',')
                                                                        tersedia = {dokter['poli']: jadwal_harian}
                                                                        data.append(tersedia)
                                                            for item in data:
                                                                if regist_poli in item:
                                                                    if regist_hari in item[regist_poli]:
                                                                        temporary={}
                                                                        antrian_baru=len(daftar_antrian[regist_hari][:])+1 
                                                                        temporary['no.rekam medis']=nomor
                                                                        temporary['nama']=(f'{nama_depan} {nama_belakang}')
                                                                        temporary['poli']=(f'poli {regist_poli}')
                                                                        temporary['antrian']=int(antrian_baru)
                                                                        temporary['hari']=regist_hari
                                                                        print(tabulate([temporary], headers="keys", tablefmt="double_outline"))
                                                                    else:
                                                                        print(f'Poli {regist_poli} Tidak tersedia di hari {regist_hari}')
                                                                        return  
                                                            while True:
                                                                checker=input('Berikut data yang sudah anda input, lanjutkan menambahkan data? (y/t) ').lower()
                                                                if checker.isalpha():
                                                                    if checker == 'y':
                                                                        del temporary['hari'] #menghapus key hari sehingga ketika di print dalam table tidak terjadi duplikasi kolom
                                                                        daftar_antrian[regist_hari].append(temporary) #memperbaharui data
                                                                        Memunculkan_daftar_antrian()
                                                                        print('Data Sudah berhasil ditambahkan')
                                                                        return
                                                                    elif checker == 't':
                                                                        print('Menambahkan Data Dibatalkan.')
                                                                        return
                                                                    else:
                                                                        print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')
                                                                else:
                                                                    print('pilihan yang anda masukan tidak valid, hanya masukan huruf')
                                                        elif regist_poli == 3:
                                                            regist_poli='obgyn'
                                                            data=[]
                                                            for dokter in data_dokter:
                                                                if 'jadwal' in dokter:
                                                                        jadwal_harian = dokter['jadwal'].split(',')
                                                                        tersedia = {dokter['poli']: jadwal_harian}
                                                                        data.append(tersedia)
                                                            for item in data:
                                                                if regist_poli in item:
                                                                    if regist_hari in item[regist_poli]:
                                                                        temporary={}
                                                                        antrian_baru=len(daftar_antrian[regist_hari][:])+1 
                                                                        temporary['no.rekam medis']=nomor
                                                                        temporary['nama']=(f'{nama_depan} {nama_belakang}')
                                                                        temporary['poli']=(f'poli {regist_poli}')
                                                                        temporary['antrian']=int(antrian_baru)
                                                                        temporary['hari']=regist_hari
                                                                        print(tabulate([temporary], headers="keys", tablefmt="double_outline"))
                                                                    else:
                                                                        print(f'Poli {regist_poli} Tidak tersedia di hari {regist_hari}')
                                                                        return
                                                            while True:
                                                                checker=input('Berikut data yang sudah anda input, lanjutkan menambahkan data? (y/t) ').lower()
                                                                if checker.isalpha():
                                                                    if checker == 'y':
                                                                        del temporary['hari'] #menghapus key hari sehingga ketika di print dalam table tidak terjadi duplikasi kolom
                                                                        daftar_antrian[regist_hari].append(temporary)
                                                                        Memunculkan_daftar_antrian()
                                                                        print('Data Sudah berhasil ditambahkan')
                                                                        return
                                                                    elif checker == 't':
                                                                        print('Menambahkan Data Dibatalkan.')
                                                                        return
                                                                    else:
                                                                        print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')
                                                                else:
                                                                    print('pilihan yang anda masukan tidak valid, hanya masukan huruf')
                                                        elif regist_poli == 4:
                                                            regist_poli='anak'
                                                            data=[]
                                                            for dokter in data_dokter:
                                                                if 'jadwal' in dokter:
                                                                        jadwal_harian = dokter['jadwal'].split(',')
                                                                        tersedia = {dokter['poli']: jadwal_harian}
                                                                        data.append(tersedia)
                                                            for item in data:
                                                                if regist_poli in item:
                                                                    if regist_hari in item[regist_poli]:
                                                                        temporary={}
                                                                        antrian_baru=len(daftar_antrian[regist_hari][:])+1 
                                                                        temporary['no.rekam medis']=nomor
                                                                        temporary['nama']=(f'{nama_depan} {nama_belakang}')
                                                                        temporary['poli']=(f'poli {regist_poli}')
                                                                        temporary['antrian']=int(antrian_baru)
                                                                        temporary['hari']=regist_hari
                                                                        print(tabulate([temporary], headers="keys", tablefmt="double_outline"))
                                                                    else:
                                                                        print(f'Poli {regist_poli} Tidak tersedia di hari {regist_hari}')
                                                                        return
                                                            while True:
                                                                checker=input('Berikut data yang sudah anda input, lanjutkan menambahkan data? (y/t) ').lower()
                                                                if checker.isalpha():
                                                                    if checker == 'y':
                                                                        del temporary['hari'] #menghapus key hari sehingga ketika di print dalam table tidak terjadi duplikasi kolom
                                                                        daftar_antrian[regist_hari].append(temporary)
                                                                        Memunculkan_daftar_antrian()
                                                                        print('Data Sudah berhasil ditambahkan')
                                                                        return
                                                                    elif checker == 't':
                                                                        print('Menambahkan Data Dibatalkan.')
                                                                        return
                                                                    else:
                                                                        print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')
                                                                else:
                                                                    print('pilihan yang anda masukan tidak valid, hanya masukan huruf')
                                                        elif regist_poli == 5:
                                                            regist_poli='THT'
                                                            data=[]
                                                            for dokter in data_dokter:
                                                                if 'jadwal' in dokter:
                                                                        jadwal_harian = dokter['jadwal'].split(',')
                                                                        tersedia = {dokter['poli']: jadwal_harian}
                                                                        data.append(tersedia)
                                                            for item in data:
                                                                if regist_poli in item:
                                                                    if regist_hari in item[regist_poli]:
                                                                        temporary={}
                                                                        antrian_baru=len(daftar_antrian[regist_hari][:])+1 
                                                                        temporary['no.rekam medis']=nomor
                                                                        temporary['nama']=(f'{nama_depan} {nama_belakang}')
                                                                        temporary['poli']=(f'poli {regist_poli}')
                                                                        temporary['antrian']=int(antrian_baru)
                                                                        temporary['hari']=regist_hari
                                                                        print(tabulate([temporary], headers="keys", tablefmt="double_outline"))
                                                                    else:
                                                                        print(f'Poli {regist_poli} Tidak tersedia di hari {regist_hari}')
                                                                        return
                                                            while True:
                                                                checker=input('Berikut data yang sudah anda input, lanjutkan menambahkan data? (y/t) ').lower()
                                                                if checker.isalpha():
                                                                    if checker == 'y':
                                                                        del temporary['hari'] #menghapus key hari sehingga ketika di print dalam table tidak terjadi duplikasi kolom
                                                                        daftar_antrian[regist_hari].append(temporary)
                                                                        Memunculkan_daftar_antrian()
                                                                        print('Data Sudah berhasil ditambahkan')
                                                                        return
                                                                    elif checker == 't':
                                                                        print('Menambahkan Data Dibatalkan.')
                                                                        return
                                                                    else:
                                                                        print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')
                                                                else:
                                                                    print('pilihan yang anda masukan tidak valid, hanya masukan huruf')
                                                        else:
                                                            print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')
                                                else: print('Poli yang anda masukan tidak valid')
                                        else:
                                            print('Nama belakang yang anda masukan tidak valid, hanya masukan huruf')
                                else:
                                    print('Nama depan yang anda masukan tidak valid, hanya masukan huruf')
                        else:
                            print('\n\t====================================\n\t=     Data rekam medis duplikat    =\n\t====================================')
                    else:
                        print('\n\t====================================\n\t=  Opsi pilihan Anda tidak valid   =\n        =       Hanya masukan angka        =\n\t====================================')
            elif regist_hari == 'minggu':
                print('\n\t===========================================\n\t= Tidak ada poli yang buka di Hari Minggu =\n        =      Silahkan daftar di hari lain       =\n\t===========================================')
            else:
                print('\n\t====================================\n\t=  Opsi pilihan Anda tidak valid   =\n        = Hanya Masukan Hari Senin - Sabtu =\n\t====================================')
        else:
            print('\n\t====================================\n\t=  Opsi pilihan Anda tidak valid   =\n        = Hanya Masukan Hari Senin - Sabtu =\n\t====================================')

def mengupdate_daftar_antrian(): #Menu update - Mengubah jadwal konsultasi atau mengubah data yang terdaftar di antrian
    while True:
        nomor=input('Masukan No.Rekam Medis yang ingin di ubah? ')
        if nomor.isdigit():
            nomor=int(nomor)
            temporary={}
            for hari,total_pasien in daftar_antrian.items():
                for pasien in total_pasien:
                    temporary=pasien
                    temporary['Hari']=hari #menambah value hari 
                    for val in pasien.values():
                        if val == nomor:
                            print(tabulate([temporary], headers="keys", tablefmt="double_outline",))
                            while True:
                                checker=input('Apakah ini data yang ingin Anda ubah? (y/t)').lower()
                                if checker.isalpha():
                                    if checker == 'y':
                                        while True:
                                            ubah=(input('''\n==============================
Pilih Kolom yang ingin di ubah
==============================
List Pilihan :
1. Hari
2. Nama
3. Poli
4. No. Rekam Media
==============================
Masukkan pilihan yang ingin dijalankan (1-4):'''))
                                            if ubah.isdigit():
                                                ubah=int(ubah)
                                                cari_index=None
                                                if ubah == 1: #Hari
                                                    while True:
                                                        ubah_hari=input('Anda ingin merubah ke Hari apa?(senin-sabtu) ').lower()
                                                        if ubah_hari.isalpha():
                                                            daftar_hari=['senin','selasa','rabu','kamis','jumat','sabtu']
                                                            if ubah_hari in daftar_hari:
                                                                cari_index=daftar_antrian[hari].index(pasien) #cari index
                                                                temporary=pasien.copy()
                                                                temporary['Hari']=ubah_hari
                                                                temporary['antrian']= len(daftar_antrian[ubah_hari][:])+1 #mengupdate antrian
                                                                print(tabulate([temporary], headers="keys", tablefmt="double_outline",))
                                                                while True:
                                                                    checker=input('Lanjutkan merubah data? (y/t)').lower()
                                                                    if checker.isalpha():
                                                                        if checker == 'y':
                                                                            daftar_antrian[ubah_hari].append(pasien) #menambah data di hari baru
                                                                            daftar_antrian[ubah_hari][len(daftar_antrian[ubah_hari])-1]#klo ubah hari dapet antrian awal lagi
                                                                            del total_pasien[cari_index] #hapus data di hari sebelumnya
                                                                            update_values_antrian()
                                                                            Memunculkan_daftar_antrian()
                                                                            return
                                                                        elif checker == 't':
                                                                            print('\n\t=================================\n\t=   Batal Mengubah Data   =\n\t=================================')
                                                                            return
                                                                        else:
                                                                            print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')
                                                                    else:
                                                                        print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')

                                                            elif ubah_hari == 'minggu':
                                                                print('\n\t===========================================\n\t= Tidak ada poli yang buka di Hari Minggu =\n        =      Silahkan daftar di hari lain       =\n\t===========================================')
                                                            else:
                                                                print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')
                                                        else:
                                                            print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')
                                                                                                        
                                                elif ubah == 2: #Nama
                                                    while True:
                                                        first_name = input('Masukkan nama depan: ').capitalize()
                                                        if first_name.isalpha():
                                                            while True:
                                                                last_name = input('Masukkan nama belakang: ').capitalize()
                                                                if last_name.isalpha():
                                                                    temporary=pasien.copy()
                                                                    temporary['nama'] = f"{first_name} {last_name}"
                                                                    print(tabulate([temporary], headers="keys", tablefmt="double_outline",))
                                                                    while True:
                                                                        checker=input('Lanjutkan merubah data? (y/t)').lower()
                                                                        if checker.isalpha():
                                                                            if checker == 'y':
                                                                                pasien['nama'] = f"{first_name} {last_name}"
                                                                                Memunculkan_daftar_antrian()
                                                                                return
                                                                            elif checker == 't':
                                                                                print('Perubahan Data dibatalkan')
                                                                                return
                                                                            else:
                                                                                print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')
                                                                        else:
                                                                            print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')
                                                                else:
                                                                    print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')
                                                        else:
                                                            print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')
                                                elif ubah == 3: #Poli
                                                    while True:
                                                        ubah_poli=(input('''\n==================
Pilih Poli
==================
List Pilihan :
1. Poli Umum
2. Poli Penyakit Dalam
3. Poli Obgyn
4. Poli Anak
5. Poli THT
==================
Masukkan pilihan yang ingin dijalankan (1-5):'''))
                                                        if ubah_poli.isdigit():
                                                            ubah_poli=int(ubah_poli)
                                                            if ubah_poli == 1:
                                                                ubah_poli='umum'
                                                                temporary=pasien.copy()
                                                                temporary['poli'] =(f'poli {ubah_poli}') #mengubah value poli
                                                                print(tabulate([temporary], headers="keys", tablefmt="double_outline",))
                                                                checker=input('Lanjutkan merubah data? (y/t)').lower()
                                                                if checker.isalpha():
                                                                    if checker == 'y':
                                                                        pasien['poli'] =(f'poli {ubah_poli}')
                                                                        Memunculkan_daftar_antrian()
                                                                        return
                                                                    elif checker == 't':
                                                                        print('Perubahan Data dibatalkan')
                                                                        return
                                                                    else:
                                                                        print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')
                                                                else:
                                                                    print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')
                                                            elif ubah_poli == 2:
                                                                ubah_poli='penyakit dalam'
                                                                temporary=pasien.copy()
                                                                temporary['poli'] =(f'poli {ubah_poli}')
                                                                print(tabulate([temporary], headers="keys", tablefmt="double_outline",))
                                                                checker=input('Lanjutkan merubah data? (y/t)').lower()
                                                                if checker.isalpha():
                                                                    if checker == 'y':
                                                                        pasien['poli'] =(f'poli {ubah_poli}')
                                                                        Memunculkan_daftar_antrian()
                                                                        return
                                                                    elif checker == 't':
                                                                        print('Perubahan Data dibatalkan')
                                                                        return
                                                                    else:
                                                                        print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')
                                                                else:
                                                                    print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')
                                                            elif ubah_poli == 3:
                                                                ubah_poli='obgyn'
                                                                temporary=pasien.copy()
                                                                temporary['poli'] =(f'poli {ubah_poli}')
                                                                print(tabulate([temporary], headers="keys", tablefmt="double_outline",))
                                                                checker=input('Lanjutkan merubah data? (y/t)').lower()
                                                                if checker.isalpha():
                                                                    if checker == 'y':
                                                                        pasien['poli'] =(f'poli {ubah_poli}')
                                                                        Memunculkan_daftar_antrian()
                                                                        return
                                                                    elif checker == 't':
                                                                        print('Perubahan Data dibatalkan')
                                                                        return
                                                                    else:
                                                                        print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')
                                                                else:
                                                                    print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')
                                                            elif ubah_poli == 4:
                                                                ubah_poli='anak'
                                                                temporary=pasien.copy()
                                                                temporary['poli'] =(f'poli {ubah_poli}')
                                                                print(tabulate([temporary], headers="keys", tablefmt="double_outline",))
                                                                checker=input('Lanjutkan merubah data? (y/t)').lower()
                                                                if checker.isalpha():
                                                                    if checker == 'y':
                                                                        pasien['poli'] =(f'poli {ubah_poli}')
                                                                        Memunculkan_daftar_antrian()
                                                                        return
                                                                    elif checker == 't':
                                                                        print('Perubahan Data dibatalkan')
                                                                        return
                                                                    else:
                                                                        print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')
                                                                else:
                                                                    print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')
                                                            elif ubah_poli == 5:
                                                                ubah_poli='THT'
                                                                temporary=pasien.copy()
                                                                temporary['poli'] =(f'poli {ubah_poli}')
                                                                print(tabulate([temporary], headers="keys", tablefmt="double_outline",))
                                                                checker=input('Lanjutkan merubah data? (y/t)').lower()
                                                                if checker.isalpha():
                                                                    if checker == 'y':
                                                                        pasien['poli'] =(f'poli {ubah_poli}')
                                                                        Memunculkan_daftar_antrian()
                                                                        return
                                                                    elif checker == 't':
                                                                        print('Perubahan Data dibatalkan')
                                                                        return
                                                                    else:
                                                                        print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')
                                                                else:
                                                                    print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')
                                                            else:
                                                                print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')
                                                        else:
                                                            print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')       
                                                elif ubah == 4: #No. Rekam Medis
                                                    while True:
                                                        ubah_nomor=input('Masukan nomor rekam medis baru: ')
                                                        if ubah_nomor.isdigit():
                                                            ubah_nomor=int(ubah_nomor)
                                                            if duplikat(ubah_nomor) == False:
                                                                temporary=pasien.copy()
                                                                temporary['no.rekam medis'] =ubah_nomor
                                                                print(tabulate([temporary], headers="keys", tablefmt="double_outline",))
                                                                checker=input('Lanjutkan merubah data? (y/t)').lower()
                                                                if checker.isalpha():
                                                                    if checker == 'y':
                                                                        pasien['no.rekam medis'] =ubah_nomor
                                                                        Memunculkan_daftar_antrian()
                                                                        return
                                                                    if checker == 't':
                                                                        print('Perubahan Data dibatalkan')
                                                                        return
                                                                    else:
                                                                        print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')
                                                                else:
                                                                    print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')
                                                            else:
                                                                print('No.Rekam Medis yang Anda masukan duplikat')
                                                        else:
                                                            print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')   
                                                else:
                                                    print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')
                                            else:
                                                print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t     = Hanya Masukan Angka =\n\t=================================')                                  
                                    elif checker == 't':
                                        print('\n\t=================================\n\t=   Batal Mengubah Data   =\n\t=================================')
                                        return
                                    else:
                                        print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')
                                else:
                                    print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')          
        else:
            print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t     = Hanya Masukan Angka =\n\t=================================')

def membatalkan_jadwal_antrian(): #Menu Delete - untuk membatalkan janji konsultasi 
    while True:
        nomor=input('Masukan No.Rekam Medis yang ingin di batalkan? ')
        if nomor.isdigit():
            for hari,total_pasien in daftar_antrian.items():
                temporary={}
                for pasien in total_pasien:
                    temporary=pasien
                    temporary['Hari']=hari
                    for val in pasien.values():
                        nomor=int(nomor)
                        if val == nomor: 
                            print(tabulate([temporary], headers="keys", tablefmt="double_outline",))
                            while True:
                                checker=input('Apakah ini antrian yang ingin anda batalkan? (y/t)').lower()
                                if checker.isalpha():
                                    cari_index=None
                                    if checker == 'y':
                                        cari_index=daftar_antrian[hari].index(pasien) #cari index pasien 
                                        del total_pasien[cari_index] #hapus data berdasarkan index
                                        update_values_antrian()
                                        Memunculkan_daftar_antrian()
                                        return
                                    elif checker == 't':
                                        print('Menghapus Data dibatalkan.')
                                        return
                                    else:
                                        print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')
                                else:
                                    print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')
        else:
            print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t=================================')

while True: #Menu Utama
    pilihanMenu=(input('''\n    =============================
      Layanan Registrasi Online\n      Alexander Fleming Hospital
    =============================
    List Pilihan :
    1. Tampilkann Jadwal dokter
    2. Registrasi Konsul
    3. Mengubah Jadwal Konsul
    4. Membatalkan Jadwal Konsul
    5. Exit Program
    ==============================
    Masukkan pilihan yang ingin dijalankan (1-5):'''))
    if pilihanMenu.isdigit():
        pilihanMenu=int(pilihanMenu)
        if pilihanMenu >= 1 and pilihanMenu <=5:
            if pilihanMenu == 1:
                submenu_1()
            elif pilihanMenu == 2:
                submenu_2()
            elif pilihanMenu == 3:
                submenu_3()
            elif pilihanMenu == 4:
                submenu_4()
            elif pilihanMenu == 5:
                print('\n\t  ----------------\n\t    Terimakasih!\n\tSemoga Lekas Sembuh\n\t  ----------------\n')
                break
        else:
            print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t  = Hanya Masukan Angka 1-5 =\n\t=================================')
    else:
         print('\n\t=================================\n\t= Opsi pilihan Anda tidak valid =\n\t     = Hanya Masukan Angka =\n\t=================================')

                    









                        


                








