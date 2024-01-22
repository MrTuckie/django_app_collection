from django.test import TestCase

# Create your tests here.
""" 
Anotações do ruivo:

Para ter o cálculo de conta de luz, precisamos de alguns valores.
* pct_pis (%)
* pct_cofins (%)
* consumo_energia_ativa (kWh)
* valor_tusd (R$/kWh)
* valor_te (R$/kWh)
* valor_cip (R$)
* bandeira_tarifaria
* tipo da instalação
* se teve multa

A princípio, deveria ser dividido o CIP também. https://www.edp.com.br/tabela-de-calculo-cip/

"""
from electricity_bill.helpers import *

class Test_calcular_valor_total_fatura(TestCase):
    
    def setUp(self):
        self.consumo = 100 # kWh
        self.parte_pis_cofins = calcula_parte_pis_cofins()
        self.parte_icms = calcula_parte_icms()
    
    def test_calcula_parte_pis_cofins(self):
        pass

    def test_calcula_parte_icms(self):
        pass
    
    def test_calcular_tarifa_com_tributos(self):
        result_tusd = calcula_tarifa_com_tributos(self.parte_pis_cofins,self.parte_icms,VALOR_TUSD_ANEEL)
        result_te = calcula_tarifa_com_tributos(self.parte_pis_cofins,self.parte_icms,VALOR_TE_ANEEL)
        self.assertAlmostEquals(0.4955,result_tusd,4,msg="Era pra ser R$ 0.4955")
        self.assertAlmostEquals(0.3858,result_te,4,msg="Era pra ser R$ 0.3858")
    
    def test_calcula_consumo_e_tarifa(self):
        result_tusd = self.consumo * calcula_tarifa_com_tributos(self.parte_pis_cofins,self.parte_icms,VALOR_TUSD_ANEEL)
        result_te = self.consumo * calcula_tarifa_com_tributos(self.parte_pis_cofins,self.parte_icms,VALOR_TE_ANEEL)
        self.assertAlmostEquals(49.55 ,result_tusd,4,msg="Deve ser R$ 49.55")
        self.assertAlmostEquals(38.58 ,result_te,4,msg="Deve ser R$ 38.58")
    
