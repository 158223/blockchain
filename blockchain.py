#Desenvovimento de uma aplicação com uso de Blockchain em Python
#Aluno: Eduarda Zanini e Eduardo tobias Dornelles 


#!/usr/bin/python
# -*- coding: utf-8 -*-

from hashlib import sha256 #interface de hash seguro e de  mensagem 
#incluídos os algoritmos de hash sha256

#função de atualização do hash
def updatehash(*args):#argumentos que vamos passar na função que recebemos mais abaixo de hash
    hashing_text = ""
    h = sha256()
    for arg in args: #lista de argumentos criada
        hashing_text += str(arg)

    h.update(hashing_text.encode('utf-8'))#aqui string encode em utf8
    return h.hexdigest() #retornar os hashs


class Block():
    data = None #transação que o bloco armazenará.
    hash = None #hash impressao digital de um dado atual
    nonce = 0 # um número único aleatório para evitar que respostas sejam anexadas ao blockchain
    previous_hash = "0"*64 #o hash do bloco anterior ao atual

    def __init__(self, data, number=0):#inicialização 
        self.data = data
        self.number = number #apresenta a posição do bloco na lista

#vamos precisar definir o hash para atualizar os valores
    def hash(self):
        return updatehash(
            self.previous_hash,
            self.number,
            self.data,
            self.nonce)
        
#para imprimir os blocos
    def __str__(self):
        return str("Block#: %s\nHash: %s\nPrevious: %s\nData: %s\nNonce: %s\n" % (
            self.number, self.hash(), self.previous_hash, self.data, self.nonce))


class Blockchain():
    difficulty = 4 #dificuldade da rede, indicativo ao minerador
    #podemos anexar o nosso bloco anterior
    def __init__(self, chain=[]):
        self.chain = chain
    #funçãao para adicionar um bloco
    def add(self, block):
        self.chain.append(block)
    #função para remover um bloco
    def remove(self, block):
    	self.chain.remove(block)
    #função para minerar um bloco
    def mine(self, block):
        try:#tenta configurar o bloco anterios
            block.previous_hash = self.chain[-1].hash()
        except IndexError:#se não tem passa
            pass
#loop até que ate que a nonce produza uma hash de 4 zeros
        while True:
            if block.hash()[:self.difficulty] == "0" * self.difficulty:
                self.add(block)#se for adicionamos em bloco e sair do loop
                break
            else:
                block.nonce += 1 # caso nao for somamos o nonce para um proximo
    #verifica se o bloco previous anterior é o que esta encadeado com o atual e que nao esta corrompido
    def isValid(self):
        for i in range(1, len(self.chain)):
            _previous = self.chain[i].previous_hash
            _current = self.chain[i-1].hash()
            if _previous != _current or _current[:self.difficulty] != "0"*self.difficulty:
                    return False
        return True

def main():
    blockchain = Blockchain() #instanciando o bloco para teste
    database = ["teste1", "teste2", "teste3", "teste4"]#dados teste

    num = 0
    #percorrer o teste para minerar 
    for data in database:
        num += 1
        blockchain.mine(Block(data, num))

    for block in blockchain.chain:
        print(block) #mostra os blocos

    #vai testar as mudanças
    blockchain.chain[2].data = "NEW DATA" #se alterar os dados de data por exemplo 
    blockchain.mine(blockchain.chain[2])           
    print(blockchain.isValid())#tem que imprimir que se mudar sera falso


if __name__ == '__main__':
    main()
