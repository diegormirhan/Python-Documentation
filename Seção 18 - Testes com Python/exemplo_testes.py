import unittest
from exemplo_atividades import comer, dormir, cor_favorita, numeros


class AtividadesTestes(unittest.TestCase):

    def test_comida_saudavel(self):
        """Retornando comida saudável!"""
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma.'
        )

    def test_comida_gostosa(self):
        """Retornando comida gostosa!"""
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),
            'Estou comendo pizza porque a gente só vive uma vez.'
        )

    def test_dormir_pouco(self):
        """Retornando dormir pouco!"""
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir por 4 horas. :('
        )

    def test_dormir_muito(self):
        """Retornando dormir muito!"""
        self.assertEqual(
            dormir(10),
            'Putz, dormi muito! Estou atrasado para o trabalho!'
        )

    def test_cor_favorita(self):
        """Retornando cor favorita!"""
        self.assertTrue(cor_favorita('branco'))

    def test_cor_nao_favorita(self):
        """Retornando a cor não favorita!"""
        self.assertFalse(cor_favorita('verde'))

    def test_alunos(self):
        """Retornando alunos!"""
        self.assertIn('Ana', ['Ana', 'Maria', 'Nicole'])

    def test_nao_estudantes(self):
        """Retornando não estudantes!"""
        self.assertNotIn('Diego', ['Paulo', 'Marina', 'Ana'])

    def test_numeros(self):
        """Retornando números!"""
        self.assertIsNone(numeros(11))

    def test_nao_numeros(self):
        """Retornando não números!"""
        self.assertIsNotNone(numeros(9))

    def test_instancia(self):
        """Retorna a instância!"""
        self.assertIsInstance(numeros(9), int)

    def test_not_instancia(self):
        """Retorna a não instância!"""
        self.assertNotIsInstance(numeros(5), str)


if __name__ == '__main__':
    unittest.main()
