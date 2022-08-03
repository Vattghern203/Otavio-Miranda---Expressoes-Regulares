import re

string = "Aqui vemos um teste de Expressões Regualares. E mais teste teste teste :)"

print(re.search(r'teste', string))

print(re.findall(r'teste', string))

print(re.sub(r'teste', 'LESTE', string, count=0))

regexp = re.compile(r'teste')

print(regexp.search(string))

print(regexp.findall(string))

print(regexp.sub('Fire', string, count=1))
