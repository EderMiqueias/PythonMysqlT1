from db import getdb
db = getdb()
cursor = db.cursor()


class Pessoa:
    def __init__(self, nome=None, idade=None, cidade=None, id=None):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.id = id
    
    def mostrarAtributos(self):
        print(f"\nID: {self.id}\nNome: {self.nome}\nIdade: {self.idade}\nCidade: {self.cidade}")


class Cidade:
    def __init__(self, nome=None, cep=None, id=None):
        self.nome = nome
        self.cep = cep
        self.id = id
    
    def mostrarAtributos(self):
        print(f"\nID: {self.id}\nNome: {self.nome}\nCEP: {self.cep}")


class Sistema:
    def __init__(self):
        self.pessoas = list()
        self.cidades = list()

        self.selectDataC()
        self.selectDataP()

        self.methods = {
            '1':self.exibirA,
            '2':self.cadastrarP,
            '3':self.pesquisarP,
            '4':self.atualizarP,
            '5':self.cadastrarC,
            '6':self.pesquisarC,
            '7':self.atualizarC
        }

    def selectDataP(self):
        sql = "SELECT * FROM pessoas"
        cursor.execute(sql)
        
        for (id,nome,idade,id_cidade) in cursor:
            p = Pessoa(nome=nome, idade=idade, cidade=id_cidade, id=id)
            self.pessoas.append(p)

    def selectDataC(self):
        sql = "SELECT * FROM cidades"
        cursor.execute(sql)
        
        for (id,nome,cep) in cursor:
            c = Cidade(nome=nome, cep=cep, id=id)
            self.cidades.append(c)

    def exibirA(self):
        print("\n-=-=-=- Pessoas -=-=-=-")
        for p in self.pessoas:
            p.mostrarAtributos()
        
        print("\n-=-=-=- Cidades -=-=-=-")
        for c in self.cidades:
            c.mostrarAtributos()

    def cadastrarP(self):
        nome = input("Nome: ")
        idade = input("Idade: ")
        cidade = input("Cidade: ")
        
        sql = "INSERT INTO pessoas (nome, idade, id_cidade) VALUES (%s, %s, %s)"
        values = (nome, idade, cidade)
        
        cursor.execute(sql, values)
        db.commit()

        sql = "SELECT MAX(id) FROM pessoas"
        cursor.execute(sql)
        id = cursor.fetchall()[0][0]

        p = Pessoa(nome=nome, idade=idade, cidade=cidade, id=id)
        self.pessoas.append(p)

    def cadastrarC(self):
        nome = input("Nome: ")
        cep = input("CEP: ")

        sql = "INSERT INTO cidades (nome, cep) VALUES (%s, %s)"
        values = (nome, cep)

        cursor.execute(sql, values)
        db.commit()

        sql = "SELECT MAX(id) FROM cidades"
        cursor.execute(sql)
        id = cursor.fetchall()[0][0]

        c = Cidade(nome=nome, cep=cep, id=id)
        self.cidades.append(c)

    def pesquisarP(self):
        ref = input("\nID/Nome/Idade/Cidade: ")

        sql = f"SELECT * FROM pessoas WHERE id = '{ref}' OR nome = '{ref}' OR idade = '{ref}' OR id_cidade = '{ref}'"
        cursor.execute(sql)
        
        for (id, nome, idade, cidade) in cursor:
            Pessoa(id=id, nome=nome, idade=idade, cidade=cidade).mostrarAtributos()

    def pesquisarC(self):
        ref = input("\nID/Nome/CEP: ")

        sql = f"SELECT * FROM cidades WHERE id = '{ref}' OR nome = '{ref}' OR cep = '{ref}'"
        cursor.execute(sql)
        
        for (id, nome, cep) in cursor:
            Cidade(id=id, nome=nome, cep=cep).mostrarAtributos()

    def atualizarP(self):
        id = int(input("\nID: "))
        nome = input("Nome: ")
        idade = input("Idade: ")
        cidade = input("cidade: ")
        
        sql = "UPDATE pessoas SET nome = %s, idade = %s, cidade = %s WHERE id = %s"
        values = (nome, idade, cidade, id)
        
        cursor.execute(sql, values)
        db.commit()
        
        index = 0
        for p in self.pessoas:
            if p.id == id:
                self.pessoas[index] = Pessoa(nome=nome, idade=idade, cidade=cidade, id=id)
            index += 1

    def atualizarC(self):
        id = int(input("\nID: "))
        nome = input("Nome: ")
        cep = input("CEP: ")
        
        sql = "UPDATE cidades SET nome = %s, cep = %s WHERE id = %s"
        values = (nome, cep, id)
        
        cursor.execute(sql, values)
        db.commit()
        
        index = 0
        for c in self.cidades:
            if c.id == id:
                self.cidades[index] = Cidade(nome=nome, cep=cep, id=id)
            index += 1

    def menu(self):
        while True:
            print(
"""
\n\033[44;1;37m-=-=-=- Sistema Cadstro -=-=-=-\033[0m\n
1 - Exibir todos
2 - Cadastrar Pessoa
3 - Pesquisar Pessoa
4 - Atualizar Pessoa

5 - Cadastrar Cidade
6 - Pesquisar Cidade
7 - Atualizar Cidade
0 - Sair
"""
            )
            
            opc = input("--> ")
            if opc in self.methods:
                self.methods[opc]()
            else:
                break

