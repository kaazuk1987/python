
#tekstem zabawa wazne rb czytanie bajtami x tworzenie pliku a dopisywaniena koncu
f = open("myfile.txt", "x")
f= open("myfile.txt","a")
f.write("Now the file has more content!ASDFFSAFEFEWDASCASAS")
f=open("myfile.txt","r")
print (f.read())
f.close()