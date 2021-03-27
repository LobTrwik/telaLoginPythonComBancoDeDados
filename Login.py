from PyQt5 import uic,QtWidgets
import sqlite3


def chama_paginaFinal():
    PaginaDeLogin.label_7.setText("")
    email = PaginaDeLogin.lineEdit_2.text()
    senha = PaginaDeLogin.lineEdit_3.text()
    banco = sqlite3.connect('LoginCadastro.db')
    cursor = banco.cursor()
    try:
        cursor.execute(f'SELECT senha FROM Cadastro WHERE login ="{email}"')
        senhaBancoDados = cursor.fetchall()
        print(email)
        print(senhaBancoDados[0][0])
        banco.close()

    except:
        print('Email ou Senha Incorreto. Tente novamente...')


    if senha == senhaBancoDados[0][0] :
        PaginaFinal.show()
        PaginaDeLogin.close()

    else:
        print('Email ou Senha Incorreto. Tente novamente...')



def logout():
    PaginaDeLogin.close()
    PaginaFinal.show()



def abre_PaginaDeCadastro():
    PaginaDeCadastro.show()

def cadastrar():
    nome = PaginaDeCadastro.lineEdit.text()
    email = PaginaDeCadastro.lineEdit_2.text()
    senha = PaginaDeCadastro.lineEdit_3.text()
    confirmar = PaginaDeCadastro.lineEdit_4.text()

    print(f'Nome: {nome}')
    print(f'Email: {email}')
    print(f'Senha: {senha}')


    sexo = ""
    if PaginaDeCadastro.radioButton.isChecked():
        print(f'{nome} é do sexo MASCULINO.')
        sexo = "Masculino"
    elif PaginaDeCadastro.radioButton_2.isChecked():
        print(f'{nome} é do sexo FEMININO.')
        sexo = "Feminino"
    else:
        print(f'{nome} é do sexo OUTROS.')
        sexo = "Outros"


    if (senha == confirmar):
        try:
            banco = sqlite3.connect('LoginCadastro.db')
            cursor = banco.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS cadastro (nome[str],login[str],senha[str],sexo[str])')
            cursor.execute("INSERT INTO cadastro VALUES ('"+nome+"','"+email+"','"+senha+"','"+sexo+"')")

            banco.commit()
            banco.close()
            PaginaDeCadastro.label.setText("Usuario cadastrado com sucesso")

        except sqlite3.Error as erro:
            print(f'Erro ao inserir os dados: {erro} ')
    else:
        PaginaDeCadastro.label.setText("As senhas digitadas estão diferentes")



app=QtWidgets.QApplication([])
PaginaDeLogin=uic.loadUi("PaginaDeLogin.ui")
PaginaFinal=uic.loadUi("PaginaFinal.ui")
PaginaDeCadastro=uic.loadUi("PaginaDeCadastro.ui")
PaginaDeLogin.pushButton.clicked.connect(chama_paginaFinal)
PaginaDeLogin.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
PaginaDeLogin.pushButton_2.clicked.connect(abre_PaginaDeCadastro)
PaginaDeCadastro.pushButton.clicked.connect(cadastrar)


PaginaDeLogin.show()
app.exec()
