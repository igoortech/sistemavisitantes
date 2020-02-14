import os,time,winsound,datetime,sqlite3

def numbers(n):
    while True:
        x = input(n)
        if x.isdigit():
            return x
        else:
            print(f'\033[0;31mERRO! SOMENTE VALORES NÚMEROS SÃO PERMITIDOS!!\033[m')

def validarn(name):
    while True:
        n = input(name)
        if n.isalpha() and len(n)>=3:
            return n
        else:
            print(f'\033[0;31mERRO! SOMENTE VALORES ALFA-NÚMERICOS SÃO PERMITIDOS!!\033[m')


class visitantes:
    def __init__(self):
        self.id=""
        self.nome=""
        self.empresa=""
        self.doc=""
        self.hora=""
        self.apt=""

    def procurar(self):
        print(8 *"##" ,8 *"##")
        print(8 *"##", "PESQUISAR VISITANTE",8 *"##")
        print("DIGITE C SE QUISER CANCELAR E VOLTAR PARA O MENU")
        nome = input("Nome para Pesquisar:").strip().upper()
        if len(nome)!=0 and nome!="C":
            db = sqlite3.connect("conexao")
            cursor = db.cursor()
            cursor.execute("SELECT * FROM visitantes")
            lista = cursor.fetchall()
            for i in lista:
                if nome in i:
                    print("Esse visitante já possui cadastro!",i)
                    time.sleep(2)
                    update = input("Você desejar atualiza-lo? [S/N]").upper()
                    if update =="S": 
                        self.nome =i[1]           
                        self.empresa =i[2]
                        self.doc =i[3] 
                        hora_e_data = int(time.time())
                        self.hora = str(datetime.datetime.fromtimestamp(hora_e_data).strftime('%Y-%m-%d %H:%M:%S'))
                        self.apt = numbers("NOVO Apt:").strip()
                        cursor.execute("""INSERT INTO visitantes\
                                        (nome,empresa, doc,hora,apt)VALUES(?,?,?,?,?)""",\
                                        (self.nome, self.empresa, self.doc, self.hora,self.apt))
                        print()
                        print("Cadastro realizado com sucesso!")
                        time.sleep(1)
                        db.commit()
                        db.close
                        self.menu()
                    else:
                        print("Voltando para o  menu sem alterar nada!")
                        time.sleep(1)
                        self.menu()

                else:
                    print("Esse visitante não possui cadastro!")
                    p = input("Você deseja cadastra-lo?")
                    time.sleep(1)
                    self.cadastrar()
        elif nome =="C":
            print("Indo para a tela principal")
            self.menu()
        
        else:
            print("voltando para o menu")
            self.menu()  

                    
    def cadastrar(self):
        rodando = True
        while rodando:
            print(8 *"##" ,8 *"##")
            print(8 *"##", "CADASTRAR VISITANTE",8 *"##")
            print("DIGITE C SE QUISER CANCELAR E VOLTAR PARA O MENU")

            temp_name = input("Nome:").strip().upper()
            if len(temp_name)>=4 and temp_name!="C":
                db = sqlite3.connect("conexao")
                cursor = db.cursor()
                cursor.execute("SELECT id, nome FROM visitantes")
                lista = cursor.fetchall()
                for i in lista:
                    if temp_name in i:
                        print("Esse visitante já possui cadastro!")
                        time.sleep(3)
                        self.menu()

                self.nome = temp_name
                temp_name=""
                time.sleep(0.6)
                self.empresa = input("Empresa:").strip().upper()
                time.sleep(0.6)
                self.doc = input("Documento:").strip().upper()
                time.sleep(0.6)
                hora_e_data = int(time.time())
                self.hora = str(datetime.datetime.fromtimestamp(hora_e_data).strftime('%Y-%m-%d %H:%M:%S'))
                self.apt = input("Apt:").strip().upper()
                time.sleep(0.6)
                cursor.execute("""INSERT INTO visitantes\
                                (nome,empresa, doc,hora,apt)VALUES(?,?,?,?,?)""",\
                                (self.nome, self.empresa, self.doc, self.hora,self.apt))
                print()
                print("Cadastro realizado com sucesso!")
                time.sleep(1)
                db.commit()
                adicionar_mais = input("Você deseja continuar cadastrando ? (S/N)").upper()
                if adicionar_mais =="S":
                    continue
                else:
                    rodando = False
                    db.close()
                    print("Voltando para tela principal!")
                    time.sleep(1.5)
                    self.menu()

            elif temp_name=="C":
                print("Voltando para o menu principal")
                self.menu()
            
            elif len(temp_name)<=3:
                print("Não é permitido campos com mínimo de 3")
                self.cadastrar()
        
            else:
                print("NÃO FOI POSSÍVEL CADASTRAR, TENTE NOVAMENTE!")
                self.cadastrar()
    

    def editar(self):
        print("________________________________________________________________")
        print("------------ ATUALIZAR VISITANTES-----------")
        print("________________________________________________________________")
        print("DIGITE C SE QUISER CANCELAR E VOLTAR PARA O MENU")
        confirma = input("Você tem certeza que deseja atualizar? [S/N]").lower()
        if confirma =="s" and confirma!="c":
            id_visitante = input("Digite o id do visitante:")
            db = sqlite3.connect("conexao")
            cursor = db.cursor()
            nome_atualiza = input("Você deseja atualizar o nome? [S/N").lower()
            if nome_atualiza =="s":
                nome = input("Nome:")
                cursor.execute("UPDATE visitantes SET nome=? WHERE id=?",(nome,id_visitante))
                db.commit()
                print("Nome Atualizado com sucesso!")
                time.sleep(2)

            empresa_atualiza = input("Você deseja atualizar a empresa? [S/N").lower()
            if empresa_atualiza =="s":
                empresa = input("Empresa:")
                cursor.execute("UPDATE visitantes SET empresa=? WHERE id=?",(empresa,id_visitante))
                db.commit()
                print("Empresa Atualizada com sucesso!")
                time.sleep(2)
            
            doc_atualiza = input("Você deseja atualizar o Documento? [S/N").lower()
            if doc_atualiza =="s":
                doc = input("Documento:")
                cursor.execute("UPDATE visitantes SET doc=? WHERE id=?",(doc,id_visitante))
                db.commit()
                print("Documento Atualizado com sucesso!")
                time.sleep(2)
            
            apt_atualiza = input("Você deseja atualizar o APT:? [S/N").lower()
            if apt_atualiza =="s":
                apt = input("Apartamento:")
                cursor.execute("UPDATE visitantes SET apt=? WHERE id=?",(apt,id_visitante))
                db.commit()
                db.close()
                print("Apartament Atualizado com sucesso!")
                time.sleep(2)
                self.menu()

            else:
                print("Voltando para o menu principal")
                time.sleep(1)
                self.menu()
        else:
            print("Voltando para o menu principal")
            time.sleep(1)
            self.menu()



    def view(self):
        print("________________________________________________________________")
        print("------------ VISUALIZAR TODOS VISITANTES CADASTRADOS-----------")
        print("________________________________________________________________")
        db = sqlite3.connect("conexao")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM visitantes")
        lista = cursor.fetchall()
        for i in lista:
            print(f'{i[0]:<5}{i[1]:<24}{i[2]:<22}{i[3]:<20}{i[4]:<30}{i[5]:<6}')
        
        print()
        print("FIM DA LISTA DE CADASTRO! PRESSIONE QUALQUER TECLA PARA CONTINUAR!")
        print()
        opcao = input("[A] ATUALIZAR   [C] CADADASTRAR   [D] EXCLUIR   [M] MENU PRINCIPAL: ").upper()
        if opcao =="A":
            self.editar()
        elif opcao =="C":
            self.cadastrar()
        elif opcao =="D":
            self.deletar()
        elif opcao =="M":
            self.menu()
        else:
            print("OPÇÃO INCORRETA! TENTA UMA DA LISTA ACIMA!")
            self.menu()

        

    def deletar(self):
        rodando = True
        while rodando:
            print("DELELETAR VISISTANTES CADASTRADOS!")
            id_visitante = input("Digite o id que deseja apagar:")
            confirma = input("Você tem certeza que deseja apagar? [S/N]").lower()
            if confirma =="s":
                db = sqlite3.connect("conexao")
                cursor = db.cursor()
                cursor.execute("DELETE FROM visitantes WHERE id =?",(id_visitante,))
                db.commit()
                print("APAGADO COM SUCESSO!")
                time.sleep(0.5)
                del_more = input("Deseja apagar outro? [S/N]").upper()
                entrada = del_more[0]
                if entrada =="S":
                    continue
                else:
                    db.close()
                    rodando = False
                    print("Voltando para a tela principal!")
                    time.sleep(2)
                    self.menu()
            else:
                print("Voltando para o menu principal")
                time.sleep(0.5)
                self.menu()

    def sair(self):
        confirma = input("Você realmente deseja sair do sistema?").lower()
        if confirma =="s":
            print("Saindo do sistema!")
            time.sleep(2)
            exit()
        else:
            print("Voltando para o menu principal")
            self.menu()


    def menu(self):
        os.system("cls")
        print(8* "----" ,"MENU DE OPÇÕES:", 8* "----" )
        print()
        print(f'{"[1]Procurar:":<18}{"[2]Cadastrar":<18}{"[3]Editar":<18}{"[4] Visualizar":<18}{"[5]Apagar":<18}{"[6]Sair":<18}')
        print()
        print(8* "----" ,"Visitantes cadastrados recentementes",8* "----" ,)
        print(f'{"ID:":<5}{"Nome:":<24}{"Empresa:":<22}{"Documento":<20}{"Hora/Data:":<30}{"Apt:":<6}')
        print()
        db = sqlite3.connect("conexao")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM visitantes")
        lista = cursor.fetchall()
        lista = lista[-10:]
        lista.reverse()
        for i in lista:
            print(f'{i[0]:<5}{i[1]:<24}{i[2]:<22}{i[3]:<20}{i[4]:<30}{i[5]:<6}')


        print()
        acao = input("Digite uma ação de 1 A 6:")
        print()
        if acao =="1":
            self.procurar()

        elif acao =="2":
            self.cadastrar()
 
        elif acao =="3":
             self.editar()

        elif acao =="4":
             self.view()

        elif acao =="5":
             self.deletar()

        elif acao =="6":
             self.sair()
        
        else:
            print("OPÇÃO INVÁLIDA! DIGITE UMA AÇÃO ENTRE 1 E  6:")
            time.sleep(2)
            self.menu()

        
    def janelaprincipal(self):
        os.system("cls")
        if os.path.isfile("conexao"):
            db = sqlite3.connect("conexao")
            print("Conectado com sucesso ao banco de dados")
            winsound.Beep(2000,60)
            time.sleep(3)
            self.menu()
        
        else:
            print("Não existe arquivo de conexão!")
            time.sleep(3)
            print("Criando arquivo de conexão")
            time.sleep(3) 
            db = sqlite3.connect("conexao")
            cursor = db.cursor()
            cursor.execute("""CREATE TABLE if not exists visitantes
                            (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,nome TEXT NOT NULL,empresa TEXT NOT NULL, doc TEXT NOT NULL, hora TEXT NOT NULL, apt TEXT NOT NULL)""")
            winsound.Beep(2000,40)
            print("A conexão foi criada com sucesso!") 
            time.sleep(3)
            self.menu()          

        self.menu()

gerencimento_visitantes  = visitantes()
gerencimento_visitantes.janelaprincipal()
