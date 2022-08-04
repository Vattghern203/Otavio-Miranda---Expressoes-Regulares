# Metacaracteres: ^ $ * ? { } [ ] \ | ( )

# Quantificadores

# * = 0 ou n.
# + = 1 ou n.
# ? = 0 ou 1.

# {} = {n}, {min} ou {max} 
# Ex: ()+ & [a-zA-z0-9]+
# Ex2: {10,} = 10 ou mais & {,10} = De 0 até 10.
# Ex3: {10} = Especificamente 10.
# Ex4: {5,10} = Um range de 5 a 10.

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm... veeem... veem...vem"!
'''

# Os quantificadores aplicam seu efeito a letra ou conjunto que se encontra a sua esquerda.
print(re.findall(r'j[A-Z]+ão+', texto, flags=re.IGNORECASE))

print(re.sub(r'jo+ão+', 'Pedrola', texto, flags=re.IGNORECASE))

print(re.sub(r'jo?ão*', 'Pedrola', texto, flags=re.IGNORECASE))

# Serve para o mesmo propósito do + (O primeiro print)
print(re.findall(r'jo{1,}ão{1,}', texto, flags=re.IGNORECASE))

print(re.findall(r've{3}m{1,2}', texto, flags=re.IGNORECASE))

texto2 = 'João ama ser amado!'

print(re.findall(r'ama[od]{0,2}', texto2, flags=re.IGNORECASE))



