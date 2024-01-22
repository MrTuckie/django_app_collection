import math
# Constantes
VALOR_TUSD_ANEEL = 0.39253000 # sem tributo
VALOR_TE_ANEEL = 0.30560000 # sem tributo
PCT_PIS = 0.820 # %
PCT_COFINS = 3.750 # %
VALOR_CIP = 24.28  # R$
PCT_ICMS = 17 # % 
# Tarifa (tusd ou te, por ex) com tributos = tarifa_aneel / ((1 - pct_pis - pct_cofins) * (1 - pct_icms))  


def trunca_tarifa(tarifa:float):
    power = 4
    return math.trunc(tarifa * 10**power)/10**power 

def calcula_parte_pis_cofins(pct_pis=PCT_PIS,pct_cofins=PCT_COFINS):
    return (100 - pct_pis - pct_cofins)/100

def calcula_parte_icms(pct_icms=PCT_ICMS):
    return (100 - pct_icms)/100

def calcula_tarifa_com_tributos(parte_pis_cofins,parte_icms,valor_tarifa_aneel):
    result = valor_tarifa_aneel / (parte_pis_cofins * parte_icms)
    return trunca_tarifa(result)