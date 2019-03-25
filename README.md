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
