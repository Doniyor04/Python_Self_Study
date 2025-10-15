import uuid # Talabaga ID yaratish uchun
import json # Malumotlarni json formatda saqlash va o'qish uchun
import pprint # json formatdagi fayllarni konsolda tartibli o'qish uchun

class Talaba:
    talabalar_soni = 0
    __talabalar = []
    def __init__(self, ism, yosh, bosqich=1):
        self.ism = ism
        self.yosh = int(yosh)
        self.idraqam = uuid.uuid4()
        if 5 >= bosqich >= 1:
            self.bosqich = bosqich
        else:
            raise ValueError("Talabaning bosqichi 1 dan 5 gacha bo'lgan butun son bo'lishi kerak")
        
        self.guruh = None
        Talaba.talabalar_soni += 1
        Talaba.__talabalar.append(self)
    
    def __str__(self):
        return self.ism.title()

    @classmethod
    # shu klassga tegishli talabalar(obyektlar)ni list korinishida qaytaradi
    def get_talabalar(cls):
        return [str(t) for t in cls.__talabalar]

    def get_info(self):
        # Talabani malumotlarini qaytaradi
        info = f"Ismi: {self.ism.title()}, Yoshi: {self.yosh}, {self.bosqich}-kurs"
        return info

    def get_ism(self):
        return self.ism
    
    def get_yosh(self):
        return self.yosh
    
    def get_bosqich(self):
        return self.bosqich
    
    def get_idraqam(self):
        return self.idraqam

    def update_bosqich(self, stage=None):
        # talabani bosqichini kiritgan bosqichga oshiradi, agar bosqich kiritmasa avtomatik 1 taga oshiradi

        # agar stage berilmasa — avtomatik +1
        if stage is None:
            if self.bosqich < 5:
                self.bosqich += 1
                return self.bosqich
            return f"{self} kursini 5 dan baland qilolmaysiz"
        if 5-self.bosqich >= stage > 0:
            self.bosqich += stage
            return self.bosqich
        elif 5-self.bosqich <= stage:
            return f"{self} {self.bosqich}-kursda. Siz {self} kursini maksimum {5-self.bosqich} ta oshira olasiz"
        elif stage <= 0:
            return f"{self} kursini kamaytirib bo'lmaydi"
        
        
        # agar stage berilsa — shu kursga o'tish (faqat oshirishga ruxsat)
        if not (1 <= stage <= 5):
            return f"{self} uchun noto'g'ri kurs (1-5 oralig'ida bo'lishi kerak)."
        if stage <= self.bosqich:
            return f"{self.ism} {self.bosqich}-kursda kamaytira olmaysiz"
        self.bosqich = stage
        return self.bosqich
    
    def save(self):
            # talabaning malumotlarini json formatda fayl ochib saqlaydi  
            talaba = {
                "ism": self.ism,
                "yosh": self.yosh,
                "bosqich": self.bosqich,
                "id": str(self.idraqam)
            }

            with open(f"{self.ism.lower()}.json", "w") as f:
                json.dump(talaba, f, indent=4)
    
    def read(self):
        # talabaning malumotlarini json formatda o'qib konsolga chiqaradi  
        with open(f"{self.ism.lower()}.json", "r") as f:
            malumot = json.load(f)
        pprint.pprint(malumot, width=120)

class Guruh:
    guruh_soni = 0
    __guruhlar = []
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar = []
        Guruh.guruh_soni += 1
        Guruh.__guruhlar.append(self)

    def __str__(self):
        return self.nomi
    
    @classmethod
    # Guruh klasiga tegishli guruhlar(obyektlar)ni ro'yxatini qaytaradi
    def get_guruhlar(cls):
        return [str(g) for g in cls.__guruhlar]
    
    @classmethod
    # Guruh klasiga tegishli obyektni o'chiradi
    def guruh_ochirish(cls, *guruh):
        if guruh:
            for g in guruh:
                cls.guruh_soni -= 1
                cls.__guruhlar.remove(g)
                print(f"{g} guruhi o'chirildi")
                del g

    def get_info(self):
        info = f"{self} guruh talabalari: {[str(t) for t in self.talabalar]}"
        return info

    def talaba_qoshish(self, *talaba):
        # guruhga talaba qo'shadi
        if talaba:
            for t in talaba:
                if isinstance(t, Talaba):
                    if t.guruh == None:
                        self.talabalar.append(t)
                        t.guruh = self.nomi
                else:
                    print(f"{t} nomli talaba yo'q")
    
    def talaba_ochirish(self, *idraqamlar):
        # berilgan idraqamli talabalarni guruhdan o'chiradi
        for idraqam in idraqamlar:
            talaba = list(filter(lambda t: t.idraqam == idraqam, self.talabalar))
            if talaba:
                if isinstance(talaba[0], Talaba):
                    self.talabalar.remove(talaba[0])
            else:
                print(f"{idraqam} idraqamli talaba bu guruhda yo'q")
    
    def get_talabalar(self):
        return [t.ism for t in self.talabalar]
    
    def get_ortalama_yosh(self):
        # Guruhdagi talabalarni o'rtacha yoshini topadi
        if not self.talabalar: # ZeroDivisionError chiqmaslik uchun
            return f"{self} guruhida talabalar yo‘q."
        yoshlar = [t.get_yosh() for t in self.talabalar]
        return f"{self} guruh o‘rtacha yoshi: {sum(yoshlar)//len(yoshlar)}"
            

    def show_students(self):
        # Guruhdagi talabalarni ko'rsatadi
        if self.talabalar:
            return [f"{talaba}, {talaba.get_bosqich()}-kurs, ID: {str(talaba.get_idraqam())}, Guruh: {talaba.guruh}" for talaba in self.talabalar]
        else:
            return f"{self} guruhida talabalar yo'q"
    
    def save(self):
        # guruhning malumotlarini json formatda fayl ochib saqlaydi  
        guruh = {
            "nomi": self.nomi,
            "talabalar": self.show_students()
        }
        with open(f"{self.nomi.lower()}.json", "w") as f:
            json.dump(guruh, f, indent=4)
    
    def read(self):
        # guruhning malumotlarini json formatda o'qib konsolga chiqaradi  
        with open(f"{self.nomi.lower()}.json", "r") as f:
            malumot = json.load(f)
        pprint.pprint(malumot, width=120)
             
class Fakultet:
    fakultet_soni = 0
    __fakultetlar = []
    def __init__(self, nomi):
        self.nomi = nomi
        self.guruhlar = []
        Fakultet.__fakultetlar.append(self)
        Fakultet.fakultet_soni += 1

    def __str__(self):
        return self.nomi

    def get_info(self):
        return f"{self.nomi} fakulteti"
    
    def guruh_qoshish(self, *guruhlar):
        # fakultetga guruh qo'shadi
        if guruhlar:
            for g in guruhlar:
                if isinstance(g, Guruh):
                    if g not in self.guruhlar:
                        self.guruhlar.append(g)
                        # self.refresh_talabalar()

    def guruh_ochirish(self, *guruhlar):
        # fakultetdan berilgan guruhni o'chiradi
        if guruhlar:
            for g in guruhlar:
                if isinstance(g, Guruh):
                    if g in self.guruhlar:
                        self.guruhlar.remove(g)
                    else:
                        return f"{g} guruhi bu fakultetda yo'q"
                else:
                    f"{g} nomli guruh mavjud emas"
    
    def guruh_topish(self, g_nomi):
        # berilgan guruhni fakultetdan qidiradi va usha guruhni nomini qaytaradi
        for g in self.guruhlar:
            if g.nomi == g_nomi:
                return g
        return None

                
    def search_student(self, ism):
        # berilgan ismni fakultetdan (fakultetni talabalar ro'yxatidan) qidiradi va usha talabani malumotini qaytaradi
        if ism:
            for t in self.talabalar:
                if t.ism.lower() == ism.lower():
                    return t.get_info()
            return f"{ism} ismli talaba bu fakultetda yo'q"


    def get_fakultet_guruhlar(self):
        # fakultetdagi guruh nomlarini ro'yxat qilib qaytaradi
        return [g.nomi for g in self.guruhlar]
            
    def get_fakultet_talabalar(self):
        # fakultetdagi talabalarni infosini olib listga joylab listni qaytaradi
        talabalar = []
        for g in self.guruhlar:
            for t in g.talabalar:
                talabalar.append(t.get_info())
        return talabalar
                
    def save(self):
        # fakultetning malumotlarini json formatda fayl ochib saqlaydi  
        fakultet = {
            "nomi": self.nomi,
            "guruhlar": self.get_fakultet_guruhlar(),
            "talabalar": self.get_fakultet_talabalar()
        }
        with open(f"{self.nomi.lower()}.json", "w") as f:
            json.dump(fakultet, f, indent=4)

    def read(self):
        # fakultetning malumotlarini json formatda o'qib konsolga chiqaradi  
        with open(f"{self.nomi.lower()}.json", "r") as f:
            malumot = json.load(f)
        pprint.pprint(malumot, width=120)
            

# talaba1 = Talaba("doniyor", 21.1, 1)
# talaba2 = Talaba("alisher", 19, 2)
# talaba3 = Talaba("otabek", 35, 3)
# talaba4 = Talaba("abdulla", 18)
# talaba5 = Talaba("davron", 25)

# guruh1 = Guruh("19-23-S")
# guruh1.talaba_qoshish(talaba1, talaba2, talaba1)

# print(guruh1.get_talabalar())

# print()
# guruh1.talaba_ochirish(talaba1.get_idraqam())

# print(guruh1.talabalar)

# guruh2 = Guruh("3-23-S")
# guruh2.talaba_qoshish(talaba1, talaba2, talaba1, talaba4)

# guruh3 = Guruh("4-19")
# guruh3.talaba_qoshish(talaba1, talaba3, talaba2)

# fakultet1 = Fakultet("Iqtisod")
# fakultet2 = Fakultet("IT")

# fakultet1.guruh_qoshish(guruh2, guruh1)
# fakultet1.guruh_qoshish(guruh1, guruh2)

# print(fakultet1.get_fakultet_guruhlar())
# print(fakultet1.get_fakultet_talabalar())

# fakultet1.guruh_ochirish(guruh1)
# print()

# print(fakultet1.get_fakultet_guruhlar())
# print(fakultet1.get_fakultet_talabalar())
