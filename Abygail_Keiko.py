my_nama = input("Program cek kategori TKA Bahasa Indonesia oleh: ")
nilai_angka = float(input("Masukkan nilai: "))

if nilai_angka >=95: 
	print("Predikat: Baik - Istimewa ")
	print("Predikat t+ertinggi 'Baik-Istimewa' diberikan secara eksklusif hanya untuk murid yang mencapai nilai minimal 95 pada mata pelajaran terkait.")

elif nilai_angka >= 76.67: 
	print("Predikat: Baik")
	print("Murid mampu menjelaskan bahasa kias dan citraan pada teks fiksi, menilai relevansi teks dengan kehidupan nyata, menyimpulkan respons emosional, serta menguji keakuratan isi teks melalui perbandingan.")

elif nilai_angka >= 50: 
	print("Predikat: Memadai")
	print("Murid mampu mengidentifikasi istilah, objek, dan latar; menyusun bagan teks; menyimpulkan ide pokok serta tokoh; memprediksi peristiwa; dan menjelaskan kelogisan hubungan antarinformasi.")

elif nilai_angka <= 50:
	print("Predikat: Kurang")
	print("Murid baru memiliki kemampuan dasar untuk mengidentifikasi informasi penting yang tertulis secara tersurat di dalam teks.")