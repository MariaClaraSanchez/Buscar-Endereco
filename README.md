# Robô que extrai dados do site do correios e insere eles uma planilha

Essa solução foi desenvolvida utilizando puramente a linguagem de programação Python com algumas bibliotecas, o objetivo dessa automação é apenas treinar python, com ela foi possível entrar no site dos correios e extrair os dados de um determinado cep, tais como : Nome da Rua, bairro e cidade e logo depois o robô cria uma planilha formata ela e insere os dados que obteve no site dos correios.
  
# Configuração
## Máquina Virtual
Caso queira executar o projeto separadamente da onde fica seus documentos python é preciso cria uma máquina virtual e para isso precisa da os seguintes passos:
<br>
1º Instalar o env em sua máquina para isso utilize o comando :
```
pip install venv
```
2º Criar sua máquina virtual:
```
python3 -m venv nome_maquina_virtual-env
```
3º Escolha o comando de acordo com seu sistema opercional:
#### Para Windows:
```
nome_maquina_virtual-env\Scripts\activate.bat
```
#### Para Unix ou no MacOS:
```
source nome_maquina_virtual-env/bin/activate
```

## Instalando Dependências
Antes de iniciar o projeto é necessário instalar as configurações de ambiente de um modo mais fácil e prático é só usar o gerenciado de pacote [pip](https://pip.pypa.io/en/stable/) para instalar as dependências.
```bash
pip install -r requirements.txt
```

# Inicializando

Para executar o robô basta executar o comando :

```
pyhton main.py
```
