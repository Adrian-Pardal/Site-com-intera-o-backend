
from flask import Flask , render_template, redirect, request, flash
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SOBER'

logado = False

@app.route('/') 
def home():
    global logado
    logado = False
    
    return render_template('login.html')


@app.route('/adm')
def adm():
    if logado == True:
        return render_template("admin.html")
    
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
   
    return redirect('/adm')




















   
if __name__ in "__main__":
    app.run(debug=True)