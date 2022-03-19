from controllers.acessar_site import Site 
from controllers.config import Config

def start():
    config = Config.get_config()
    
    rastreio = Site(config['user']['caminho'])
    rastreio.acessar_google()
   

if __name__ == '__main__':
    start()