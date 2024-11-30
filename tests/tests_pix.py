# tests_pix.py


import unittest

from test_criar_cobranca_imediata import TestCriarCobrancaImediata
from test_consultar_cobranca_imediata import TestConsultarCobrancaImediata
from test_revisar_cobranca_imediata import TestRevisarCobrancaImediata
from test_criar_cobranca_com_vencimento import TestCriarCobrancaComVencimento


# Tests Suites
def suite():
    my_suite = unittest.TestSuite()

    my_suite.addTests(
        unittest.defaultTestLoader.loadTestsFromTestCase(TestCriarCobrancaImediata)
    )
    my_suite.addTests(
        unittest.defaultTestLoader.loadTestsFromTestCase(TestRevisarCobrancaImediata)
    )
    my_suite.addTests(
        unittest.defaultTestLoader.loadTestsFromTestCase(TestConsultarCobrancaImediata)
    )
    my_suite.addTests(
        unittest.defaultTestLoader.loadTestsFromTestCase(TestCriarCobrancaComVencimento)
    )

    return my_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
