from flask import Flask, render_template, request, redirect, url_for, session, send_file
import mysql.connector

import os

app = Flask(__name__)
app.secret_key = 'a'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ServerLogin')
def ServerLogin():
    return render_template('ServerLogin.html')


@app.route('/OwnerLogin')
def OwnerLogin():
    return render_template('OwnerLogin.html')


@app.route('/UserLogin')
def UserLogin():
    return render_template('UserLogin.html')


@app.route('/NewOwner')
def NewOwner():
    return render_template('NewOwner.html')


@app.route('/NewUser')
def NewUser():
    return render_template('NewUser.html')


@app.route("/FileInfo")
def FileInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM filetb")
    data = cur.fetchall()
    return render_template('FileInfo.html', data=data)


@app.route("/serverlogin", methods=['GET', 'POST'])
def adminlogin():
    error = None
    if request.method == 'POST':
        if request.form['uname'] == 'server' and request.form['password'] == 'server':
            status = ''
            import datetime
            date = datetime.datetime.now().strftime('%Y-%m-%d')

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
            cur = conn.cursor()
            cur.execute("SELECT * FROM ownertb where status='waiting'")
            data = cur.fetchall()

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
            cur = conn.cursor()
            cur.execute("SELECT * FROM ownertb where status='Active'")
            data1 = cur.fetchall()

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
            cursor = conn.cursor()
            cursor.execute("select * from filetb ")
            data2 = cursor.fetchall()
            for x1 in data2:
                fid = x1[0]
                oname = x1[1]
                Fname = x1[3]
                mdate = x1[5]

                path = "static/upload/" + Fname

                if os.path.isfile(path):
                    status = "File Found"
                    file_datetime = get_file_datetime(path)

                    string_without_quotes = remove_special_characters(str(file_datetime))
                    print(string_without_quotes)

                    if mdate == string_without_quotes:
                        status = "File Found"
                    else:
                        status = "File Found Modified"

                else:
                    status = "File Not Found"

                conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT * from auditb where FileId='" + str(fid) + "' and date='" + date + "' ")
                data4 = cursor.fetchone()
                if data4 is None:
                    conn = mysql.connector.connect(user='root', password='', host='localhost',
                                                   database='1cloudAuditdbpy')
                    cursor = conn.cursor()
                    cursor.execute(
                        "INSERT INTO auditb VALUES ('','" + str(
                            fid) + "','" + oname + "','" + Fname + "','" + status + "','" + str(date) + "')")
                    conn.commit()
                    conn.close()

                print(status)

            return render_template('ServerHome.html', data=data, data1=data1)

        else:
            alert = 'Username or Password is wrong'
            return render_template('goback.html', data=alert)


@app.route("/ServerHome")
def ServerHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM ownertb where status='waiting'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM ownertb where status='Active'")
    data1 = cur.fetchall()
    return render_template('ServerHome.html', data=data, data1=data1)


@app.route("/UserApproved")
def UserApproved():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where status='waiting'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where status='Active'")
    data1 = cur.fetchall()
    return render_template('UserApproved.html', data=data, data1=data1)


@app.route("/Approved")
def Approved():
    id = request.args.get('lid')
    email = request.args.get('email')

    import random
    loginkey = random.randint(1111, 9999)
    message = "Owner Login Key :" + str(loginkey)

    sendmsg(email, message)

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
    cursor = conn.cursor()
    cursor.execute("Update ownertb set Status='Active',LoginKey='" + str(loginkey) + "' where id='" + id + "' ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM ownertb where status='waiting'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM ownertb where status='Active'")
    data1 = cur.fetchall()

    return render_template('ServerHome.html', data=data, data1=data1)


@app.route("/Approved1")
def Approved1():
    id = request.args.get('lid')
    email = request.args.get('email')

    import random
    loginkey = random.randint(1111, 9999)
    message = "User Login Key :" + str(loginkey)

    sendmsg(email, message)
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
    cursor = conn.cursor()
    cursor.execute("Update regtb set Status='Active',LoginKey='" + str(loginkey) + "' where id='" + id + "' ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where status='waiting'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where status='Active'")
    data1 = cur.fetchall()

    return render_template('UserApproved.html', data=data, data1=data1)


@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    if request.method == 'POST':
        uname = request.form['uname']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        username = request.form['username']
        password = request.form['password']
        gname = request.form['password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO regtb VALUES ('','" + uname + "','" + mobile + "','" + email + "','" + address + "','" + username + "','" + password + "','waiting','')")
        conn.commit()
        conn.close()

        alert = 'Record Saved!'
        return render_template('goback.html', data=alert)


@app.route("/newowner", methods=['GET', 'POST'])
def newowner():
    if request.method == 'POST':
        uname = request.form['uname']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        username = request.form['username']
        password = request.form['password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO ownertb VALUES ('','" + uname + "','" + mobile + "','" + email + "','" + address + "','" + username + "','" + password + "','waiting','')")
        conn.commit()
        conn.close()

        alert = 'Record Saved!'
        return render_template('goback.html', data=alert)


@app.route("/ownerlogin", methods=['GET', 'POST'])
def ownerlogin():
    if request.method == 'POST':

        username = request.form['uname']
        password = request.form['password']
        loginkey = request.form['loginkey']
        session['oname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
        cursor = conn.cursor()
        cursor.execute("SELECT * from ownertb where username='" + username + "' and Password='" + password + "' ")
        data = cursor.fetchone()
        if data is None:

            alert = 'Username or Password is wrong'
            return render_template('goback.html', data=alert)

        else:

            Status = data[7]
            lkey = data[8]

            if Status == "waiting":

                alert = 'Waiting For Server Approved!'
                return render_template('goback.html', data=alert)

            else:

                if lkey == loginkey:

                    conn = mysql.connector.connect(user='root', password='', host='localhost',
                                                   database='1cloudAuditdbpy')
                    cur = conn.cursor()
                    cur.execute("SELECT * FROM ownertb where username='" + session['oname'] + "'")
                    data1 = cur.fetchall()
                    return render_template('OwnerHome.html', data=data1)
                else:
                    alert = 'Login Key Incorrect'
                    return render_template('goback.html', data=alert)


@app.route('/OwnerHome')
def OwnerHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM ownertb where username='" + session['oname'] + "'")
    data1 = cur.fetchall()
    return render_template('OwnerHome.html', data=data1)


import os.path
import time


def get_file_datetime(file_path):
    # Get the creation time
    creation_time = os.path.getctime(file_path)

    # Get the modification time
    modification_time = os.path.getmtime(file_path)

    # Get the access time
    access_time = os.path.getatime(file_path)

    # Convert timestamps to readable date and time
    creation_time_str = time.ctime(creation_time)
    modification_time_str = time.ctime(modification_time)
    access_time_str = time.ctime(access_time)

    return {

        modification_time_str

    }


@app.route('/OwnerFileUpload')
def OwnerFileUpload():
    return render_template('OwnerFileUpload.html', oname=session['oname'])


import pyAesCrypt
import random
import string
import base64, os


def encrypt(key, source, des):
    output = des
    pyAesCrypt.encryptFile(source, output, key)
    return output


def decrypt(key, source, des):
    dfile = source.split(".")
    output = des

    pyAesCrypt.decryptFile(source, output, key)
    return output


import re


def remove_special_characters(input_string):
    # Define the special characters you want to remove
    special_characters = ["'", "{", "}"]

    # Construct the regex pattern to match any of the special characters
    pattern = '|'.join(map(re.escape, special_characters))

    # Remove the special characters using the sub() function
    output_string = re.sub(pattern, '', input_string)

    return output_string


import hmac
import hashlib
import binascii


def create_sha256_signature(key, message):
    byte_key = binascii.unhexlify(key)
    message = message.encode()
    return hmac.new(byte_key, message, hashlib.sha256).hexdigest().upper()


@app.route("/owfileupload", methods=['GET', 'POST'])
def owfileupload():
    if request.method == 'POST':
        oname = session['oname']
        info = request.form['info']
        file = request.files['file']

        import random
        fnew = random.randint(111, 999)
        savename = str(fnew) + file.filename

        file.save("static/upload/" + savename)

        filepath = "./static/upload/" + savename
        head, tail = os.path.split(filepath)
        file_size_bytes = os.path.getsize(filepath)
        # Convert bytes to kilobytes
        file_size_kb = file_size_bytes / 1024
        file_size_str = "{:.2f}".format(file_size_kb)

        file_datetime = get_file_datetime(filepath)

        string_without_quotes = remove_special_characters(str(file_datetime))
        print(string_without_quotes)

        newfilepath1 = './static/upload/' + str(tail)
        newfilepath2 = './static/Encrypt/' + str(tail)

        from ecies.utils import generate_key

        secp_k = generate_key()
        privhex = secp_k.to_hex()
        pubhex = secp_k.public_key.format(True).hex()
        key = pubhex
        encrypt(key, newfilepath1, newfilepath2)

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM filetb ")
        data = cursor.fetchone()

        if data:

            conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
            cursor1 = conn1.cursor()
            cursor1.execute("select max(id) from filetb")
            da = cursor1.fetchone()
            if da:
                d = da[0]
                print(d)

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
            cursor = conn.cursor()
            cursor.execute("SELECT  *  FROM filetb where  id ='" + str(d) + "'   ")
            data = cursor.fetchone()
            if data:
                hash1 = data[7]
                num1 = random.randrange(1111, 9999)
                hash2 = create_sha256_signature("E49756B4C8FAB4E48222A3E7F3B97CC3", str(num1))

                conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO filetb VALUES ('','" + oname + "','" + str(
                        info) + "','" + savename + "','" + pubhex + "','" + str(
                        string_without_quotes) + "','" + hash1 + "','" + hash2 + "')")
                conn.commit()
                conn.close()

                conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO   fileintb VALUES ('','" + savename + "','" + str(file_size_str) + "','" + str(
                        string_without_quotes) + "','" + hash1 + "','" + hash2 + "')")
                conn.commit()
                conn.close()
        else:

            hash1 = '0'
            num1 = random.randrange(1111, 9999)
            hash2 = create_sha256_signature("E49756B4C8FAB4E48222A3E7F3B97CC3", str(num1))

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO filetb VALUES ('','" + oname + "','" + info + "','" + savename + "','" + pubhex + "','" + str(
                    string_without_quotes) + "','" + hash1 + "','" + hash2 + "')")
            conn.commit()
            conn.close()

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO   fileintb VALUES ('','" + savename + "','" + str(file_size_str) + "','" + str(
                    string_without_quotes) + "','" + hash1 + "','" + hash2 + "')")
            conn.commit()
            conn.close()

        return render_template('OwnerFileUpload.html', pkey=pubhex, oname=oname)


@app.route('/OwnerFileInfo')
def OwnerFileInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM filetb where OwnerName='" + session['oname'] + "'")
    data1 = cur.fetchall()
    return render_template('OwnerFileInfo.html', data=data1)


@app.route('/AuditInfo')
def AuditInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM auditb where OwnerName='" + session['oname'] + "'")
    data1 = cur.fetchall()
    return render_template('AuditInfo.html', data=data1)



@app.route('/AAuditInfo')
def AAuditInfo():
    import datetime
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM auditb where  date='"+ date +"'")
    data1 = cur.fetchall()
    return render_template('AAuditInfo.html', data=data1)

@app.route('/keywordInfo')
def keywordInfo():
    import datetime
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM filekeytb where OwnerName='" + session['oname'] + "' and date='"+ date +"'")
    data1 = cur.fetchall()
    return render_template('OkeywordInfo.html', data=data1)


@app.route("/ODownload")
def ODownload():
    fid = request.args.get('fid')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM  filetb where  id='" + fid + "'")
    data = cursor.fetchone()
    if data:
        prkey = data[4]
        fname = data[3]

    else:
        return 'Incorrect username / password !'

    privhex = prkey

    filepath = "./static/Encrypt/" + fname
    head, tail = os.path.split(filepath)

    newfilepath1 = './static/Encrypt/' + str(tail)
    newfilepath2 = './static/Decrypt/' + str(tail)

    decrypt(privhex, newfilepath1, newfilepath2)

    return send_file(newfilepath2, as_attachment=True)


@app.route("/OwnerFileApproved")
def OwnerFileApproved():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM userfiletb where status='waiting' and OwnerName='" + session['oname'] + "' ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM userfiletb where status='Approved' and OwnerName='" + session['oname'] + "' ")
    data1 = cur.fetchall()
    return render_template('OwnerFileApproved.html', data=data, data1=data1)


@app.route("/OApproved")
def OApproved():
    rid = request.args.get('rid')
    fid = request.args.get('fid')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM  userfiletb where  id='" + rid + "'")
    data = cursor.fetchone()
    if data:
        prkey = data[4]
        UserName = data[5]
    else:
        return 'Incorrect username / password !'

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM  regtb where  UserName='" + UserName + "'")
    data1 = cursor.fetchone()
    if data1:
        session["email"] = data1[3]
    else:
        return 'Incorrect username / password !'

    mailmsg = "Request Id" + rid + "\n Decryptkey: " + prkey

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
    cursor = conn.cursor()
    cursor.execute("update userfiletb set Status='Approved'  where id='" +
                   rid + "'")
    conn.commit()
    conn.close()

    sendmsg(session["email"], mailmsg)

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM userfiletb where status='waiting' and OwnerName='" + session['oname'] + "' ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM userfiletb where status='Approved' and OwnerName='" + session['oname'] + "' ")
    data1 = cur.fetchall()
    return render_template('OwnerFileApproved.html', data=data, data1=data1)


@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    if request.method == 'POST':

        username = request.form['uname']
        password = request.form['password']
        loginkey = request.form['loginkey']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "' and Password='" + password + "' ")
        data = cursor.fetchone()
        if data is None:

            alert = 'Username or Password is wrong'
            return render_template('goback.html', data=alert)

        else:

            Status = data[7]
            lkey = data[8]

            if Status == "waiting":

                alert = 'Waiting For Server Approved!'
                return render_template('goback.html', data=alert)

            else:

                if lkey == loginkey:

                    conn = mysql.connector.connect(user='root', password='', host='localhost',
                                                   database='1cloudAuditdbpy')
                    cur = conn.cursor()
                    cur.execute("SELECT * FROM regtb where username='" + session['uname'] + "'")
                    data1 = cur.fetchall()
                    return render_template('UserHome.html', data=data1)
                else:
                    alert = 'Login Key Incorrect'
                    return render_template('goback.html', data=alert)


@app.route('/UserHome')
def UserHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM UserHome where OwnerName='" + session['uname'] + "'")
    data1 = cur.fetchall()
    return render_template('UserHome.html', data=data1)


@app.route('/USearch')
def USearch():
    '''conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM filetb ")
    data1 = cur.fetchall()'''
    # return render_template('USearch.html', data=data1)
    return render_template('USearch.html')


@app.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        sear = request.form['sear']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM  filetb where FileInfo like'%" + sear + "%'  ")
        data1 = cur.fetchall()
        return render_template('USearch.html', data=data1)


@app.route("/SendKeyRequest")
def SendKeyRequest():
    fid = request.args.get('fid')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM   filetb where  id='" + fid + "'")
    data = cursor.fetchone()
    if data:

        oname = data[1]
        fname = data[3]
        prkey = data[4]


    else:
        return 'Incorrect username / password !'

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO userfiletb VALUES ('','" + fid + "','" + oname + "','" + fname + "','" + prkey + "','" + session[
            'uname'] + "','waiting')")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM userfiletb where status='waiting' and username='" + session['uname'] + "' ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM userfiletb where status='Approved' and username='" + session['uname'] + "' ")
    data1 = cur.fetchall()
    return render_template('UDownload.html', data=data, data1=data1)


@app.route("/UDownload")
def UDownload():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM userfiletb where status='waiting' and username='" + session['uname'] + "' ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM userfiletb where status='Approved' and username='" + session['uname'] + "' ")
    data1 = cur.fetchall()
    return render_template('UDownload.html', data=data, data1=data1)


@app.route("/userdownload")
def userdownload():
    ufid = request.args.get('ufid')

    session["ufid"] = ufid

    return render_template('userdownload.html')


@app.route("/uddd", methods=['GET', 'POST'])
def uddd():
    if request.method == 'POST':
        sear = request.form['sear']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1cloudAuditdbpy')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM  userfiletb where  id='" + session["ufid"] + "'")
        data = cursor.fetchone()
        if data:
            prkey = data[4]
            fname = data[3]


        else:
            return 'Incorrect username / password !'

        if sear == prkey:

            filepath = "./static/Encrypt/" + fname
            head, tail = os.path.split(filepath)

            newfilepath1 = './static/Encrypt/' + str(tail)
            newfilepath2 = './static/Decrypt/' + str(tail)

            decrypt(prkey, newfilepath1, newfilepath2)

            return send_file(newfilepath2, as_attachment=True)
        else:
            return 'key Inorrect..!'


def sendmsg(Mailid, message):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    fromaddr = "projectmailm@gmail.com"
    toaddr = Mailid

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Alert"

    # string to store the body of the mail
    body = message

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "qmgn xecl bkqv musr")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()


if __name__ == '__main__':
    # app.run(host='0.0.0.0',debug = True, port = 5000)
    app.run(debug=True, use_reloader=True)
