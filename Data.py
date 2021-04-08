class Data():
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def get_nama(self):
        return self.nama

    def get_nim(self):
        return self.nim

    def get_jurusan(self):
        return self.jurusan

    def get_summary(self):
        return self.nama + "Nama : " + self.nama + "\n NIM : " + self.nim + "\n Jurusan : " + self.jurusan
