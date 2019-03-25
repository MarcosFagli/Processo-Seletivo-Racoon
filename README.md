# Processo-Seletivo-Racoon
Tarefa da primeira fase do processo seletivo da Raccon Marketing Digital

## Problema

Você é responsável por um software de gestão de estoque de produtos. Ao fazer uma
alteração no sistema, uma rotina que não foi devidamente testada acabou quebrando todo o
banco de dados. Por sorte, não houve perda completa dos dados, mas eles não estão mais no
formato esperado pelo sistema. Sua missão nesse projeto é recuperar os dados e deixá-los no
formato adequado novamente. Além disso, você precisará criar também alguns métodos para
validação das correções.
O banco de dados utilizado é um banco de dados NoSQL, orientado a documentos. Não se
assuste caso você não conheça esses nomes. Não iremos mexer diretamente com banco de
dados, mas somente com o documento, em formato JSON, onde estão armazenados os dados
de produto.
Problemas detectados no banco de dados corrompido

### 1. Nomes
Todos os nomes de produto tiveram alguns caracteres modificados, houve substituição
de todos os "a" por "æ", "c" por "¢", "o" por "ø", "b" por "ß". É preciso reverter essas
substituições para recuperar os nomes originais.
Exemplo:
Original:
```
"name" = "Lava & Seca 10,2 Kg Samsung Eco bubble branca com 09 Programas de Lavagem"
```
Corrompido:
```
"name" = "Lævæ & Se¢æ 10,2 Kg Sæmsung E¢ø ßußßle ßræn¢æ ¢øm 09 Prøgræmæs de Lævægem"
```

### 2. Preços
Os preços dos produtos devem ser sempre do tipo number, mas alguns deles estão no
tipo string. É necessário transformar as strings novamente em number.
Exemplo:
Original:
```
"price" = 1250.00
```
Corrompido:
```
"price" = "1250.00"
```

### 3. Quantidades
Nos produtos onde a quantidade em estoque era zero, o atributo "quantity" sumiu. Ele
precisa existir em todos os produtos, mesmo naqueles em que o estoque é 0.
Exemplo:
Original:
```
{
    "id": 1316334,
    "name": "Refrigerador bottom Freezer Electrolux de 02 Portas Frost Free com 598 Litros",
    "quantity": 0,
    "price": 3880.23,
    "category": "Eletrodomésticos"
}
```
Corrompido:
```
{
    "id": 1316334,
    "name": "Refrigerador bottom Freezer Electrolux de 02 Portas Frost Free com 598 Litros",
    "price": 3880.23,
    "category": "Eletrodomésticos"
}
```

## Questões:

Para esse projeto, você utilizará o arquivo broken-database.json e irá fazer
uma série de transformações até que ele volte ao formato original. Para isso será necessário
desenvolver algumas funções e depois verificar se realmente foi recuperado. Você deverá
utilizar JavaScript ou Python para resolver esse problema, caso não conheça nenhuma
dessas linguagens, é uma ótima oportunidade para aprender! :)

### 1. Recuperação dos dados originais do banco de dados
Você deverá criar três funções para percorrer o banco de dados corrompido e corrigir os três
erros descritos anteriormente:
```
a) Nos nomes;
b) Nos preços;
c) Nas quantidades.
```
Implementar e entregar as três funções separadamente para correção. Enviar também para
correção um arquivo com o banco de dados corrigido, ou seja, após passar pelas três funções.

### 2. Validação do banco de dados corrigido
Você deverá implementar funções para validar a sua recuperação do banco de dados. Todas
essas funções deverão ter como input o seu banco de dados corrigido na questão 1. As
funções de validação são:
```
a) Uma função que imprime a lista com todos os nomes dos produtos, ordenados primeiro
por categoria em ordem alfabética, depois ordenados por id em ordem crescente;
b) Uma função que calcula qual é o valor total do estoque por categoria, ou seja, a soma
do valor de todos os produtos em estoque de cada categoria, considerando a
quantidade de cada produto.
```
Implementar e entregar as 2 funções separadamente para correção. Enviar também para
correção qual foi a saída para cada uma delas.

## Soluções:
A tecnica utilizada para realizar as tarefas foram as seguintes:
### 0. Pré solução:
Antes de realizar as funções para tratamento dos erros, foi aberto o arquivo broken-database.json. Utilizando a biblioteca em python para json, as informações json foram transformadas em um dicionário python e em seguida, uma lista de dicionários foi criada. 
A função ReadFile é responsável por esse processamento e retorna uma lista de dicionários python

### 1. Correção dos nomes:
Para a correção dos nomes, foi criada uma função chamada Replace, que percorre a lista de dicionários, e para cada dicionário, analisa a chave "name", buscando pelos caracteres corrompidos, e alterando-os.

### 2. Correção dos preços:
Para a correção dos preços, foi criada uma função chamada ConvertPrice, que percorre a lista de dicionários, e para cada dicionário, reinsere o conteúdo do dicionário na chave "price", com uma conversão para float (tipo de dado number, quando convertido para json) do proprio conteúdo da chave price, naquele dicionário.

### 3. Correção do conteúdo:
Para a correção da falta do campo "quantity", foi criada uma função chamada InsertQuantity, que percorre a lista de dicionários, e para cada dicionário, verifica se a chave "quantity" existe naquele dicionário. Caso não exista, aquela posição da lista é reposta com todos os dados do dicionário presente, acrescido do campo "quantity" com valor 0.

### 4. Imprimir a lista com os nomes por ordem alfabética de categoria e em seguida ordenados por ordem crescente de ID:
Imprime uma lista somente com os nomes, impressa primeiramente por ordem alfabética de categoria e em seguida, impressa por ordem númerica. 
Para esta tarefa foi criada a função PrintName. Nela o dicionário é quebrado em três vetores com nome, quantidade e Id, a partir desses foi utilizado a função sorted, nativa do python, para ordenar, por meio de outro vetor, o vetor nome. Esta regra foi aplicada para as duas formas de ordenação.

Saída (ordenação por categoria):
```
Impressao dos nomes por categoria:
1 Mouse Gamer Predator cestus 510 Fox Preto
2 Fogão de Piso Electrolux de 04 bocas, Mesa de Vidro Prata
3 Forno Micro-ondas Panasonic com capacidade de 21 Litros branco
4 Lava & Seca 10,2 Kg Samsung Eco bubble branca com 09 Programas de Lavagem
5 Refrigerador bottom Freezer Electrolux de 02 Portas Frost Free com 598 Litros
6 Home Theater LG com blu-ray 3D, 5.1 canais e 1000W
7 Kit Gamer acer - Notebook + Headset + Mouse
8 Monitor 29 LG FHD Ultrawide com 1000:1 de contraste
9 Smart TV 4K Sony LED 65” 4K X-Reality Pro, UpScalling, Motionflow XR 240 e Wi-F
10 Conjunto de Panelas antiaderentes com 05 Peças Paris
```
Saída (Ordenação por ID):
```
Impressao dos nomes por ID:
1 Refrigerador bottom Freezer Electrolux de 02 Portas Frost Free com 598 Litros
2 Mouse Gamer Predator cestus 510 Fox Preto
3 Kit Gamer acer - Notebook + Headset + Mouse
4 Monitor 29 LG FHD Ultrawide com 1000:1 de contraste
5 Conjunto de Panelas antiaderentes com 05 Peças Paris
6 Fogão de Piso Electrolux de 04 bocas, Mesa de Vidro Prata
7 Smart TV 4K Sony LED 65” 4K X-Reality Pro, UpScalling, Motionflow XR 240 e Wi-F
8 Forno Micro-ondas Panasonic com capacidade de 21 Litros branco
9 Lava & Seca 10,2 Kg Samsung Eco bubble branca com 09 Programas de Lavagem
10 Home Theater LG com blu-ray 3D, 5.1 canais e 1000W
```

### 5. Imprimir as categorias e valores em estoque de cada uma.
Imprime uma lista com as categorias disponíveis e os valores em estoque de cada categoria.
Para esta tarefa foi criada a função CategoryCust. Nesta se percorre a lista de dicionários, e para cada nova categoria detectada, a categoria, e o valor é colocado em uma nova lista. Ainda, quando a categoria detectada já existe no vetor, é apenas somado o valor de estoque existente, com a multiplicação entre quantidade do produto e seu preço.
No final é impresso a lista gerada com categoria e valor, e no fim, é impresso "Total", com o valor total em estoque.
Saída:
```
Valor dos produtos por categoria em estoque:
Panelas = 4049.64
Eletrodomésticos = 315752.67
Eletrônicos = 203989.20
Acessórios = 0.00
Total = 523791.51
```

