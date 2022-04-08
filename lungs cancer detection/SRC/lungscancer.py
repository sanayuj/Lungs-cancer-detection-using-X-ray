from flask import *

from SRC.database import *

app=Flask(__name__)
@app.route('/')
def main():
    return render_template("login.html")

@app.route('/homepage',methods=["GET","POST"])
def homepage():
    return render_template('homepage.html')

@app.route('/addtip',methods=["GET","POST"])
def addtip():
    return render_template('add tips.html')

@app.route('/manage_tips',methods=["GET","POST"])
def manage_tips():
    qry="select * from tips"
    res=selectall(qry)
    return  render_template('manage tips.html',val=res)


@app.route('/reg',methods=["GET","POST"])
def reg():
    return  render_template('Register.html')


@app.route('/view',methods=["GET","POST"])
def view():
    return render_template('view user.html')

@app.route('/add_tips.',methods=["GET","POST"])
def add_tips():
    return render_template('add_tips.html')


@app.route('/feed',methods=["GET","POST"])
def feed():
    qry="SELECT `user`.`fname`,`lastname`,`id`.* FROM `user` JOIN `id` ON`id`.`user_id`=`user`.`login_id` "
    res=selectall(qry)

    return render_template('feedback.html',val=res)



@app.route('/logincode',methods=['POST'])
def logincode():
    uname=request.form['textfield']
    password=request.form['textfield2']
    qry="select * from login where username =%s and password=%s"
    val=(uname,password)
    res=select(qry,val)


    if res is None:
        return '''<script>alert("invalid username or password ");
        window.location="/"</script>'''
    elif res[3]=='admin':
        return'''<script>alert("Login sucess");
        window.location="/homepage"</script>'''
    else:
        return '''<script>alert("invalid username or password ");
                window.location="/"</script>'''
@app.route('/addtipcode',methods=['POST'])
def addtipcode():
    tip=request.form['textfield']
    des=request.form['textfield2']
    qry="insert into tips values(NULL,%s,%s,curdate())"
    val = (tip, des)
    iud(qry, val)
    return '''<script>alert("Tips added ");
                   window.location="/manage_tips"</script>'''

@app.route('/delete')
def delete():
    id=request.args.get('id')

    qry="delete from tips where id=%s"
    iud(qry,id)
    return '''<script>alert("Tips deleted ");
                      window.location="/manage_tips"</script>'''

app.run(debug=True)