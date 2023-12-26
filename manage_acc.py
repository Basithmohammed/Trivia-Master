#!C:\Users\USER\AppData\Local\Programs\Python\Python312\python.exe
print("content-type:text/html\r\n\r\n")
import pymysql
import cgi
connection = pymysql.connect(host="localhost", user="root", password="", database="project")
cur = connection.cursor()
f=cgi.FieldStorage()
id=f.getvalue("id")

cur.execute("""select * from users where sno='%s' """%(id))
print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <link rel="icon" href="files/images.jpeg">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <style>
            body{
            background-image: url('files/quizbg6.jpg');
          background-repeat:no-repeat;
          background-size:cover;
          
        }

        .box1{
          margin: 50px;
          font-size:25px;
          padding: 15px;
          justify-content:center;
          align-item:center;
          display:flex;
          border:2px solid white;
          border-radius:10px;
          width:250px;
          color:grey;
        }
        a{
            color:grey;
        }
        
        #id2:hover {
          background-color: #80ff80;
        }
        #id3:hover {
          background-color: #ff4d4d;
        }
        a:focus{
            color:red;
        }
        .box{
             margin-left:530px;

        }
        .box{
            margin-top:150px;
        }
        .back{
                margin-top:-520px;
                position:relative;
                font-size:29px;
            }
        </style>

    </head>
    <body>
    <div class="main">
        <h2 style="color:grey;font-size:50px;text-align:center;text-transform: uppercase;margin-top:100px;">Manage Your Account</h2>
    </div>
    <div class="box">
    <div class="box1" id="id2"><a href="editprofile.py?id=%s" style="text-decoration:none">&nbsp; &nbsp; Edit Profile </a></div>
    <div class="box1" id="id3"><a href="delete_ac.py?id=%s" style="text-decoration:none">&nbsp; &nbsp; Delete Account </a></div>
    </div>
    <p class="back"><a href="userpage.py?id=%s" style="color:white;text-decoration:none;opacity:0.5;">
        &#x21A9</a></p>"""%(id,id,id))
    
print("""
    <p class="par1" style="color:white;position:absolute;margin-top:600px;margin-left:420px;font-size:15px;
    text-align:center;opacity:0.5;">By Registering,you agree to our <a href="#"style="color:white;opacity:0.5;text-decoration:none;">
    Terms & Condition</a> and acknowledge you've read our <a href="#" style="color:white;opacity:0.5;text-decoration:none;">Privacy Policy.</a> </p>
    </body>
    </html>
      """)