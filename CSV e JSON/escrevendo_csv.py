from csv import writer

# with open('filmes.csv', 'a', encoding="utf8", newline="") as arquivo: #w escreve, 'a' concatena
#     escritor_csv = writer(arquivo)
#     filme = None
#     escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
#     while filme != 'sair':
#         filme = input("Informe o nome do filme: ")
#         if filme != 'sair':
#             genero = input("Informe o Gênero: ")
#             duracao = input("Informe a duração em Minutos: ")
#             escritor_csv.writerow([filme, genero, duracao])

# DictWriter
from csv import DictWriter

with open('filmes2.csv', 'a', encoding="utf8", newline="") as arquivo:
    # IF FILE EXIST - COMO FAZER?
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()

    filme = None
    while filme != 'sair':
        filme = input("Informe o nome do filme: ")
        if filme != 'sair':
            genero = input("Informe o Gênero: ")
            duracao = input("Informe a duração em Minutos: ")
            escritor_csv.writerow({'Título': filme, 'Gênero': genero, 'Duração': duracao})


            def popup():
                response = messagebox.askyesno("This is my Popup!", "Hello your asshole?")
                Label(root, text=response).pack()  # YES = 1 | NO = 0
                if response == 1:
                    Label(root, text="KKKKKKKKKK assholeee").pack()
                else:
                    Label(root, text="OMG I really thought you are").pack()


            Button(root, text="Popup", command=popup).pack()
