"""
Documentando Funções com Docstrings
"""

def diz_oi():
    """Uma função simples que retorna a String 'Oi'!"""
    return 'Oi!'

print(diz_oi())
print(diz_oi.__doc__)

def exponencial(numero, potencia=2):
    """
    Função que RETORNA por padrão o quadrado de 'numero'
    :param numero: Número que desejamos gerar o exponencial
    :param potencia: Potência que queremos gerar o exponecial
    :return: Retorna o exponencial de 'número' por 'potência'
    """
    return numero ** potencia

print(exponencial.__doc__)