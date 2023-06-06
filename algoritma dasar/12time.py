import time; # Digunakan untuk meng-import modul time

ticks = time.time()
print "Berjalan sejak 12:00am, January 1, 1970:", ticks #python 2
print ("Berjalan sejak 12:00am, January 1, 1970:", ticks) #untuk python 3 gunakan tanda kurung, print()


import time;

localtime = time.localtime(time.time())
print "Waktu lokal saat ini :", localtime #python 2


import time;

localtime = time.asctime( time.localtime(time.time()) )
print "Waktu lokal saat ini :", localtime #python 2


import calendar

cal = calendar.month(2008, 1)
print "Dibawah ini adalah kalender:" #python 2
print cal


