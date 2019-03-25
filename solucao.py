#Autor: Marcos Augusto Faglioni Junior
#Objetivo: Corrigir um arquivo Json - Processo seletivo Racoon
#Data: 24/03/2019

import json

#Nome do arquivo json sem .json
file = "broken-databases"

#Funcao: ReadFile
#Objetivo: Ler o arquivo json e converter cada mensagem em um elemento de uma lista python
#Parametros: Nome do arquivo.json
#Retorno: Lista python com elementos da mensagem json
def ReadFile(name):
	#Abrindo o arquivo como leitura
	fileOld = open(name + ".json", "r")

	#Lendo o arquivo
	content = fileOld.read()

	#Separando cada mensagem json por um marcador unico
	content = content.split("}")

	#Criar uma lista vazia para armazenamento da conversao json python
	contentPy = []

	#Percorrer cada elemento do vetor, reinserindo o '}' retirado por ser um marcador unico no fim de cada elemento, e entao converter por meio da biblioteca json, o json informado em str python
	for i in range(len(content)-1):
		#Reinserindo elemento '}
		content[i] = content[i] + "}"

		if(i==0):
			#Primeiro elemento do vetor possui estrutura diferente, remover somente o '['
			content[i] = content[i][1:len(content[i])]
		else:
			#Outros elementos do vetor deve-se retirar ",\n"
			content[i] = content[i][3:len(content[i])]

		#Inserindo cada mensagem json convertida no vetor
		contentPy.append(json.loads(content[i]))

	#Fechando o arquivo para evitar falhas no mesmo
	fileOld.close()

	#Retorno da lista de produtos (cada elemento eh um produro em dicionario python)
	return contentPy


#Funcao: StoreFile
#Objetivo: Armazenar em um arquivo json  o dicionario python 
#Parametros: Lista python com elementos da mensagem json; Nome do arquivo.json
#Retorno: Sem retorno (Adiciona um arquivo na pasta do programa com o nome do arquivo original acrescido da palavra new)
def StoreFile(listStr, name):
	#Abre ou cria um arquivo chamado name+new.json
	fileNew = open(name + "new.json", "w")

	#Cria uma string para armazenar os retornos da transformacao entre dicionario python e json
	string = '['

	#Traducao de cada elemento do dicionario
	for i in range(len(listStr)):
		string = string + json.dumps(listStr[i], indent=4, ensure_ascii=False) + ",\n"

	string = string + ']'	

	#Escreve no arquivo aberto
	fileNew.write(string)

	#Fecha o arquivo para não ocorrer falhas
	fileNew.close()


#Funcao: Replace
#Objetivo: Corrigir o campo "name" de um dicionario, para realizar as seguintes modificacoes: 'ø' por 'o'; 'æ' por 'a'; '¢' por 'c'; 'ß' por 'b'
#Parametros: Lista com elementos no formato lista de dicionario python que possua um campo "name"
#Retorno: Lista python com elementos da mensagem json corrigidos no campo "name"
def Replace(listStr):
	#Percorre todos os nomes, buscando as letras alteradas, e no caso de combinação, altera a mesma pela respectiva
	for i in range(len(listStr)):
		listStr[i]["name"] = listStr[i]["name"].replace('ø', 'o').replace('æ', 'a').replace('¢', 'c').replace('ß', 'b')

	return listStr


#Funcao: ConvertPrice
#Objetivo: Converter o campo "price" de cada entrada de um dicionario para valor inteiro
#Parametros: Lista com elementos no formato lista de dicionario python que possua um campo "price"
#Retorno: Lista python com elementos da mensagem json corrigidos no campo "price"
def ConvertPrice(listStr):
	#Para cada valor do campo "price", converte o valor para ponto flutuante (float)
	for i in range(len(listStr)):
		listStr[i]["price"] = float(listStr[i]["price"])

	return listStr


#Funcao: InsertQuantity
#Objetivo: Inserir o campo "quantity" com valor igual a 0, em um dicionario numa lista, caso não exista
#Parametros: Lista com elementos no formato lista de dicionario python
#Retorno: Lista python com elementos da mensagem json corrigidos com o campo "quantity"
def InsertQuantity(listStr):
	#Caso nao exista o campo "quantity", o mesmo sera criado com 0 unidades
	for i in range(len(listStr)):
		if not("quantity" in contentPy[i]):
			listStr[i] = {'id': listStr[i]["id"], 'name': listStr[i]["name"], 'quantity': 0, 'price': listStr[i]["price"], 'category': listStr[i]["category"]}

	return listStr


#Funcao: PrintName
#Objetivo: Printar no terminal uma lista com os nomes de produtos por ordem alfabetica de categoria, em seguida, uma lista com os nomes dos produtos ordenados por ordem crescente de ID
#Parametros: Lista com elementos no formato lista de dicionario python
#Retorno: Sem retorno
def PrintName(listStr):
	#Criação dos vetores temporarios 
	category = []
	name = []
	ID = []

	#Preenchimento dos vetores com o conteudo das listas de dicionarios
	for i in range(len(listStr)):
		category.append(listStr[i]["category"])
		name.append(listStr[i]["name"])
		ID.append(listStr[i]["id"])

	#Impressao por ordem de categoria
	#Criacao do vetor ordenado de nomes por cateoria
	orderNames = [name for category, name in sorted(zip(category,name))]

	#Impressao dos nomes por categoria
	print("Impressao dos nomes por categoria:")
	for i in range(len(orderNames)):
		print(str(i+1) + " " + orderNames[i])

	print("\n\n")

	#Impressao por ordem de id
	#Criacao do vetor ordenado de nomes por ID
	orderNames = [name for ID, name in sorted(zip(ID,name))]

	#Impressao dos nomes por ID
	print("Impressao dos nomes por ID:")
	for i in range(len(orderNames)):
		print(str(i+1) + " " + orderNames[i])
	print()


def CategoryCust(listStr):
	category = []
	value = []

	for i in range(len(listStr)):
		if listStr[i]["category"] in category:
			value[category.index(listStr[i]["category"])] = value[category.index(listStr[i]["category"])] + listStr[i]["price"] * listStr[i]["quantity"]
		else:
			category.append(listStr[i]["category"])
			value.append(listStr[i]["price"] * listStr[i]["quantity"])

	print("Valor dos produtos por categoria em estoque:")
	for i in range(len(category)):
		print(category[i] + " = " + "{0:.2f}".format(value[i]))

	print("Total = " + "{0:.2f}".format(sum(value)))
	print()



contentPy = ReadFile(file)
contentPy = Replace(contentPy)
contentPy = ConvertPrice(contentPy)
contentPy = InsertQuantity(contentPy)
PrintName(contentPy)
CategoryCust(contentPy)
StoreFile(contentPy, file)