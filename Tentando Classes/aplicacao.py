import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import *
from PIL import ImageTk, Image
from tkinter import filedialog
import datetime
from configparser import ConfigParser
import time, threading, logging
from maskedentry import MaskedWidget
from protocolos_cnj import ProtocolosCNJ
import tkinter.scrolledtext as ScrolledText
import funcoes


root = tk.Tk()
root.title("Protocolos CNJ")
# root.iconbitmap('imagens/icon.ico')

# ----------------------------------- CLASSES -----------------------------------------------------------
class TextHandler(logging.Handler):
    # This class allows you to log to a Tkinter Text or ScrolledText widget
    # Adapted from Moshe Kaplan: https://gist.github.com/moshekaplan/c425f861de7bbf28ef06

    def __init__(self, text):
        # run the regular Handler __init__
        logging.Handler.__init__(self)
        # Store a reference to the Text it will log to
        self.text = text

    def emit(self, record):
        msg = self.format(record)

        def append():
            self.text.configure(state='normal')
            self.text.insert(tk.END, msg + '\n')
            self.text.configure(state='disabled')
            # Autoscroll to the bottom
            self.text.yview(tk.END)

        # This is necessary because we can't modify the Text from other threads
        self.text.after(0, append)


# ------------------------------------Váriaveis Globais -------------------------------------------------

# Abrindo Arquivo de Configuração
arquivo_memoria = 'memoria.ini'
config = ConfigParser()
config.read(arquivo_memoria)

# Data atual
data_hoje_datetime = str(datetime.date.today())

listaCombobox = ["Aguardando Processamento",
                 "Processado com Sucesso",
                 "Duplicado",
                 "Processado com Erro",
                 "Erro no arquivo"]

protocolos = None


# ---------------------------------------------------------------------------------------------
# Da uma ohada no maskedntry
# Funções
def openfile():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(
        ("Todos os Arquivos", "*.*"), ("PDF Files", "*.pdf"), ("JPG Files", "*.jpg"), ("PNG Files", "*.png")))
    saveasfile_Entry.delete(0, tk.END)
    saveasfile_Entry.insert(0, root.filename)


def switch_button_state():
    # IF PARA SE DESATIVAR O BOTÃO, ELSE PARA SE ATIVAR!
    if (check2['state'] == tk.NORMAL and saveasfile_Entry['state'] == tk.NORMAL and selectfile_button[
        'state'] == tk.NORMAL):
        check2['state'] = tk.DISABLED
        # saveasfile_Entry.delete(0, tk.END)

        # Buffer Arquivo para não perder o nome do arquivo
        config['aplicacao']['bufferarquivo'] = config['aplicacao']['arquivonome']

        saveasfile_Entry['state'] = tk.DISABLED
        selectfile_button['state'] = tk.DISABLED
        check2.deselect()

    else:
        check2['state'] = tk.NORMAL
        saveasfile_Entry['state'] = tk.NORMAL
        saveasfile_Entry.delete(0, tk.END)
        saveasfile_Entry.insert(0, config['aplicacao']['bufferarquivo'])  # Inserindo o Buffer
        selectfile_button['state'] = tk.NORMAL


# Funções do DATE
def open_window_date(tipoData):
    if tipoData:
        data1 = 1
        data2 = 0

        if data1_entry.get() == "__/__/____":
            data1_entry.insert(0, dataManipulada(data_hoje_datetime, "juntar"))
        evento = data1_entry

    else:
        data1 = 0
        data2 = 1

        if data2_entry.get() == "__/__/____":
            data2_entry.insert(0, dataManipulada(data_hoje_datetime, "juntar"))
        evento = data2_entry


    top = tk.Toplevel()
    top.title("Defina a Data")
    top.geometry("400x300")

    cal = Calendar(top, selectmode="day", year=int(dataManipulada(evento.get(), "ano")),
                   month=int(dataManipulada(evento.get(), "mes")),
                   day=int(dataManipulada(evento.get(), "dia")),
                   locale='pt_BR')
    cal.pack(pady=20, fill="both", expand=True)

    submitedate = tk.Button(top, text="Selecionar Data", command=lambda: grab_date_calendar(data1, data2, cal, top)).pack(
        pady=(0, 10))


def grab_date_calendar(data1, data2, cal, top):
    datastring = cal.get_date()
    dataCalendar = dataManipulada(datastring, 'juntar')

    if data1 == 1:
        data1_entry.insert(0, dataCalendar)
    if data2 == 1:
        data2_entry.insert(0, dataCalendar)

    top.destroy()


def change_status():
    combobox["values"] = ["Aguardando Processamento",
                          "Processado com Sucesso",
                          "Duplicado",
                          "Processado com Erro",
                          "Erro no arquivo"
                          ]


def clear_all_requisicao():
    urlCNJ_entry.delete(0, tk.END)
    tribunal_entry.delete(0, tk.END)
    passwordTribunal_entry.delete(0, tk.END)
    numProtocolo_entry.delete(0, tk.END)
    combobox.current(0)


def buscar_paginas():
    global protocolos

    url = urlCNJ_entry.get()
    tribunal = tribunal_entry.get()
    senha_tribunal = passwordTribunal_entry.get()

    arq_protocolo = saveasfile_Entry.get()

    protocolos = ProtocolosCNJ(url=url,
                               arquivo=arq_protocolo, append_arquivo=sobrescrever.get(), grava_bd=savedatabase.get(),
                               tribunal=tribunal, senha_tribunal=senha_tribunal)

    params = get_params()

    paginas = protocolos.buscar_paginas(params)

    protocolos_por_paginas_entry.delete(0, tk.END)
    protocolos_por_paginas_entry.insert(0, paginas['registros_por_pagina'])

    total_protocolos_entry.delete(0, tk.END)
    total_protocolos_entry.insert(0, paginas['total_registros'])

    total_paginas_entry.delete(0, tk.END)
    total_paginas_entry.insert(0, paginas['paginas'])


def indexdocombobox():
    comboboxatual = str(combobox.current())
    index_trt = {
        "0": "1",
        "1": "3",
        "2": "5",
        "3": "6",
        "4": "7",
        "-1": "1"
    }
    return index_trt.get(comboboxatual)


def salvardados(*args):
    # Requisição
    config['requisicao']['urlEndpoint'] = urlCNJ_entry.get()
    config['requisicao']['tribunal'] = tribunal_entry.get()
    config['requisicao']['passwordTribunal'] = passwordTribunal_entry.get()
    config['requisicao']['numProtocolo'] = numProtocolo_entry.get()
    config['requisicao']['statusLabel'] = combobox.get()
    config['requisicao']['statusIndex'] = indexdocombobox()

    msg = 'Url CNJ = ' + urlCNJ_entry.get()
    logging.info(msg)

    if data1_entry.get() == "__/__/____":
        config['requisicao']['data_de'] = dataManipulada(data_hoje_datetime, "juntar")
    else:
        config['requisicao']['data_de'] = dataManipulada(data1_entry.get(), "juntar")

    if data2_entry.get() == "__/__/____":
        config['requisicao']['data_ate'] = dataManipulada(data_hoje_datetime, "juntar")
    else:
        config['requisicao']['data_ate'] = dataManipulada(data2_entry.get(), "juntar")

    # Aplicação
    config['aplicacao']['savefile'] = str(salvarcomoarquivo.get())
    config['aplicacao']['sobrescrever'] = str(sobrescrever.get())
    config['aplicacao']['salvarbanco'] = str(savedatabase.get())
    if saveasfile_Entry['state'] == tk.NORMAL:
        config['aplicacao']['arquivonome'] = saveasfile_Entry.get()

    # Escrevendo no arquivo memoria
    with open(arquivo_memoria, 'w') as configfile:
        config.write(configfile)


def recuperardados():
    # Requisição
    urlCNJ_entry.insert(0, config['requisicao']['urlEndpoint'])
    tribunal_entry.insert(0, config['requisicao']['tribunal'])
    passwordTribunal_entry.insert(0, config['requisicao']['passwordTribunal'])
    numProtocolo_entry.insert(0, config['requisicao']['numProtocolo'])
    combobox.insert(0, config['requisicao']['statusLabel'])
    data1_entry.insert(0, config['requisicao']['data_De'])
    data2_entry.insert(0, config['requisicao']['data_Ate'])

    # Aplicação
    if config['aplicacao']['savefile'] == 'True':
        salvarcomoarquivo.set(1)

        check2['state'] = tk.NORMAL
        saveasfile_Entry['state'] = tk.NORMAL

        saveasfile_Entry.insert(0, config['aplicacao']['arquivonome'])

        if config['aplicacao']['sobrescrever'] == 'True':
            sobrescrever.set(1)
    else:
        salvarcomoarquivo.set(0)
        sobrescrever.set(0)

        check2['state'] = tk.DISABLED
        saveasfile_Entry['state'] = tk.DISABLED

    if config['aplicacao']['salvarbanco'] == 'True':
        savedatabase.set(1)
    else:
        savedatabase.set(0)


def dataManipulada(dataParaManipular, funcao):
    if funcao == "inverter":
        # SPLIT EM: DD/MM/YYYY
        listaDeData = list(dataParaManipular.split("/"))
        return listaDeData[2] + '-' + listaDeData[1] + '-' + listaDeData[0]

    elif funcao in ["dia", "mes", "ano"]:
        data_index = {
            "dia": 0,
            "mes": 1,
            "ano": 2
        }
        listaDeData = list(dataParaManipular.split("/"))
        return listaDeData[data_index.get(funcao)]

    elif funcao == "juntar":
        if "/" in dataParaManipular:
            # FORMATO: DD/MM/YYYY
            dataList = dataParaManipular.split("/")
            dataOficial = dataList[0] + dataList[1] + dataList[2]

        if "-" in dataParaManipular:
            # FORMATO: YYYY-MM-DD
            todaysplit = dataParaManipular.split("-")
            today_day = todaysplit[2]
            today_month = todaysplit[1]
            today_year = todaysplit[0]

            dataOficial = today_day + today_month + today_year

        return dataOficial



def get_params():
    return {
        'protocolo': numProtocolo_entry.get(),
        'dataInicio': dataManipulada(data1_entry.get(), "inverter"),
        'dataFim': dataManipulada(data2_entry.get(), "inverter"),
        'status': indexdocombobox()
    }


def executar():
    tot_paginas = int(total_paginas_entry.get())
    paginas = range(1, tot_paginas + 1)
    executar_paginas(paginas)


def validate(event):
    # VALIDATE PARA EVENTOS DE DATA
    if event.widget is data1_entry or event.widget is data2_entry:
        data = event.widget.get()
        data = data.split("/")

        if event.widget is data1_entry:
            evento = data1_entry
        else:
            evento = data2_entry
            if data[0] + data[1] + data[2] == config['requisicao']['data_ate']:
                return

        # VERIFICAÇÕES
        try:
            datetime.datetime.strptime(evento.get(), '%d/%m/%Y')
        except ValueError:
            response = messagebox.showerror("Campo Data Inválido", "É necessário preencher o campo data corretamente!.")
            evento.clean()
            return

        # Atribuindo a Variaveis
        data1_entry_ano = dataManipulada(data1_entry.get(), "ano")
        data1_entry_mes = dataManipulada(data1_entry.get(), "mes")
        data1_entry_dia = dataManipulada(data1_entry.get(), "dia")

        data2_entry_ano = dataManipulada(data2_entry.get(), "ano")
        data2_entry_mes = dataManipulada(data2_entry.get(), "mes")
        data2_entry_dia = dataManipulada(data2_entry.get(), "dia")

        date1 = datetime.date(int(data1_entry_ano), int(data1_entry_mes), int(data1_entry_dia))
        date2 = datetime.date(int(data2_entry_ano), int(data2_entry_mes), int(data2_entry_dia))

        was_date1_before = date1 < date2

        if was_date1_before is False:
            response = messagebox.showerror("Data Incorreta", "Preencha o campo com uma data válida.")
            evento.clean()
            return

        # SALVAR NO ARQUIVO
        if evento.get().find('_') != -1:
            response = messagebox.showerror("Data Incorreta", "Preencha o campo com uma data válida.")
            evento.clean()
            return
        else:
            salvardados()

    else:
        salvardados()


def executar_paginas(paginas):
    # TODO Verificar se os campos necessários à execução foram todos preenchidos (parâmetros e páginas)

    global protocolos
    qtd_paginas = len(paginas)
    contador = 0
    params = get_params()
    paginas_erro = []

    for pagina in paginas:

        params['page'] = pagina

        if not protocolos.executar_pagina(params):
            paginas_erro.append(pagina)

        contador += 1
        progressBar['value'] = int((float(contador) / float(qtd_paginas)) * 100)
        paginas_processadas_entry.delete(0, tk.END)
        paginas_processadas_entry.insert(0, str(contador))
        paginas_erro_entry.delete(0, tk.END)
        paginas_erro_entry.insert(0, str(len(paginas_erro)))
        root.update_idletasks()

    return paginas_erro


# ---------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------

# Parâmetros da Requisição
frame_parametros = tk.LabelFrame(root, text="Parâmetros", padx=40, pady=15)
frame_parametros.grid(row=0, column=0, sticky=tk.E + tk.N + tk.S + tk.W, ipadx=5, ipady=5, padx=5, pady=5)
frame_parametros.grid_columnconfigure(0, weight=0)
frame_parametros.grid_columnconfigure(1, weight=0)
for i in range(9):
    frame_parametros.grid_rowconfigure(i, weight=1)



# Parametros de Aplicação
frame_aplicacao = tk.LabelFrame(frame_parametros, text="Parâmetros de Aplicação", padx=5, pady=5)
frame_aplicacao.grid(row=0, column=0, columnspan=2, padx=5, pady=(0, 5), ipadx=5, ipady=5, sticky=tk.E + tk.N + tk.W + tk.S)
for i in range(4):
    frame_aplicacao.grid_columnconfigure(i, weight=1)

# CheckBoxes
salvarcomoarquivo = tk.BooleanVar()
sobrescrever = tk.BooleanVar()
savedatabase = tk.BooleanVar()

# FIRST FRAME - PARÂMETRO DE APLICAÇÃO
check1 = tk.Checkbutton(frame_aplicacao, text="Salvar em Arquivo", variable=salvarcomoarquivo,
                        command=switch_button_state)
check1.bind("<Leave>", validate)
check1.grid(row=0, sticky=tk.W)

check2 = tk.Checkbutton(frame_aplicacao, text="Sobrescrever conteúdo\n anterior do arquivo", variable=sobrescrever)
check2.bind("<Leave>", validate)
check2.grid(row=1, padx=(10, 0))

namefile_label = tk.Label(frame_aplicacao, text="Nome arquivo: ")
namefile_label.grid(row=1, column=1, sticky=tk.E)
saveasfile_Entry = tk.Entry(frame_aplicacao, width=30)
saveasfile_Entry.bind("<FocusOut>", validate)
saveasfile_Entry.grid(row=1, column=2)

selectfile_button = tk.Button(frame_aplicacao, text="Select a File", relief=tk.RAISED, command=openfile)
selectfile_button.grid(row=1, column=3, padx=15)

check3 = tk.Checkbutton(frame_aplicacao, text="Salvar em Banco de Dados", variable=savedatabase)
check3.bind("<Leave>", validate)
# check3.deselect()
check3.grid(row=3, sticky=tk.W)



# -----------------------------------------------------------------------------------------------------

# Labels
urlCNJ_label = tk.Label(frame_parametros, text="URL endpoint CNJ:").grid(row=1, sticky=tk.E + tk.N + tk.W + tk.S, pady=5, padx=5)
tribunal_label = tk.Label(frame_parametros, text="Tribunal:").grid(row=2, pady=5, sticky=tk.E + tk.N + tk.W + tk.S, padx=5)
passwordTribunal_label = tk.Label(frame_parametros, text="Senha do Tribunal:").grid(row=3, pady=5, sticky=tk.E + tk.N + tk.W + tk.S, padx=5)
numProtocolo_label = tk.Label(frame_parametros, text="Nº Protocolo:").grid(row=4, pady=5, sticky=tk.E + tk.N + tk.W + tk.S, padx=5)

# Entrys
urlCNJ_entry = tk.Entry(frame_parametros, width=40)
urlCNJ_entry.bind("<FocusOut>", validate)
urlCNJ_entry.grid(row=1, column=1, sticky=tk.W+tk.E+tk.N+tk.S, pady=5)

tribunal_entry = tk.Entry(frame_parametros, width=40)
tribunal_entry.bind("<FocusOut>", validate)
tribunal_entry.grid(row=2, column=1, sticky=tk.W+tk.E+tk.N+tk.S, pady=5)

passwordTribunal_entry = tk.Entry(frame_parametros, show="*", width=40)
passwordTribunal_entry.bind("<FocusOut>", validate)
passwordTribunal_entry.grid(row=3, column=1, sticky=tk.W+tk.E+tk.N+tk.S, pady=5)

numProtocolo_entry = tk.Entry(frame_parametros, width=40)
numProtocolo_entry.bind("<FocusOut>", validate)
numProtocolo_entry.grid(row=4, column=1, sticky=tk.W+tk.E+tk.N+tk.S, pady=5)

# -----------------------------------------------------------------------------------------------------

# Status Combobox

status_label = tk.Label(frame_parametros, text="Status:").grid(row=5, sticky=tk.E + tk.N + tk.W + tk.S, pady=5, padx=5)
combobox = ttk.Combobox(frame_parametros, values=listaCombobox, postcommand=change_status, width=25, state="readonly")
combobox.bind("<FocusOut>", validate)
combobox.grid(row=5, column=1, sticky=tk.W+tk.E+tk.N+tk.S)

# -----------------------------------------------------------------------------------------------------

# Frame para Periodo
numero_protocolo_frame = tk.LabelFrame(frame_parametros, text="Período Correspondido")
numero_protocolo_frame.grid(row=7, columnspan=2, sticky=tk.N + tk.S + tk.W, padx=5, pady=5, ipadx=5, ipady=5)

# Buttons Calendar
calendarImage = ImageTk.PhotoImage(Image.open("imagens/calendar1.png").resize((20, 20), Image.ANTIALIAS))

# Variáveis que são usadas em 'which_data' para diferenciar qual é qual.
data_inicio = True
data_final = False

periodo_buttonInicio = tk.Button(numero_protocolo_frame, image=calendarImage, command=lambda: open_window_date(data_inicio))
periodo_buttonInicio.grid(row=0, column=2, padx=(5, 0), sticky=tk.E + tk.N + tk.W + tk.S)

periodo_buttonFinal = tk.Button(numero_protocolo_frame, image=calendarImage, command=lambda: open_window_date(data_final))
periodo_buttonFinal.grid(row=0, column=5, padx=(5, 0), sticky=tk.E + tk.N + tk.W + tk.S)

# Periodo Datas com Mask
global data1
data1 = 0
definedate1_label = tk.Label(numero_protocolo_frame, text="De:")
definedate1_label.grid(row=0)

data1_entry = MaskedWidget(numero_protocolo_frame, 'fixed', mask='99/99/9999')
data1_entry.grid(row=0, column=1, padx=(5, 0), pady=(5, 5))

global data2
data2 = 0
definedate2_label = tk.Label(numero_protocolo_frame, text="Até:")
definedate2_label.grid(row=0, column=3, padx=(10, 0))

data2_entry = MaskedWidget(numero_protocolo_frame, 'fixed', mask='99/99/9999')
data2_entry.grid(row=0, column=4, padx=(5, 0), pady=(5, 5))

# BIND FOCUSOUT
data1_entry.bind("<FocusOut>", validate)
data2_entry.bind("<FocusOut>", validate)

# -----------------------------------------------------------------------------------------------------

# Buttons
limpar_campos = tk.Button(frame_parametros, text="Limpar", command=clear_all_requisicao)
limpar_campos.grid(row=8, column=0, sticky=tk.E + tk.N + tk.S + tk.W, pady=(5, 0))

buscar_paginas = tk.Button(frame_parametros, text="Buscar Páginas", command=buscar_paginas)
buscar_paginas.grid(row=8, column=1, sticky=tk.E + tk.N + tk.S + tk.W, pady=(5, 0))

# -----------------------------------------------------------------------------------------------------

# FRAME PARA LOG
frame_log = tk.LabelFrame(root, text="Log de Execução", padx=5, pady=5)
frame_log.grid(row=0, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky=tk.E + tk.N + tk.W + tk.S)
frame_log.grid_columnconfigure(0, weight=1)
frame_log.grid_rowconfigure(0, weight=1)

st = ScrolledText.ScrolledText(frame_log, state='disabled')
st.configure(font='TkFixedFont')
st.pack()

# Create textLogger
text_handler = TextHandler(st)

# Logging configuration
logging.basicConfig(filename='test.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Add the handler to logger
logger = logging.getLogger()
logger.addHandler(text_handler)

# text_log = tk.Text(frame_log)
# text_log.pack()
# text_log.bind("<Key>", lambda e: "break")

# -----------------------------------------------------------------------------------------------------

# FRAME Resultados
frm_result = tk.LabelFrame(root, text='Resultados', pady=5)
frm_result.grid(row=1, column=0, ipadx=5, ipady=5, padx=5, pady=5, sticky=tk.E + tk.N + tk.S + tk.W)
frm_result.grid_columnconfigure(0, weight=0)
frm_result.grid_columnconfigure(1, weight=0)
frm_result.grid_rowconfigure(0, weight=0)
frm_result.grid_rowconfigure(1, weight=0)
frm_result.grid_rowconfigure(2, weight=0)

# Labels - Resultados
total_paginas_label = tk.Label(frm_result, text="Total de Páginas: ")
total_paginas_label.grid(padx=(30, 0), pady=(0, 5), sticky=tk.E)
protocolos_por_paginas_label = tk.Label(frm_result, text="Protocolos por Página: ")
protocolos_por_paginas_label.grid(padx=(30, 0), pady=(0, 5), sticky=tk.E)
total_protocolos_label = tk.Label(frm_result, text="Total de Protocolos: ")
total_protocolos_label.grid(padx=(30, 0), pady=(0, 5), sticky=tk.E)

# Entrys - Resultados
total_paginas_entry = tk.Entry(frm_result, width=40)
total_paginas_entry.grid(row=0, column=1, sticky=tk.W)
protocolos_por_paginas_entry = tk.Entry(frm_result, width=40)
protocolos_por_paginas_entry.grid(row=1, column=1, sticky=tk.W)
total_protocolos_entry = tk.Entry(frm_result, width=40)
total_protocolos_entry.grid(row=2, column=1, sticky=tk.W)

# -----------------------------------------------------------------------------------------------------

# FRAME Resumos Painel de Progresso

# Definindo Frame para tela
frame_progresspanel = tk.LabelFrame(root, text="Painel de Progresso", pady=5)
frame_progresspanel.grid(row=1, column=1, sticky=tk.E + tk.N + tk.S + tk.W, padx=5, pady=5, ipadx=5, ipady=5)
frame_progresspanel.grid_columnconfigure(0, weight=1)
frame_progresspanel.grid_columnconfigure(1, weight=1)
for i in range(4):
    frame_progresspanel.grid_rowconfigure(i, weight=0)

# Labels - Painel de Progresso
paginas_processadas_label = tk.Label(frame_progresspanel, text="Quantidade de Páginas Processadas: ")
paginas_processadas_label.grid(row=0, column=0, padx=(10, 0), pady=(0, 5), sticky=tk.E)
paginas_erro_label = tk.Label(frame_progresspanel, text="Quantidade de Páginas com Erro: ")
paginas_erro_label.grid(row=1, column=0, padx=(10, 0), pady=(0, 5), sticky=tk.E)
lista_paginas_erro = tk.Label(frame_progresspanel, text="Lista de Páginas com Erro: ")
lista_paginas_erro.grid(row=2, column=0, padx=(10, 0), pady=(0, 5), sticky=tk.E)

# Entrys - Painel de Progresso
paginas_processadas_entry = tk.Entry(frame_progresspanel, width=40)
paginas_processadas_entry.grid(row=0, column=1, sticky=tk.W)
paginas_erro_entry = tk.Entry(frame_progresspanel, width=40)
paginas_erro_entry.grid(row=1, column=1, sticky=tk.W)
lista_paginas_erro_entry = tk.Entry(frame_progresspanel, width=40)
lista_paginas_erro_entry.grid(row=2, column=1, sticky=tk.W)

# ProgressBar
progressBar = ttk.Progressbar(frame_progresspanel, orient=tk.HORIZONTAL, length=450, mode='determinate')
progressBar.grid(row=3, columnspan=2, pady=20, padx=20)

# -----------------------------------------------------------------------------------------------------

# Botão Executar e Executar Páginas com Erro
execute_button = tk.Button(root, text="Executar", relief=tk.GROOVE, command=executar)
execute_button.grid(row=2, column=0, sticky=tk.E + tk.N + tk.S + tk.W, padx=5, pady=5)

execute_erros_button = tk.Button(root, text="Executar Páginas com Erro", relief=tk.GROOVE, command=executar)
execute_erros_button.grid(row=2, column=1, sticky=tk.E + tk.N + tk.S + tk.W, padx=5, pady=5)

# -----------------------------------------------------------------------------------------------------
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)

recuperardados()
root.mainloop()

# a partir daqui ta o inicio de tudo
