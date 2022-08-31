'''
from validate_docbr import CPF
from cpf_cnpj import Cpf
cpf = CPF()
print(cpf.validate("012.345.678-90"))
'''

import requests

from acesso_cep import BuscaEndereco
cep = "01001000"
objeto_cep = BuscaEndereco(cep)

#r = requests.get("https://viacep.com.br/ws/01001000/json/")
#print(r.text)

bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(bairro, cidade, uf)