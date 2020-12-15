# blockchain
Aplicação com uso de Blockchain em python 
O termo blockchain pode ser utilizado para representar aplicações de criptomoedas, bem como uma lista de registros, ou seja, uma lista de transações que são compartilhadas por várias máquinas não estando localizado apenas em um servidor central.

Ao invés de uma arquitetura cliente-servidor em uma aplicação blockchain o acesso aos registros é compartilhado por todos os nodos e a verificação é feita por todos, podendo se dizer que é descentralizado.

Bloco:
Blocos armazenam dados como documentos, transações ou ocorrências.
Cada bloco possui um código hash que funciona como seu identificador, além de poder ser utilizado para verificar se os dados foram alterados.
Estão interligados por meio de criptografia, onde o bloco b armazena um código hash do bloco  b - 1, assim, formando uma lista conhecida como blockchain.

Estrutura dos blocos:
Index - representa a posição do bloco na lista.
Previous - o hash do bloco anterior ao atual.
Current - o código hash do bloco atual
Timestamp - a data e hora de criação do bloco.
Data - a transação que o bloco armazenará.
Nonce - um número único aleatório para evitar que respostas sejam anexadas ao blockchain. 

Características: 
A lista de transações é mantida por uma rede de clientes.
A concisão do blockchain é garantida por meio de Algoritmos, sendo um dos mais conhecidos o  Proof-of-Work.
Blocos novos são adicionados ao final da lista, recebendo o código hash do bloco que anteriormente era o último da lista, assim mantendo uma ligação entre os blocos
O bloco inicial não possui no hash do bloco anterior um valor zero representando que não há nenhum bloco antes dele. Ele é conhecido como genesis.

Nesta aplicação foi utilizado estes conceitos base para o desenvolvimento deste.
