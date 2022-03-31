from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class Site:
    def __init__(self, caminho_driver: str) -> None:
        """Instancia a classe com as configurações iniciais
        Args: 
            caminho_driver (str): caminho do executavel do chromedriver 
        """
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--lang=pt-BR')
        chrome_options.add_argument('disable-infobars')
        chrome_options.add_argument('--log-level=3')

        self.driver = webdriver.Chrome(caminho_driver,
                                       options=chrome_options)

    def acessar_correios(self) -> dict:
        """Acessa o site do google
        """
        lista_ceps = ['37713-300','28953-818','28954-785','28959-100']
        #lista_ceps = ['37713-300','28953-818']
        self.driver.get('https://buscacepinter.correios.com.br/app/endereco/index.php')
        xpath_endereco = '//*[@id="endereco"]'
        xpath_click = '//*[@value="ALL"]'
        xpath_botao = '//*[@name="btn_pesquisar"]'
        xpath_voltar = '//*[@name="btn_voltar"]'
        
        dados = {}
        
        for cep in lista_ceps:
            time.sleep(2)
            #self.driver.find_element(By.XPATH, xpath_endereco).send_keys('37586-000')
            self.driver.find_element(By.XPATH, xpath_endereco).send_keys(cep)
            time.sleep(2)
            self.driver.find_element(By.XPATH, xpath_click).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, xpath_botao).click()
            time.sleep(4)
            
            rua = self.driver.find_element(By.XPATH,'//*[@id="resultado-DNEC"]/tbody/tr/td[{}]'.format(1)).text
            bairro = self.driver.find_element(By.XPATH,'//*[@id="resultado-DNEC"]/tbody/tr/td[{}]'.format(2)).text
            cidade = self.driver.find_element(By.XPATH,'//*[@id="resultado-DNEC"]/tbody/tr/td[{}]'.format(3)).text
            
            #print(cep + " - " + rua + " - " + bairro + " - " + cidade)

            dados.update({cep: {
                'rua': rua,
                'bairro': bairro,
                'cidade': cidade
            }})
            
            
            
            time.sleep(4)
            self.driver.find_element(By.XPATH,xpath_voltar).click()
        #print(dados)
        return dados