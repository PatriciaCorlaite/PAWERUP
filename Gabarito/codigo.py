# entrar no sistema da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time


# pausa a cada comando 1s
pyautogui.PAUSE = 2
# aperta a tecla windows
pyautogui.press("win")
# digite o nome do programa
pyautogui.write("chrome")
# aperta enter
pyautogui.press("enter")
# digitar o link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
# aperta enter 
pyautogui.press("enter")

# esperar 5 segundos
time.sleep(5)
# fazer login
pyautogui.click(x=496, y=374)
# digitar e-mail
pyautogui.write("automacao@gmail.com")
# passar para o campo de senha
pyautogui.press("tab")
# digitar senha 123456
pyautogui.write("123456")
# clicar em enter
pyautogui.click(x=682, y=521) 

import pandas as pd
tabela = pd.read_csv('gabarito\produtos.csv')
#print(tabela)

for linha in tabela.index:  

    #cadastrar produtos 
    pyautogui.click(x=676, y=488) 
    #codigo 
    pyautogui.press("tab")
    pyautogui.write (str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    #marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    #tipo   
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"])) #para numero"1"
    pyautogui.press("tab")
    #preco_unitario
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"])) 
    pyautogui.press("tab")
    #custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    #obs
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write("obs")

    #Enviar produto
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)

