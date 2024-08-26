from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time, os, re

pagina = 1
try:
    driver = webdriver.Chrome()
except Error as E:
    print(f'An Error has occurred --> {E}')

def buscar_vagas():
    global pagina
    global driver
    driver.implicitly_wait(10)
    try:
        #Acessando portal de vagas
        if pagina == 1:
            driver.get("https://www.divulgavagas.com.br/")
        driver.implicitly_wait(50)
        
        # print("Entrando no if")
        # if driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div/div[3]/button'):
        #     driver.quit()
        #     time.sleep(10)
        #     buscar_vagas()
        # print("Saindo do IF")
        
        driver.implicitly_wait(3)
        #Digitando a vaga que está sendo buscada
        if pagina == 1:   
            driver.find_element(By.XPATH, '//*[@id="input_vaga"]').send_keys("Desenvolvedor")
            driver.implicitly_wait(3)
            #Acionando o botão de busca
            driver.find_element(By.XPATH, '//*[@id="formFiltro"]/div/div[2]/button').click()
            driver.implicitly_wait(3)

        #Pegando a lista com todos os links da página
        links = driver.find_elements(By.XPATH,"//a")
        lista_link = []
        for x in links:
            lista_link.append(x.get_attribute("href"))
        print(lista_link)
        #montando uma lista com todos 
        #link_texto = [f'{x.text}->{x.get_attribute("href")}'  for x in list_elements]
        create_email(lista_link)
    except:
        print(f'An Error Occurred --> Entrando na Re-chamada da função')
        driver.quit()
        #time.sleep(120)
        #buscar_vagas()
    if pagina >= 1 and pagina <= 5:
        print(f"Mudando de página {pagina}")
        driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/nav/ul/li[8]').click()
        return buscar_vagas()

def create_email (links: list):
    print("Entrando -> Create Email")
    global pagina
    atual = ''
    email: str = f" Pagina {pagina} \n"
    for x in links:
        x = validar_os_links(x)
        if x != "" and x != atual:
            atual = x
            email += f"link para vaga -> {x}; \n"
    print(email)
    escrevendo_arquivo(email)


def escrevendo_arquivo(email: str):
    print("Entrando -> escrevendo arquivo")
    global pagina
    try:
        try:
            arquivo = open(f'vagas{pagina}.txt', 'w')
        except:
            print("houve algum erro ao abrir o arquivo")
        try:    
            arquivo.write(f' {email} \n')
            print('teste')
            pagina += 1
            arquivo.write('############################################################')
        except:
            print("Erro na escrita no arquivo!")
    except:
        print("Erro no processo!!!")
    return 0


def validar_os_links(link: str)-> str:
    print('Entrando -> Validar os links')
    pattern = '.+\/vaga-de-emprego\/.+'
    if re.search(pattern, link):
        return link
    else:
        return ""

buscar_vagas()


# if :
#     buscar_vagas()