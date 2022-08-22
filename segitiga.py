class Segitiga:
  def __init__(self):
    self.alas = int (input ('masukan nilai alas '))
    self.tinggi = int (input ('masukan nilai tinggi '))

  def get_luas(self):
    return 0.5 * self.alas * self.tinggi

def cetak ():
    import os
    segitiga1 = Segitiga()
    print('luas segitiga:', segitiga1.get_luas())
    
    teks = "Hasil : {}\n".format(segitiga1.get_luas())
    filehasil = open("Hasil_segitiga.txt", "a")
    filehasil.write(teks)
    filehasil.close()
    
    
    os.system('pause')
    os.system('cls')
while True:
    cetak ()
