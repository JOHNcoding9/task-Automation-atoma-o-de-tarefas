#1 etapa: entrar no Chrome
#2 etapa: entrar no link do sistema da empresa https://dlp.hashtagtreinamentos.com/python/intensivao/login
#3 etapa : fazer o login
#4 etapa: cadastrar o produto
#5 etapa repetir esse processo até o fim da lista
import pyautogui
import pandas
tabela=pandas.read_csv("produtos.csv")
from time import sleep 
pyautogui.PAUSE= 0.5
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
pyautogui.click(x=540, y=852)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
sleep(2)
pyautogui.click(x=682, y=375)
pyautogui.write("JOHNlindo2024@gmail.com")
pyautogui.press("tab")
pyautogui.write("7894361211")
pyautogui.click(x=948, y=530)
sleep(3)
#código do produto
for linha in tabela.index:
 pyautogui.click(x=680, y=255)
 codigo=str(tabela.loc[linha,"codigo"]) #localizar na tabela a linha (1 por exemplo) na coluna ("codigo")
 pyautogui.write(codigo)
#Marca
 pyautogui.press("tab")
 marca=str(tabela.loc[linha,"marca"])
 pyautogui.write(marca)
#tipo
 pyautogui.press("tab")
 tipo=str(tabela.loc[linha,"tipo"])
 pyautogui.write(tipo)
#categoria
 pyautogui.press("tab")
 categoria=str(tabela.loc[linha,"categoria"])
 pyautogui.write(categoria)
#preço
 pyautogui.press("tab")
 preco_unitario=str(tabela.loc[linha,"preco_unitario"])
 pyautogui.write(preco_unitario)
#custo
 pyautogui.press("tab")
 custo=str(tabela.loc[linha,"custo"])
 pyautogui.write(custo)
#obs
 pyautogui.press("tab")
 obs=str(tabela.loc[linha,"obs"])
 if obs!="nan":
  pyautogui.write(obs)
 #póximo item
 pyautogui.click(x=875, y=902)
 pyautogui.scroll(5000)