'''
Ingrid Lima dos Santos

	Para obter os pontos relativos a este trabalho, você deverá fazer um programa, usando a linguagem de programação que desejar, que seja capaz de validar expressões de lógica proposicional escritas em latex e definir se são expressões gramaticalmente corretas. Você validará apenas a forma da expressão (sintaxe).  
	A entrada será fornecida por um arquivo de textos que será carregado em linha de comando, com a seguinte formatação:  
		1. Na primeira linha deste arquivo existe um número inteiro que informa quantas expressões 
lógicas estão no arquivo.
		2. Cada uma das linhas seguintes contém uma expressão lógica que deve ser validada.  
	A saída do seu programa será no terminal padrão do sistema e constituirá de uma linha de saída 
para cada expressão lógica de entrada contendo ou a palavra valida ou a palavra inválida e nada mais.

Gramática:
	Formula=Constante|Proposicao|FormulaUnaria|FormulaBinaria.  
	Constante="T"|"F". 
	Proposicao=[a−z0−9]+ 
	FormulaUnaria=AbreParen OperadorUnario Formula FechaParen 
	FormulaBinaria=AbreParen OperatorBinario Formula Formula FechaParen 
	AbreParen="(" 
	FechaParen=")" 
	OperatorUnario="¬" 
	OperatorBinario="∨"|"∧"|"→"|"↔" 
'''
import re

archive = open('test.txt')
lines = archive.readline()

regex = r"^[a-z0-9TF ()\\]+$"

for line in archive:
	if re.search(regex, line):
		print('válida')
	else:
		print('inválida')


