#!C:\Users\USER\AppData\Local\Programs\Python\Python312\python.exe
print("content-type:text/html\r\n\r\n")
import cgi
import pymysql
connection = pymysql.connect(host="localhost", user="root", password="", database="project")
cur = connection.cursor()
f=cgi.FieldStorage()
id=f.getvalue("id")
cur.execute("""select * from users where sno='%s' """%(id))
f=cur.fetchall()
# print(f)
for i in f:
    b="files/" +i[4]
    c=i[1]
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
            margin-left:-20px;
        }
        #id1:hover {
          background-color: #ffffb3;  
        }
        #id2:hover {
          background-color: #b3ffb3;    
        }
        #id3:hover {
          background-color:	 #80ffff;
        }
        #id4:hover {
          background-color: #ffb3ff;
        }
        
        a:focus{
            color:red;
        }
        .box{
             margin-left:530px;       
        }    
        .w3-xxlarge{
                margin-top:-690px;
                position:relative;
                font-size:29px;
            }
        </style>

    </head>
    <body>
    <div class="main">
        <h2 style="color:grey;font-size:50px;text-align:center;text-transform: uppercase;">WELCOME <br><span style="color:#ff004f;">%s</span> </h2>
        <img src="%s" style="height:150px;width:150px; border:2px solid black; border-radius:100px;
        margin-left:1100px;margin-top:-170px;display:flex;flex-wrap:wrap;justify-content:space-between;" alt="image">
    </div>
    <div class="box">
    <div class="box1" id="id1"><a href="quizpage.py?id=%s" style="text-decoration:none;">&nbsp; &nbsp; Take Quiz</a></div>
    <div class="box1" id="id2"><a href="view_history.py?id=%s" style="text-decoration:none">&nbsp; &nbsp; View History</a></div>
    <div class="box1" id="id3"><a href="manage_acc.py?id=%s" style="text-decoration:none">&nbsp; &nbsp; Manage Account</a></div>
    <div class="box1" id="id4"><a href="login.py" style="text-decoration:none">&nbsp; &nbsp; Logout</a></div>
    </div>
    <p class="class"><a href="index.html" style="color:white;text-decoration:none;opacity:0.5;">
        <li class="w3-xxlarge"><i class="fa fa-home"></i></li></a></p>
        
        
    <p class="par1" style="color:white;position:absolute;margin-top:600px;margin-left:420px;font-size:15px;
    text-align:center;opacity:0.5;">By Registering,you agree to our &nbsp &nbsp &nbsp <a href="#"style="color:white;opacity:0.5;text-decoration:none;">
    Terms & Condition </a> and acknowledge you've read our &nbsp &nbsp &nbsp <a href="#" style="color:white;opacity:0.5;text-decoration:none;">
    Privacy Policy.</a> </p>
    </body>
    </html>
""" %(c,b,id,id,id))

