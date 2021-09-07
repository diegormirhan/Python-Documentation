import unittest
from robo import Robo


class RoboTestes(unittest.TestCase):

    def setUp(self) -> None:
        self.megamen = Robo('Mega Men', bateria=50)
        print('\nsetUp está sendo executado!')

    def test_carregar(self):
        self.megamen.carregar()
        self.assertEqual(self.megamen.bateria, 100)

    def test_dizer_nome(self):
        self.assertEqual(self.megamen.dizer_nome(), 'BEEP BEEP BOOP BOOP. EU SOU MEGA MEN')
        self.assertEqual(self.megamen.bateria, 49, 'A bateria deveria estar em 49%')

    def tearDown(self) -> None:
        print('tearDown está sendo executado!')


if __name__ == '__main__':
    unittest.main()
