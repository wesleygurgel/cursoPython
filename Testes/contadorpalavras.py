from collections import Counter, OrderedDict

leitura = open('texto.txt', encoding='utf8')
texto = ""
for palavra in leitura:
    texto += palavra

# Tirando caracteres
texto = texto.replace(',', '')
texto = texto.replace('-', '')
texto = texto.replace('"', '')
texto = texto.replace('.', '')
texto = texto.replace('?', '')
texto = texto.replace('!', '')
texto = texto.replace('“', '')
texto = texto.replace('”', '')

texto = texto.split()
myCounter = Counter(texto)

with open('contador.txt', 'w', encoding="utf8", newline="") as arquivo:
    quantidade = len(myCounter)
    ordenado = OrderedDict(myCounter.most_common(quantidade-1))
    for key, value in ordenado.items():
        arquivo.write(f'A palavra "{key.upper()}" apareceu {value} vezes\n')



