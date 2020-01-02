import rarfile

r = rarfile.RarFile('Data.rar')
r.extractall()
r.close()
