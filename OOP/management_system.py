class Talaba:
    talabalar_soni = 0
    __talabalar = []
    def __init__(self, ism, yosh, idraqam, bosqich=1):
        self.ism = ism
        self.yosh = yosh
        self.idraqam = idraqam
        self.bosqich = bosqich
        Talaba.talabalar_soni += 1
        Talaba.__talabalar.append(self)
    
    def __str__(self):
        return self.ism.title()

    @classmethod
    def get_talabalar(cls):
        return [str(t) for t in cls.__talabalar]

    def get_info(self):
        info = f"Ismi: {self.ism.title()} \nYoshi: {self.yosh} \n{self.bosqich}-kurs ID: {self.idraqam}"
        return info

    def get_ism(self):
        return self.ism
    
    def get_yosh(self):
        return self.yosh
    
    def get_bosqich(self):
        return self.bosqich
    
    def get_idraqam(self):
        return self.idraqam

    def update_bosqich(self, stage=1):
        if stage > self.bosqich:
            self.bosqich += 1
        else:
            print(f"{self.ism} {self.bosqich}-kursda kamaytira olmaysiz")
    

class Guruh:
    guruh_soni = 0
    __guruhlar = []
    def __init__(self, nomi, *talabalar):
        self.nomi = nomi
        self.talabalar = list(talabalar)
        Guruh.guruh_soni += 1
        Guruh.__guruhlar.append(self)

    def __str__(self):
        return f"{self.nomi}"
    
    # def __del__(self):
    #     print(f"{self} guruhi o'chirildi")

    @classmethod
    def get_guruhlar(cls):
        return [str(g) for g in cls.__guruhlar]
    
    @classmethod
    def guruh_ochirish(cls, guruh):
        cls.guruh_soni -= 1
        cls.__guruhlar.remove(guruh)
        print(f"{guruh} guruhi o'chirildi")
        del guruh

    def get_info(self):
        info = f"{self} guruh talabalari: {[str(t) for t in self.talabalar]}"
        return info

    def talaba_qoshish(self, *talaba):
        for t in talaba:
            if isinstance(t, Talaba):
                self.talabalar.append(t)
            else:
                print(f"{t} nomli talaba yo'q")
    
    def talaba_ochirish(self, *idraqamlar):
        for idraqam in idraqamlar:
            talaba = list(filter(lambda t: t.idraqam == idraqam, self.talabalar))
            if talaba:
                if isinstance(talaba[0], Talaba):
                    self.talabalar.remove(talaba[0])
            else:
                print(f"{idraqam} idraqamli talaba bu guruhda yo'q")

    def show_students(self):
        if self.talabalar:
            return [f"{talaba} {talaba.get_bosqich()}-kurs" for talaba in self.talabalar]
        else:
            print(f"{self} guruhida talabalar yo'q")
            

talaba1 = Talaba("doniyor", 21, "dsgre513", 2)
talaba2 = Talaba("alisher", 19, "dsgrdfv3")

guruh1 = Guruh("19-23-S")

guruh1.talaba_qoshish(talaba1, talaba2)
print(guruh1.show_students())

guruh1.talaba_ochirish('dsgre513', "sadffzsd", 'dsgrdfv3', '1sd2f1s')

guruh1.show_students()