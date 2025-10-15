import unittest
from management_system import Talaba, Guruh, Fakultet

# O'zgaruvchilar

talaba1 = Talaba("doniyor", 21.1)
talaba2 = Talaba("alisher", 19, 2)
talaba3 = Talaba("otabek", 35, 3)
talaba4 = Talaba("abdulaziz", 28)

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


    def test_talaba_ochirish(self):
        guruh2.talaba_qoshish(talaba3, talaba4)

        id_talaba3 = talaba3.get_idraqam()
        guruh2.talaba_ochirish(id_talaba3)
        self.assertEqual([talaba4], guruh2.talabalar)

        guruh2.talaba_ochirish(talaba4.get_idraqam())
        self.assertEqual([], guruh2.talabalar)


    def test_get_talabalar(self):
        self.assertEqual([], guruh1.get_talabalar())
        guruh1.talaba_qoshish(talaba1, talaba2, talaba1)
        self.assertEqual(['doniyor', 'alisher'], guruh1.get_talabalar())


    def test_oralama_yosh(self):

        oralama_yosh_g3 = guruh3.get_ortalama_yosh()
        self.assertEqual(f"{guruh3} guruhida talabalar yo‘q.", oralama_yosh_g3)

        guruh2.talaba_qoshish(talaba3, talaba4)
        oralama_yosh_g2 = guruh2.get_ortalama_yosh()
        yoshlar = [t.get_yosh() for t in guruh2.talabalar]
        self.assertEqual(f"{guruh2} guruh o‘rtacha yoshi: {sum(yoshlar)//len(yoshlar)}", oralama_yosh_g2)


    def test_show_students(self):

        self.assertEqual(f"{guruh3} guruhida talabalar yo'q", guruh3.show_students())

        list_info =  [f"{talaba}, {talaba.get_bosqich()}-kurs, ID: {str(talaba.get_idraqam())}, Guruh: {talaba.guruh}" for talaba in guruh1.talabalar]
        self.assertEqual(list_info, guruh1.show_students())

class FakultetTest(unittest.TestCase):

    def test_create(self):

        self.assertIsNotNone(fakultet1.nomi)
        self.assertEqual("Iqtisod", fakultet1.nomi)

        self.assertIsNotNone(fakultet1.guruhlar)


    def test_guruh_qoshish_ochirish(self):

        fakultet1.guruh_qoshish(guruh1, guruh2, guruh1)
        self.assertEqual([guruh1, guruh2], fakultet1.guruhlar)

        fakultet1.guruh_ochirish(guruh1, guruh2)
        self.assertEqual([], fakultet1.guruhlar)
        

    def test_guruh_topish(self):
        self.assertEqual(None, fakultet1.guruh_topish(guruh1))

        fakultet1.guruh_qoshish(guruh1)
        self.assertEqual(guruh1, fakultet1.guruh_topish(guruh1.nomi))
        fakultet1.guruh_ochirish(guruh1)
    


if __name__ == '__main__':
    unittest.main()
