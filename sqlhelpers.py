from app import mysql, session
#Simplifica o acesso ao banco de dados 'crypto'
class Table:
        def __init__(self, table_name, *args):
                    self.table - table_name
                    self.columns = "(%s)" %",".join(args)
                    self.columnsList = args
                    # se a tabela ainda não existir, cria.
                    if isnewtable(table_name):
                        create_data = ""
                        for column in self.columnsList:
                            create_data += "%s varchar(100)," %column

                        cur = mysql.connection.cursor() #create the table
                        cur.execute("CREATE TABLE %s(%s)" %(self.table, create_data[:len(create_data)-1]))
                        cur.close()
                    
        #obter todos os valores da tabela        
        def getall(self):
            cur = mysql.connection.cursor()
            result = cur.execute("SELECT * FROM %s" %self.table)
            data = cur.fetchall(); return data
            
        #obter um valor da tabela com base nos dados de uma coluna    
        def getone(self,search,value):
            data = {}; cur = mysql.connection.cursor()
            result = cur.execute("SELECT * FROM %s WHERE %s = \"%s\"" %(self.table, search, value))
            if result > 0: data = cur.fetchone()
            cur.close(); return data
            
         #excluir um valor da tabela com base nos dados da coluna   
        def deleteone(self,search,value):
            cur = mysql.connection.cursor()
            cur.execute("DELETE from %s where %s = \"%s\"" %(self.table, search, value))
            mysql.connection.commit(); cur.close()

        
        #exclui todos os valores da tabela
        def deleteall(self):
            self.drop() #remove table and recreate
            self.__init__(self.table, *self.columnsList)
            
        #remove tabela do mysql
        def drop(self):
             cur = mysql.connection.cursor()
             cur.execute("DROP TABLE %s" %self.table)
             cur.close()
             
         #insere valores na tabela
        def insert(self, *args):
            data = ""
            for arg in args:#converte dados no formato de string mysql
                 data += "\"%s\"," %(arg)
            
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO %s%s VALUES(%s)" %(self.table, self.columns, data[:len(data)-1]))
            mysql.connection.commit()
            cur.close()
            
    #executa o código mysql em python        
def sql_raw(execute):
        cur = mysql.connection.cursor()
        cur.execute(execution)
        mysql.connection.commit()
        cur.close()
        
    #verifique se a tabela já existe    
def isnewtable(tableName):
        cur.mysql.connection.cursor()
            
        try:#tentativa para obter dados da tabela
            result = cur.execute(" select * from %s" %stableName)
            cur.close()
        except:
            return True
        else: 
            return False
        
#verifica se o usuário já existe        
def isnewuser(username):
               
        users = Table("users", "name", "email", "username", "password")
        data = users.getall()
        usernames = [user.get('username') for user in data]

        return False if username in usernames else True
    