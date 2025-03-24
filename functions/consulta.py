from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from time import sleep
from os import environ
from dotenv import load_dotenv
load_dotenv()

driver_path = environ.get('CHROMEDRIVER')

def consulta(nomeC,cel,email):
    global url 
    url = "https://bit.ly/3hPam49"
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--allow-insecure-localhost')
    # driver = webdriver.Chrome(options=options, service=Service(driver_path))
    # driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    driver = webdriver.Chrome(service=Service(ChromeDriverManager(driver_version=driver_path).install()))
    driver.get(url)
    sleep(7)

    driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/button[1]").click()
    sleep(1)
    driver.find_element(By.XPATH,"//*[@id='Padrao2000_Nome']").send_keys(nomeC)
    sleep(1)
    driver.find_element(By.XPATH,"//*[@id='Padrao2000_Telefone_celMod1']").send_keys(cel)
    sleep(1)
    driver.find_element(By.XPATH,"//*[@id='Padrao2000_E_mail']").send_keys(email)
    sleep(3)
    driver.find_element(By.XPATH,"//*[@id='DIVPadrao2000_Modelo']/div/span/span[1]/span").click()
    sleep(1)
    driver.find_element(By.XPATH,"/html/body/span/span/span[1]/span/input").send_keys(modelo)
    sleep(1)
    driver.find_element(By.XPATH,"//*[@id='select2-Padrao2000_ModeloSelect-results']/li[1]/ul/li").click()
    sleep(3)
    driver.find_element(By.XPATH,"//*[@id='DIVPadrao2000_Anofabricacao']/div/div[2]/label[1]").click()
    sleep(10)
    driver.find_element(By.XPATH,"//*[@id='select2-Padrao2000_Cobertura8999-container']").click()
    sleep(3)
    driver.find_element(By.XPATH,"//*[@id='select2-Padrao2000_Cobertura8999-result-bcdk-3']").click()

nomeC = "Vinicius De Araujo"
cel = "85 989313544"
email = "viniciusderarujop@gmail.com"
modelo = "Royal"
consulta(nomeC,cel,email)