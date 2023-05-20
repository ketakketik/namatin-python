# Ini komentar

"""
Kita bisa menulis string multiline dengan 3 tanda petik.
Berguna untuk menulis dokumen atau sejenisnya.
"""

########################## Data Promitive dan Operator ######################

# ini angka
3 # 3
-6 # -6

# operasi hitung
1 + 5 # 6
9 - 2 # 7
15 / 3 # 5.0

# hasil pembagian selalu bilangan desimal
3 / 2 # 1.5

# Pembagian bilangan bulat, hasilnya akan dibulatkan ke bawah
12 // 5 # 2
7 // -3 # -2
5.0 // 2.0 # 2.0 ini berlaku ke bilangan desimal juga
5.0 // -2.0 # -2.0 

# modulus, mencari sisa pembagian
10 % 5 # 0
7 % 2 # 1

# pangkat
2**5 # 32

# prioritas perhitungan
1 + 2 * 5 # 11
(1 + 2) * 5 # 15

# Boolean (perhatikan huruf kapital di awal)
True
False

# negasi
not True # False
not False # True

# operasi boolean
True and False # False
True or False # True

# True bernilai 1, False bernilai 0
True + True # 2
False - 10 # -10

# Operator pembanding
0 == False # True
10 > True # True
-5 == False # False
-2 != True # True

# None, 0, dan strings/list/dicts/tuples/sets yang kosong dianggap False
bool(0) # False
bool("") # False
bool([]) # False
bool({}) # False
bool(set()) # False
bool(10) # True
bool(-69) # True

# Menggunakan operator boolean pada bilangan akan mengubahnya menjadi boolean untuk dievaluasi, namun nilai yang dikembalikan tidak berubah
-2 or 0 # -2
-2 and 0 # 0

# kesetaraan
2 == 2 # True
-3 == 9 # False

# Ketidaksetaraan
2 != 1 # True
2 != 2 # False

# Pembanding
2 < 5 # True
2 > 4 # False
2 <= 2 # True
5 >= 10 # False

# Mengecek apakah suatu angka berada di rentang tertentu
5 > 2 and 2 > 1 # True
5 > 2 > 1 # True
5 < 2 and 2 > 1 # False
5 < 2 > 1 # False

# is mengecek 2 variable apakah objek yang sama, sedangkan == mengecek apakah
# 2 variable memiliki nilai yang sama.
a = [0, 1, 2, 3] # list a
b = a # mengarahkan b ke objek yang sama, yaitu a dalam memori
b is a # True, karena a dan b merujuk ke objek yang sama dalam memori
b == a # True, karena a dan b punya nilai yang sama
b = [0, 1, 2, 3] # list b
b is a # False, karena a dan b sudah tidak merujuk ke objek yang sama dalam memori
b == a # True, karena a dan b punya nilai yang sama

# String dapat dibuat dengan menggunakan kutip tunggal (') atau kutip ganda ("")
'ini string'
"ini juga string"

# string dapat ditambahkan dengan string lain
'halo' + 'dunia' + 'tipu-tipu' # halo dunia tipu-tipu

# string literal (bukan string sebagai nilai variable) dapat ditambahkan tanpa menggunakan tanda +
'halo' 'dunia' 'tipu-tipu' # halo dunia tipu-tipu

# string dapat diperlakukan sebagai list
'halo dunia tipu-tipu'[1] # a

# mencari panjang string
len("halo dunia tipu-tipu") # 20

# f-string digunakan untuk menyisipkan variable di dalam {} dan dievaluasi 
# dan digabungkan dengan string
nama = "Agus"
f"Hai namaku {nama} dan namaku terdiri dari {len(nama)} karakter" # Hai namaku Agus dan namaku terdiri dari 4 karakter

# None adalah objek yang menunjukan ketiadaan
None # None

# Gunakan is alih-alih == untuk memeriksa None
"Aku" is None # False
None is None # True

########################################## Variable dan Koleksi (list, tupple, dict, set) ==========================================

# fungsi print
print("Hai dunia tipu-tipu, saya baru belajar Python") # Hai dunia tipu-tipu, saya baru belajar Python

# fungsi print() mencetak newline di akhir kembaliannya.
# gunakan end untuk mengubah akhirannya.
print("halo dunia", end="")
print('tipu-tipu')
# halo duniatipu-tipu

# menentukan nilai variable dari input pada konsol
input_variable = input("Nama: ")
print(f"Hai dunia tipu-tipu nama saya {input_variable} dan sekarang sedang belajar python")

# tidak ada deklarasi variable, variable yang dibuat harus diberikan nilainya.
# konvensi penamaan variable adalah huruf_kecil_dengan_garis_bawah_sebagai_spasi
ini_variable = 10
print(ini_variable)

# mengakses variable yang belum dinyatakan dengan nilai akan terjadi exception
# ini_error
# print(ini_error) # NameError

# if dapat digunakan untuk mengevaluasi kondisi dan mengembalikan nilai berdasarkan kondisi tersebut
# int() mengubah nilai menjadi int atau integer
x = int(input("masukan angka: "))
apakah_x_genap = "genap" if x % 2 == 0 else "ganjil"
print(apakah_x_genap)

# list
ini_list = [] # list kosong
ini_list_lain = [1, 2, 3, 4]
print(ini_list)
print(ini_list_lain)

# menambah dan menghapus nilai list
ini_list.append(1)
print(ini_list)
ini_list.append(10)
print(ini_list)
ini_list.append(3)
print(ini_list)
ini_list.pop() # menghapus nilai list yang ada di akhir
print(ini_list)
ini_list.append(3)
ini_list.append(14)
print(ini_list)

# mengakses elemen list dengan indeks. indeks bilangan positif dimulai dari 0 dan mengindeks dari kiri ke kanan
print(ini_list)
print(ini_list[0])
print(ini_list[2])
# indeks bilangan negatif dimulai dari -1 dan meengindeks dari kanan ke kiri
print(ini_list[-1])
print(ini_list[-2])

# Jika mengakses elemen melebihi panjang indeks akan terjadi IndexError
# print(ini_list[5])

# melihat rentang elemen list
# [awal:akhir:langkah]
print(ini_list)
print(ini_list[1:3])
print(ini_list[:2])
print(ini_list[2:])
print(ini_list[::2])
print(ini_list[::-1])

# menyalin elemen list menggunakan [:]
sama_ini_list = ini_list[:]
print(sama_ini_list)
# tetapi objeknya berbeda, sehingga akan mengembalikan nilai False jika dibandingkan dengan is
print(sama_ini_list is ini_list)

# menghapus elemen berdasarkan indeksnya
ini_list.append(9)
del ini_list[1]
print(ini_list)

# menghapus kemunculan pertama elemen list
ini_list.append(3)
ini_list.remove(3)
print(ini_list)

# menyisipkan elemen ke indeks tertentu
# insert(indeks, elemen)
ini_list.insert(1, 3)
print(ini_list)

# mendapatkan indeks dari elemen pertama yang ditemukan
print(ini_list.index(3))

# menggabungkan list
list_gabungan = ini_list + ini_list_lain + sama_ini_list
print(list_gabungan)

# menambahkan atau menggabungkan bisa menggunakan extend
list_gabungan.extend([100, 23])
print(list_gabungan)

# mengecek keberadaan elemen
print(3 in list_gabungan)
print(98 in list_gabungan)

# melihat panjang indeks list
print(len(list_gabungan))

# tuples seperti list tapi immutable
ini_tuples = (1, 2, 3)
print(ini_tuples[1])
# ini_tuples[1] = 1 # error

# saat membuat tupple dengan panjang 1, harus diakhiri dengan koma
# selain 1, bahkan tupple kosong tidak perlu
# karena jika tupple dengan panjang 1 tidak diberi koma di akhir, akan diperlakukan seperti integer
print(type(1))
print(type((1,)))
print(type(()))

# dapat melakukan operasi pada tuples seperti list
# memeriksa panjang tuple
print(len(ini_tuples))
# menggabungkan tupple
print(ini_tuples + (2, 3, 4))
# slicing tuple
print(ini_tuples[:-1])
# memeriksa elemen tupple
print(3 in ini_tuples)

# kita dapat membongkar nilai tupple dan menugaskan ke variable
a, b, c = (1, 2, 3)
print(a, b, c)
a, *b, c = (1, 2, 3, 4)
print(a, b, c)
d, e, f = 4, 5, 6
print(d, e, f)
d, e = e, d
print(d, e, f)

# dict seperti mapping pada solidity, ia menyimpan pasangan key dan value
# nama_dict = {key1: value1, key2: value2, key3: value3}
dict_kosong = {}
dict_presiden = {"nama": "Jokowi", "usia": 56, "jenis kelamin": "Laki-laki", "Agama": "Islam"}

# pada dict, key haruslah tipe data yang tidak bisa diubah
# supaya dapat dikonversi menjadi hash dalam rangka pencarian nilai
# dict_list = {[1, 2, 3]: [1, 2, 3]} # error bang, list sebagai dapat diubah
dict_tup = {(1, 2, 3): [1, 2, 3]}

# mengakses nilai dict
# nama_dict[key]
print(dict_presiden["nama"])

# kita bisa mendapatkan semua key sebagai iterable dengan kata kunci keys()
# misalnya kita dapat memasukan key ke list
data_list = list(dict_presiden.keys())
print(data_list)

# kita dapat mendapatkan semua value sebagai iterable dengan kata kunci values()
# misalnya kita dapat memasukan value ke list
nilai_data_list = list(dict_presiden.values())
print(nilai_data_list)

# memeriksa keberadaan key pada dict
# case-sensitive
print("nama" in dict_presiden)
print("Nama" in dict_presiden)

# error jika melihat value dari key yang tidak ada
# print(dict_presiden["istri"])

# bisa gunakan get() untuk menghindari error
print(dict_presiden.get("istri"))
print(dict_presiden.get("nama"))

# get() dapat diberikan nilai kembalian default jika key tidak ditemukan
print(dict_presiden.get("istri", 9))
print(dict_presiden.get("nama", 9))

# setdefault() digunakan untuk menyisipkan key-value jika key tidak ditemukan
print(dict_presiden.setdefault("istri", "Iriana"))
print(dict_presiden.setdefault("istri", 1))

# update dict
dict_presiden.update({"suku": "Jawa"})
dict_presiden["masa jabatan"] = 5
print(dict_presiden)

# menghapus 1 key pada dict
del dict_presiden["suku"]
print(dict_presiden)

# menggabung dict dengan pembongkaran
dict_partai = {"nama partai": "PDIP", "jabatan": "Petugas Partai"}
dict_identitas_presiden = {**dict_presiden, **dict_partai}
print(dict_identitas_presiden)

# set menyimpan kumpulan elemen yang unik
# tidak ada indeks urutan dan hanya menyimpan satu elemen unik saja.
set_kosong = set()
set_isi = {1, 1, 2, 3, 4, 4}
print(set_isi)

# elemen pada set harus immutable
# set_invalid = {[1], 1} # error
# print(set_invalid)
set_valid = {(1,), 2}
print(set_valid)

# menambahkan elemen set
set_isi.add(6)
print(set_isi)
# set tidak dapat menambahkan elemen yang sudah ada
set_isi.add(6)
print(set_isi)

# operator '&' digunakan untuk menggabungkan 2 set yang hasilnya adalah elemen yang hanya terdapat di kedua set
set_intersect = set_isi & set_valid
print(set_intersect)

# operator '|' digunakan untuk menggabungkan 2 set yang hasilnya adalah semua elemen dari kedua set
set_unions = set_isi | set_valid
print(set_unions)

# operator '-' digunakan untuk membuat set baru yang berisi elemen di set pertama tapi tidak ada di set kedua
set_difference = set_isi - set_valid
print(set_difference)

# operator '^' digunakan untuk membuat set baru dari elemen yang ada di set pertama dan kedua, 
# tapi tidak ada di semua set
set_symetric = set_isi ^ set_valid
print(set_symetric)

# operator '>=' untuk mengecek apakah elemen set di sebelah kiri ada semua di set sebelah kanan
# True jika iya, False jika tidak
bool_set_kiri = set_isi >= set_difference
print(bool_set_kiri)

# sebaliknya, operator '<=' untuk mengecek apaka elemen di sebelah kanan ada semua di set sebelah kiri
# True jika iya, False jika tidak
bool_set_kanan = set_isi <= set_intersect
print(bool_set_kanan)

# mengecek apakah elemen ada di set
bool_ada_di_set = 2 in set_isi
bool_ada_di_set2 = 100 in set_difference
print(bool_ada_di_set)
print(bool_ada_di_set2)

# mengcopy set
set_ini_copy = {3, 4, 56, 39}
set_isi = set_ini_copy.copy()
print(set_isi)
print(set_isi is set_ini_copy)

#################################################################################
######################## Control Flow dan Iterables #############################
#################################################################################

var_int = int(input("masukin angka: "))

# if statement
if var_int < 10:
    print("kurang dari 10")
elif var_int > 10:
    print("lebih dari 10")
else:
    print("udah pasti 10")

# loop
# format() adalah metode string untuk mengganti {} dengan nilai string
'''
for loop akan melakukan pengulangan elemen list sehingga akan mencetak:
    Manusia adalah makhluk hidup.
    Hewan adalah makhluk hidup.
    Tumbuhan adalah makhluk hidup.
'''
for makhluk in ["Manusia", "Hewan", "Tumbuhan"]:
    print("{} adalah makhluk hidup.".format(makhluk))

'range(angka) akan melakukan perulangan mulai dari 0 sampai {angka - 1}'
for i in range(int(input("masukan angka: "))):
    print(i)

'''range(min, max) akan melakukan perulangan dari angka min sampai max - 1.
min < max
'''
for i in range(int(input("masukin angka: ")), int(input("masukin angka: "))):
    print(i)

'''
range(min, max, langkah) akan melakukan perulangan dari min sampai max - 1 dengan
penambahan sesuai langkah.
'''
for i in range(10, 200, 42):
    print(i)

'''
fungsi enumerate() dalam loop for untuk mendapatkan indeks dan nilai dari 
setiap elemen dalam daftar. Fungsi enumerate() akan mengembalikan objek enumerate yang 
berisi pasangan indeks dan nilai dari elemen-elemen dalam daftar.
Dalam setiap iterasi, variabel i akan berisi indeks dari elemen, sedangkan variabel 
value akan berisi nilai dari elemen tersebut. Dengan menggunakan fungsi enumerate(), 
Anda dapat mengakses baik indeks maupun nilai elemen dengan mudah dalam setiap iterasi.
'''
makhluk = ["Manusia", "Hewan", "Tumbuhan"]
for i, daftar in enumerate(makhluk):
    print(i, daftar)

"""
while loop akan terus berjalan selama kondisi yang ditentukan masih terpenuhi. 
Ketika kondisi tersebut tidak lagi terpenuhi, while loop akan berhenti. 
"""
y = 10
while y < 69:
    print(y)
    y += 2

'''
Blok try digunakan untuk mengelompokkan kode yang mungkin memunculkan exception. 
Dalam contoh ini, digunakan raise untuk secara sengaja memunculkan IndexError.

Jika exception terjadi di dalam blok try, program akan mencocokkan jenis exception dengan blok 
except yang sesuai. Dalam contoh ini, ada dua blok except yang berbeda. 
Blok except IndexError akan menangani IndexError yang terjadi, 
sedangkan blok except (TypeError, NameError) akan menangani TypeError dan NameError. 
Pada contoh ini, kedua blok except hanya menggunakan pernyataan pass, 
yang berarti mereka tidak melakukan tindakan pemulihan apa pun. 
Anda dapat menggantinya dengan kode yang sesuai untuk menangani exception tersebut, 
seperti menampilkan pesan kesalahan atau mengambil tindakan pemulihan tertentu.

Blok else adalah opsional dan akan dieksekusi hanya jika tidak ada exception yang terjadi 
di dalam blok try. Dalam contoh ini, jika tidak ada exception, maka pesan "All good!" akan dicetak.

Blok finally juga opsional dan akan dieksekusi dalam semua keadaan, baik exception 
terjadi atau tidak. Ini biasanya digunakan untuk membersihkan sumber daya atau 
menjalankan tindakan terakhir yang perlu dilakukan, seperti menutup file atau koneksi database. 
Dalam contoh ini, pesan "We can clean up resources here" akan dicetak baik saat exception 
terjadi maupun tidak.
'''
    # try:
    #     raise IndexError("ini IndexError")
    # except IndexError() as e:
    #     pass
    # except (NameError, TypeError):
    #     pass
    # else:
    #     print("semuanya sip")
    # finally:
    #     print("GG gaming")

'''
penggunaan pernyataan with memudahkan pengelolaan sumber daya yang memerlukan pembersihan 
setelah selesai digunakan. Contoh yang Anda berikan menggunakan with untuk membuka dan membaca 
file teks.

Dalam contoh tersebut, file teks "inicontoh.txt" dibuka dengan 
pernyataan with open("inicontoh.txt") as f. Pernyataan with secara otomatis 
akan mengelola pembukaan dan penutupan file, sehingga Anda tidak perlu khawatir tentang 
menutup file secara manual.

Setelah file terbuka, perulangan for line in f digunakan untuk 
membaca setiap baris dalam file. Setiap baris kemudian dicetak.

Setelah blok with selesai dieksekusi, file akan ditutup secara otomatis, 
bahkan jika terjadi pengecualian selama pembacaan file. Ini memastikan bahwa sumber 
daya file dibebaskan dengan benar setelah selesai digunakan.

Pernyataan with sangat berguna ketika bekerja dengan sumber daya seperti file, 
koneksi database, atau objek yang memerlukan pembersihan setelah digunakan.
'''

with open("inicontoh.txt") as f:
    for line in f:
        print(line)

"""
untuk membuka file dengan mode "w+" yang berarti file akan dibuka untuk ditulis dan 
dibaca (overwrite mode). Jika file tidak ada, maka file akan dibuat.
isi file tidak ditambah, namun diganti oleh apa yang tertera pada write.
namanya juga overwrite

Setelah file terbuka, kita menggunakan metode write() pada objek 
file untuk menulis string str(contents) ke dalam file. Metode write() digunakan 
untuk menulis teks ke dalam file.
"""
with open("inicontoh.txt", "w+") as file:
    file.write(str(dict_identitas_presiden))

"""
kami mengimpor modul json untuk bekerja dengan data JSON. 
Setelah membuka file dengan mode "w+" (overwrite mode) menggunakan pernyataan with, 
kita menggunakan metode json.dumps() untuk mengubah objek contents menjadi representasi JSON 
dalam bentuk string.

Metode dumps() digunakan untuk mengkodekan objek menjadi string JSON. Dalam contoh ini, 
kita mengkodekan objek contents menjadi string JSON dan kemudian menuliskannya ke dalam file 
menggunakan metode write().

Setelah blok with selesai dieksekusi, file akan ditutup secara otomatis, dan perubahan 
yang kita tulis ke file akan disimpan.

Penting untuk mengimpor modul json dan menggunakan metode json.dumps() saat ingin 
menulis objek ke dalam file dalam format JSON. Hal ini memastikan bahwa objek dikodekan 
dengan benar sesuai dengan sintaks dan aturan format JSON.
"""
import json
with open("inicontoh2.txt", "w+") as file_json:
    file_json.write(json.dumps(dict_partai))

"""
Setelah membuka file dengan mode "r+" (read and write mode) menggunakan pernyataan with, 
kita menggunakan metode read() untuk membaca seluruh isi file sebagai string dan 
menyimpannya ke dalam variabel contents.

Kemudian, kita mencetak nilai contents yang berisi isi file tersebut.

Setelah blok with selesai dieksekusi, file akan ditutup secara otomatis.

Metode read() membaca seluruh isi file sebagai string. Jika file sangat besar, 
bisa lebih efisien untuk membaca file per baris menggunakan perulangan for line in file. 
Namun, dalam contoh ini, kami menggunakan metode read() untuk membaca seluruh isi file sebagai 
string secara langsung.
"""
with open("inicontoh.txt", "r+") as file:
    isi_file = file.read()
print(isi_file)

# Membuka file json
with open("inicontoh2.txt", "r+") as file_json:
    isi_file_json = json.load(file_json)
print(isi_file_json)

# object iterable
obj_iterable = dict_identitas_presiden.keys()
print(type(obj_iterable))
print(obj_iterable)

for i in obj_iterable:
    print(i)

# tidak bisa mengakses objek iterable dengan index
# print(obj_iterable[1]) # TypeError

# mengakses dengan begini
iterable = iter(obj_iterable)

# menggunakan fungsi next() pada sebuah iterator, itu akan mengembalikan 
# elemen berikutnya dalam urutan. Iterator tersebut mempertahankan keadaan internalnya, 
# sehingga Anda dapat melintasi elemen-elemen tersebut satu per satu.
print(next(iterable))
print(next(iterable))
print(next(iterable))

# bisa juga pakai loop
for i in iterable:
    print(i)

# bisa manggil objek iterable pakai list(), hanya saja cuma bisa sekali
ini_iterable = iter(obj_iterable)
print(list(ini_iterable))
print(list(ini_iterable))

###########################################################
######################### FUNCTION ########################
###########################################################

# bikin function pakek def
def tambah(x, y):
    print("a adalah {}, dan b adalah {}".format(x, y))
    return x + y

print(tambah(2, 3))

# cara lain memberikan argumen
print(tambah(x=2, y=2))
print(tambah(int(input("angka: ")), int(input("angka: "))))

# tanda * pada argumen hasilnya adalah tupple
# harus ditempatkan di akhir
def ini_args(*args):
    print("args:", args)

def itu_args(x, *args):
    print("x adalah: ", x)
    print("args adalah: ", args)

ini_args(1, 2, 3)
itu_args(1, 23, 344)

# ** hasilnya dict
# harus ditempatkan di akhir
# liat pemberian argumennya
def ini_dict(**kwargs):
    return kwargs

print(ini_dict(a= "b", c= "d"))

# jika hanya * dan ** yang jadi argumen, penempatan tidak penting
def gatau_function_apa(*args, **kwargs):
    print(args)
    print(kwargs)

gatau_function_apa(1, 2, c=3, d=4)

# Global scope dan local scope
z = 1

def ini_zet(num):
    z = num
    print(z)
print(z)
ini_zet(2)

print("global")
def ini_pasti_zet(num):
    global z
    z = num
    print(z)
print(z)
ini_pasti_zet(10)
print(z)

# function dapat disimpan dalam variable
# bisa bikin fungsi bersarang

def selalu_minus(x):
    def kurangin(y):
        return y - x
    return kurangin

kurangin_100 = selalu_minus(100)
kurangin_100(10)

# function anonim, bisa dipakek untuk argumen fungsi lain
print((lambda x: x < 2)(10))
print(kurangin_100((lambda z: z + 19)(20)))

# map digunakan untuk menerapkan suatu fungsi pada setiap 
# elemen dalam urutan (seperti daftar atau tuple) dan mengembalikan 
# hasilnya dalam bentuk iterator atau daftar baru.
print(list(map(kurangin_100, [4, 2, 3])))

# filter dipakek buat memfilter sesuai kondisi tertentu
print(list(filter(lambda y: y < 10, [2, 3, 4, 90, 11])))


#######################################################################
############################# Modules #################################
#######################################################################

# impor module
import math
print(math.sqrt(17))

# import spesifik function dari module
from math import ceil, floor
print(ceil(3.6))
print(floor(4.5))

# import semua function dari module
from math import *

# menyingkat module
import math as m
math.sqrt(3) == m.sqrt(3)

# mendapatkan daftar function module
with open("modulemath.py", "w+") as file:
    file.write(str(dir(math)))

##############################################
################ Class ######################
#############################################

# "class" untuk membuat class, kalo di solidity, ia seperti contract
class Manusia:

    spesies = "Homo Sapiens"

    # __init__ seperti constructor pada solidity, dieksekusi saat class diinisiasi
    def __init__(self, nama):
        self.nama = nama

        # inisiasi properti
        self.umur = 0
    
    # instance method kek fungsi pada solidity
    def sapa(self, pesan):
        print("{nama}: {pesan}".format(nama=self.nama, pesan=pesan))
    
    def nyanyi(self):
        return "Cinta ini, kadang-kadang tak ada logika"

    # classmethod
    @classmethod
    def info_spesies(cls):
        return cls.spesies

    # static method kek pure function
    @staticmethod
    def ngakak():
        return "wkwkwkwk"
    
    # property kek view funcion (read only)
    @property
    def usia(self):
        return self.umur
    
    # ngeset property
    @usia.setter
    def usia(self, usia):
        self.umur = usia
    
    # hapus properti
    @usia.deleter
    def usia(self):
        del self.umur
    
# pengecekan untuk menjalankan kode jika dijalankan sebagai program utama
if __name__ == '__main__':
    a = Manusia(nama="Agus")
    a.sapa("assalamu'alaikum")
    b = Manusia("Budi")
    b.sapa("Walaikumsalam")

    # memanggil method
    a.info_spesies()

    # mengubah class method
    Manusia.spesies = "Anak Cucu Adam"
    a.sapa(a.info_spesies())
    b.sapa(a.info_spesies())

    # memanggil static method
    print(a.ngakak())
    print(Manusia.ngakak())

    # update property
    a.usia = 29
    a.sapa("Saya berusia {usia} tahun.".format(usia=a.usia))

    
