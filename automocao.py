import pyautogui
pyautogui.PAUSE = 0.5
import time
import pandas as pd


# Passo 1: Entrar no site
# Abrir navegador (chrome)
pyautogui.press ("win")
pyautogui.write ("chrome")
pyautogui.press ("enter")
time.sleep(2)

# Inserir e acessar Link do site
pyautogui.click(x=397, y=85)
link = "dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(1)

# Passo 2: Fazer Login
# Seleciona o campo de login
pyautogui.press("tab")
# Insere o email
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
# Insere a senha
pyautogui.write("sua senha")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(1)

# Passo 3: Importar base da dados para cadastro
tabela = pd.read_csv("produtos.csv")

# Passo 4: Cadastro de produtos
for linha in tabela.index:
    pyautogui.click(x=742, y=328)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.press(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    if not pd.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(tabela.loc[linha, "obs"])
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
    time.sleep(1)