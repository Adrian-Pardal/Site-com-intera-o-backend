
from flask import Flask , render_template, redirect, request, flash

# o arquivo json pode ser usando para armazenar informações
import json

# a bibilioteca ast poede ser usanda para transformar string em dicionario
import ast

import os # biblioteca usada para diretorios

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SOBER'
#usamos essa configuração inicial para abrir o flask no python e criamos e backend dentro .
logado = False

@app.route('/') 
def home():
    global logado
    logado = False
    
    return render_template('login.html')


@app.route('/adm')
def adm():
    if logado == True:
        with open('users.json') as usersTemp :
            users = json.load(usersTemp)
            

        return render_template("admin.html" , users=users)
    
    if logado == False:
        return redirect('/')


@app.route('/login' , methods=['POST'])
def login():
    global logado

    name = request.form.get('name')
    password = request.form.get('password')
     
    with open('users.json') as usersTemp :
        users = json.load(usersTemp)
        cont = 0
        for user in users:
            cont += 1
            if name == 'admin' and password == '159':
                logado = True
                return redirect('/adm')
            
            if user['name'] == name and user['password'] == password:
                return render_template("username.html") 
               
            if cont >= len(users):
                flash('usuario invalido !!')
                return redirect('/')

@app.route('/registerUser' , methods=['POST'])
def registerUser():
    global logado
    user = []
    name = request.form.get('name')
    password = request.form.get('password')
    user = [
        {
            "name": name,
            "password": password
        }
    ]
   
    with open('users.json') as usersTemp :
        users = json.load(usersTemp)

    newUser =  users  + user

    with open('users.json', 'w') as recordingTemp :
        json.dump(newUser , recordingTemp , indent= 4 , sort_keys=True)
    logado = True    
    flash(f'{name} Registered')
    return redirect('/adm')

@app.route('/deleteUser' , methods=['POST'])
def deleteUser():
    global logado
    logado = True
    user = request.form.get('UserPaDelete')
    
    userDict = ast.literal_eval(user)
    # Usando a biblioteca ast transformamos string em dicionario com isso conseguimos identificar no arquibo json para remover

    name = userDict["name"]
    # Para ficar mais limpo o front end estou a variavel name para quando ast transformar em dicionario e depois so chame 
    # o nome do usuario
    
    with open('users.json') as usersTemp:
        usersJson = json.load(usersTemp) 
    # usando a formula para abrir arquivo json usamos with  para abrir usa open e chamamos o nome do arquivo que queremos.    
        for c in usersJson:
            if c == userDict:
              usersJson.remove(userDict)
              with open('users.json', 'w') as userToDeleted :
                json .dump(usersJson , userToDeleted , indent=4) # e para remover depois da ação de procurar no arquivo ai
                                                                 # voce abre para excluir porque vs code n reconhece a função 'remove'
        # Aqui usamos o for com  para procurar o 'c' dentro users.json se em  users.json tiver um usuario  igual
        # a do userDict que sera o nome e senha do usuario que voce quer remover O programa ira excluir e te retornar em 'flash'
        # o nome do usuario com a frases deleted junto ao nome  
                    
    flash(f'{name}Deleted')
    return redirect('/adm')


@app.route('/upload' , methods=['POST'])
def upload():
    global logado
    logado = True
    
    file = request.files.get('document')
    name_file = file.filename.replace(" ", "-")
    # o replace e usado para mudar a formatação das palvras que o python vai pegar como um em arquivo 
    # aonde tiver espaço vamos trocar para um hifen

    file.save(os.path.join('files',  name_file ))

    flash('Saved File')
    return redirect('/adm')















   
if __name__ in "__main__":
    app.run(debug=True)
# Essa parte fechamos o flask e tudo que estiver dentro vai ser feito pelo python.    