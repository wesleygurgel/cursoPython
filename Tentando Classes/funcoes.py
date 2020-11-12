from aplicacao import root, check2, saveasfile_Entry, selectfile_button, config, data1_entry, data_hoje_datetime, data2_entry, combobox, urlCNJ_entry, tribunal_entry, passwordTribunal_entry, numProtocolo_entry, protocolos_por_paginas_entry, sobrescrever, savedatabase, total_protocolos_entry, total_paginas_entry, salvarcomoarquivo, arquivo_memoria, progressBar, paginas_processadas_entry, paginas_erro_entry
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