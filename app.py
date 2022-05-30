from flask import Flask, make_response, redirect, render_template ,request
import cryptocode
import sqlite3

app = Flask(__name__)

# cookielerin şifreleneceği password

enc_password = "redbull_kanatlandirir"

# admin panel user & password

admin_name = "admin"
admin_password = "miniCTF"

@app.route('/')
def hello():
    id = request.cookies.get('id')
    name = request.cookies.get('name')
    if id:
        decoded = cryptocode.decrypt(id, enc_password)
        if decoded == "soru1":
            resp = make_response(redirect('/soru1'))
            return resp
        elif decoded == "soru2":
            resp = make_response(redirect('/soru2'))
            return resp
        elif decoded == "soru3":
            resp = make_response(redirect('/soru3'))
            return resp
        elif decoded == "soru4":
            resp = make_response(redirect('/soru4'))
            return resp
        elif decoded == "soru5":
            resp = make_response(redirect('/soru5'))
            return resp
        elif decoded == "finished":
            #resp = make_response(redirect('/soru2'))
            #return resp
            #return render_template('cer.html')
            data = cryptocode.decrypt(name, enc_password)
            return render_template('cer.html', data=data)
        else:
            return render_template('index.html')
    else:
        return render_template('index.html')

@app.route('/soru1', methods=['GET', 'POST'])
def soru1():

    id = request.cookies.get('id')

    if id:
        decoded = cryptocode.decrypt(id, enc_password)
        if decoded == "soru1":
            #resp = make_response(redirect('/soru1'))
            #return resp
            return render_template('soru1.html')
        else:
            resp = make_response(redirect('/'))
            return resp
    else:
        return render_template('index.html')
    
    #return render_template('index.html')

@app.route('/soru2', methods=['GET', 'POST'])
def soru2():

    id = request.cookies.get('id')

    if id:
        decoded = cryptocode.decrypt(id, enc_password)
        if decoded == "soru2":
            #resp = make_response(redirect('/soru1'))
            #return resp
            return render_template('soru2.html')
        else:
            resp = make_response(redirect('/'))
            return resp
    else:
        return render_template('index.html')
    
    #return render_template('index.html')

@app.route('/soru3', methods=['GET', 'POST'])
def soru3():

    id = request.cookies.get('id')

    if id:
        decoded = cryptocode.decrypt(id, enc_password)
        if decoded == "soru3":
            #resp = make_response(redirect('/soru1'))
            #return resp
            return render_template('soru3.html')
        else:
            resp = make_response(redirect('/'))
            return resp
    else:
        return render_template('index.html')
    
    #return render_template('index.html')
@app.route('/soru4', methods=['GET', 'POST'])
def soru4():

    id = request.cookies.get('id')

    if id:
        decoded = cryptocode.decrypt(id, enc_password)
        if decoded == "soru4":
            #resp = make_response(redirect('/soru1'))
            #return resp
            return render_template('soru4.html')
        else:
            resp = make_response(redirect('/'))
            return resp
    else:
        return render_template('index.html')
    
@app.route('/soru5', methods=['GET', 'POST'])
def soru5():

    id = request.cookies.get('id')

    if id:
        decoded = cryptocode.decrypt(id, enc_password)
        if decoded == "soru5":
            #resp = make_response(redirect('/soru1'))
            #return resp
            return render_template('soru5.html')
        else:
            resp = make_response(redirect('/'))
            return resp
    else:
        return render_template('index.html')
       

@app.route('/control', methods=['POST'])
def control():

    id = request.cookies.get('id')
    if id:
        decoded = cryptocode.decrypt(id, enc_password)
        if decoded == "soru1":
            flag = request.form['flag']
            if flag == "flag{kaynak_ustasi}":
                flag_istrue = "true"

                encoded = cryptocode.encrypt("soru2",enc_password)

                resp = make_response(render_template('correct.html', flag=flag_istrue))

                resp.set_cookie('id', encoded)

                return resp

                #return render_template('soru1.html', flag=flag_istrue)
            else:
                flag_istrue = "false"
                return render_template('soru1.html', flag=flag_istrue)
        elif decoded == "soru2":
            flag = request.form['flag']
            if flag == "flag{masmavi}":
                flag_istrue = "true"

                encoded = cryptocode.encrypt("soru3",enc_password)

                resp = make_response(render_template('correct.html', flag=flag_istrue))

                resp.set_cookie('id', encoded)

                return resp

                #return render_template('soru1.html', flag=flag_istrue)
            else:
                flag_istrue = "false"
                return render_template('soru2.html', flag=flag_istrue)
                #return render_template('correct.html', flag=flag_istrue)
            #resp = make_response(redirect('/soru1'))
            #return resp
            #return "soru1"
        elif decoded == "soru3":
            flag = request.form['flag']
            if flag == "flag{malware_4ever}":
                flag_istrue = "true"

                encoded = cryptocode.encrypt("soru4",enc_password)

                resp = make_response(render_template('correct.html', flag=flag_istrue))

                resp.set_cookie('id', encoded)

                return resp

                #return render_template('soru1.html', flag=flag_istrue)
            else:
                flag_istrue = "false"
                return render_template('soru3.html', flag=flag_istrue)
                #return render_template('correct.html', flag=flag_istrue)
            #resp = make_response(redirect('/soru1'))
            #return resp
            #return "soru1"
        elif decoded == "soru4":
            flag = request.form['flag']
            if flag == "flag{php_everywhere}":
                flag_istrue = "true"

                encoded = cryptocode.encrypt("soru5",enc_password)

                resp = make_response(render_template('correct.html', flag=flag_istrue))

                resp.set_cookie('id', encoded)

                return resp

                #return render_template('soru1.html', flag=flag_istrue)
            else:
                flag_istrue = "false"
                return render_template('soru4.html', flag=flag_istrue)

        elif decoded == "soru5":
            
            if request.method == 'POST':

                user = request.form['user']

                password = request.form['password']

                if user == "admin" and password == "admin":
                    flag_istrue = "true"

                    encoded = cryptocode.encrypt("finished",enc_password)

                    resp = make_response(render_template('correct.html', flag=flag_istrue))

                    resp.set_cookie('id', encoded)

                    return resp
                else:
                    flag_istrue = "false"
                    return render_template('soru5.html', flag=flag_istrue)
        else:
            return redirect('/')
    else:
        return render_template('index.html')
    #return "zort"
    #return render_template('index.html')



@app.route('/register', methods=['POST']) 
def register():

   name = request.form['name']

   email = request.form['email']

   if name == "" or email == "":
       return make_response(redirect('/'))

   conn = sqlite3.connect('database.db')

   with sqlite3.connect("database.db") as con:
    cur = con.cursor()
    cur.execute("INSERT INTO login (name,email) VALUES (?,?)",(name,email) )
    con.commit()

   #result = hashlib.md5(name.encode())

   result = cryptocode.encrypt(name,enc_password)

   encoded = cryptocode.encrypt("soru1",enc_password)

   resp = make_response(redirect('/'))
   #resp.set_cookie('name', str(result.hexdigest()))
   resp.set_cookie('name', result)
   resp.set_cookie('id', encoded)

   return resp

    #return name + "" + email
    #return jsonify(data)

@app.route('/login', methods=['GET', 'POST']) 
def login():

    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']

        if user == admin_name and password == admin_password:
            result = cryptocode.encrypt("miniCTF",enc_password)
            resp = make_response(redirect('/show'))
            resp.set_cookie('secret', result)
            return resp
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')

@app.errorhandler(404)
def e404(e):
    return redirect('/')

@app.errorhandler(405)
def e405(e):
    return redirect('/')   

@app.route('/show')
def deneme():

    secret = request.cookies.get('secret')
    if secret:
        con = sqlite3.connect("database.db")
        con.row_factory = sqlite3.Row
   
        cur = con.cursor()
        cur.execute("select * from login")
   
        a = ""

        rows = cur.fetchall()


        list_accumulator = []
        for item in rows:
            list_accumulator.append({k: item[k] for k in item.keys()})

        return render_template("rows.html", list_accumulator=list_accumulator)
    else:
        return redirect('/')


def dict_from_row(row):
    return dict(zip(row.keys(), row))         
   
@app.route('/clearcookie', methods=['GET', 'POST'])
def clearcookie():

   resp = make_response(redirect('/'))
   resp.delete_cookie('id')
   resp.delete_cookie('name')
   return resp

@app.route('/flag.php')
def flag():

    id = request.cookies.get('id')
    if id:
        return render_template('soru4_flag.html')
    else:
        return redirect("/")
