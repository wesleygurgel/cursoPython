# Módulo Collections - Counter
"""
Collections -: High-Perfomance Container Datetypes

Counter -: Recebe um interável como parâmetro e cria um objeto do tipo Collections Counter que é parecido com um
dicionário, contendo como chave o elemento ad lista passada como parâmetro e como valor a quantidade de ocorrências
desse elemento.

"""
from collections import Counter

# Podemos utilizar qualquer iterável
lista = [1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,5,6,6,6,6,7,7,7,7,8,8,9,34,21,3,12,123,121]

res = Counter(lista)
print(type(res))
print(res)
# Counter({3: 7, 5: 7, 2: 6, 4: 6, 1: 5, 6: 4, 7: 4, 8: 2, 9: 1, 34: 1, 21: 1, 12: 1, 123: 1, 121: 1})


print('\nExemplo 2')
print(Counter('Wesley Gurgel'))
# Counter({'e': 3, 'l': 2, 'W': 1, 's': 1, 'y': 1, ' ': 1, 'G': 1, 'u': 1, 'r': 1, 'g': 1})


print('\nExemplo 3')
texto = """
No filme “Mauá - o imperador e o rei” é retratada a história de Irineu Evangelista de Sousa, um dos mais bem-sucedidos empreendedores da história brasileira, sendo responsável por diversas iniciativas modernizadoras para economia nacional ao longo do século XX. No Brasil atual, entretanto, o que se observa, é o oposto do que o Mauá deixou como legado, uma vez que o empreendedorismo no país apresenta diversos entraves, os quais dificultam a mudança do cenário nacional nesse aspecto. Nesse sentido, convém analisar as principais causas relacionadas a essa problemática em nossa sociedade.

De início, é oportuno refletir a situação sob a perspectiva da obra “Raízes do Brasil”, do escritor e jornalista Sérgio Buarque de Holanda, em que se afirma a negligência política com demandas relacionadas ao desenvolvimento do empreendedorismo no Brasil ao longo das decádas. Com base na supracitada ideia, evidencia-se que tal cenário prejudicial influencia na falta de políticas públicasefetivas aos trabalhadores que tentam alavancar um novo negócio, mas esbarram em diversos processos burocráticos que, muitas vezes, impedem o desenvolvimento de uma “start-up”. Em tal ótica, não há como isentar de crítica a atuação estatal por permitir que os pequenos empresários, os que mais precisam ser favorecidos, encontrem tantas barreiras para efetivar seu empreendimento.

Ademais, é imperativo ressaltar que a falta de escolaridade é promotora do problema. Segundo uma pesquisa realizada pelo Sebrae, 34% do empreendedores possuem nível fundamental incompleto. Convém, nesse caso, ressalta uma ideia do filósofo alemão Immanuel Kant, o qual defende que a educação projeta o que o indivíduo será. Nesse sentido, aquelas pessoas que não desfrutam de uma educação poderosa e edificadora que tenha como base todos os aspectos educacionais e sociais possíveis, infelizmente podem levar uma grande desvantagem em comparação a uma pessoa que tenha uma alto grau informacional. 

Portanto, o Governo deve criar um novo plano de ações para os microempreendedores, por meio do poder legislativo, que contenha, no mínimo, uma menor carga tributária, acesso ao crédito facilitadocom a menor taxa de juros possível, cursos ead sobre como empreender, marketing aplicado às re disponibilizados gratuitamente por organizações educacionais do governo sobre com os seguintes assuntos: gerenciamento de um pequeno comércio, como usar as redes sociais para favorecer uma marca, etc. Espera-se, com isso, que ao longo do tempo se diminuam os desafios para executar o empreendedorismo no Brasil.
"""

palavras = texto.split()
myCounter = Counter(palavras)
print(myCounter)

# Encontrando as 5 palavras mais ocorrência
print(myCounter.most_common(5))









