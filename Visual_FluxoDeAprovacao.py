import json
import re
import requests
import schedule
import threading
import time
import tkinter as tk
from tkinter import messagebox
from requests.auth import HTTPBasicAuth
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os
from datetime import datetime

# Configurações do Jira
jira_url = 'https://atlassian.net'
username = 'vinicius.crepaldi.br'
api_token = 'JLsCE11hYes7P_aWz1xnVAH'
#Filtro para buscar chamados que estão com status aguardando aprovação
filter_id = ""

# Variável global para controle da execução do programa
programa_em_execucao = True

# Função para buscar os issues de um filtro
def buscar_chamados_do_filtro(filter_id):
    pass

# Função para obter os comentários de um chamado específico
def obter_comentarios_chamado(issue_key):
    pass

# Função para extrair o e-mail do superior imediato e um e-mail adicional, se presente
def extrair_email_superior(comments):
    pass

# Função para adicionar um comentário ao chamado
def adicionar_comentario(issue_key, comentario):
    pass

# Função para enviar e-mail
def enviar_email(chamado_numero, email_destino, email_copia=None, nome_completo=""):
    pass

# Função para verificar se já foi enviado e-mail e comentário no mesmo dia
def email_enviado_hoje(comments):
    pass

# Função para verificar chamados e agir
def verificar_chamados_e_iniciar_processo():
    pass

# Interface gráfica com controle de execução
def iniciar_interface_grafica():
    def iniciar_programa():
        pass

    def parar_programa():
        pass

    def executar_programa():
        pass

    root = tk.Tk()
    root.title("Fluxo de aprovação, aguardando aprovação")

    log_text = tk.Text(root, height=10, width=50)
    log_text.pack()

    iniciar_btn = tk.Button(root, text="Iniciar Programa", command=iniciar_programa)
    iniciar_btn.pack(side=tk.LEFT)

    parar_btn = tk.Button(root, text="Parar Programa", command=parar_programa, state=tk.DISABLED)
    parar_btn.pack(side=tk.LEFT)

    root.mainloop()

# Iniciar interface gráfica
iniciar_interface_grafica()
