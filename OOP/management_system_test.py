import unittest
from management_system import Talaba, Guruh, Fakultet

# O'zgaruvchilar

talaba1 = Talaba("doniyor", 21.1)
talaba2 = Talaba("alisher", 19, 2)
talaba3 = Talaba("otabek", 35, 3)

guruh1 = Guruh("19-23-S")
guruh2 = Guruh("3-25-A")
guruh3 = Guruh("15-24-B")

fakultet1 = Fakultet("Iqtisod")
fakultet2 = Fakultet("IT")


class TalabaTest(unittest.TestCase):
    def test_create(self):
        
        self.assertIsNotNone(talaba1.ism)
        self.assertEqual('doniyor', talaba1.ism)
        
        self.assertIsNotNone(talaba1.yosh)
        self.assertEqual(21, talaba1.yosh)
        
        self.assertIsNotNone(talaba1.bosqich)
        self.assertEqual(1, talaba1.bosqich)

        self.assertIsNotNone(talaba1.idraqam)
        # self.assertEqual(None, talaba1.guruh)

        try:
            talaba4 = Talaba('oybek', 19, 6)
        except ValueError as error:
            self.assertEqual(type(error), ValueError)

    def test_update_bosqich(self):
        talaba1.bosqich = talaba1.update_bosqich()
        self.assertEqual(2, talaba1.bosqich)

        talaba2.bosqich = talaba2.update_bosqich(2)
        self.assertEqual(4, talaba2.bosqich)
        talaba2.bosqich = talaba2.update_bosqich(-2)
        self.assertEqual(f"{talaba2} kursini kamaytirib bo'lmaydi", talaba2.bosqich)

        talaba3_bosqich = talaba3.bosqich
        talaba3.bosqich = talaba3.update_bosqich(4)
        self.assertEqual(f"{talaba3} {talaba3_bosqich}-kursda. Siz {talaba3} kursini maksimum {5-talaba3_bosqich} ta oshira olasiz", talaba3.bosqich)

class GuruhTest(unittest.TestCase):
    def test_create(self):

        self.assertIsNotNone(guruh1.nomi)
        self.assertEqual("19-23-S", guruh1.nomi)

        self.assertIsNotNone(guruh1.talabalar)
        self.assertEqual([], guruh1.talabalar)

    def test_talaba_qoshish(self):
        guruh1.talaba_qoshish(talaba1, talaba2, talaba1)
        self.assertEqual([talaba1, talaba2], guruh1.talabalar)

    def test_get_talabalar(self):
        self.assertEqual([], guruh1.get_talabalar())
        guruh1.talaba_qoshish(talaba1, talaba2, talaba1)
        self.assertEqual(['doniyor', 'alisher'], guruh1.get_talabalar())

    

if __name__ == '__main__':
    unittest.main()