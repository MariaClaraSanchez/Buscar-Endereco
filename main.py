from controllers.acessar_site import Site 
from controllers.config import Config
from controllers.relatorio import Planilha

def start():
    config = Config.get_config()
    
    rastreio = Site(config['user']['caminho'])
    dados_cep = rastreio.acessar_correios()
    print(dados_cep)
    planilha = Planilha()
    
    planilha.formatar_planilha()
    planilha.escreve_dados(dados_cep)
    
if __name__ == '__main__':
    start()