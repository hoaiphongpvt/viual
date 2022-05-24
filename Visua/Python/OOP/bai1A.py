class HinhChuNhat:
    def __init__(self,chieudai,chieurong):
        self.chieudai = chieudai
        self.chieurong = chieurong

    def Dientich(self):
        return (self.chieudai * self.chieurong)
hcn = HinhChuNhat(6,5)
print("Dien tich hinh chu nhat la: ", hcn.Dientich())