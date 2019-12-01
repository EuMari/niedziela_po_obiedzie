import unittest

class PierwszyTest(unittest.TestCase):
    def setUp(self)                         #setUp musi byc
        print("Przygotowanie do testu")
    def test_224(self):                     #test moze sie nazywac dowolnie, ale musi sie zaczynac od "test"
        print("Sprawdzam, czy 2+2 =4..")
        assert(2+2==4)
    def tearDown(self):                     #tearDown musi byc
        print("Sprzatam po testach")

if __name__ == '__main__':                  #odpal test tylko z tego pliku; jezeli bedzie gdzies zaimportowane, to test sie nie uruchomi
    unittest.main(verbosity=2)
