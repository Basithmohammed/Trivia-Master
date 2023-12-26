#!C:\Users\USER\AppData\Local\Programs\Python\Python312\python.exe
print("content-type:text/html\r\n\r\n")
import pymysql
import cgi

connection = pymysql.connect(host="localhost", user="root", password="", database="project")
cur = connection.cursor()
f = cgi.FieldStorage()
id = f.getvalue("id")

cur.execute("""select * from users where sno='%s' """ % (id))
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
        
        .back{
                margin-top:0px;
                position:relative;
                font-size:29px;
            }
        </style>

    </head>
    <body>
    <div class="main">
    </div>
    
    <p class="back"><a href="userpage.py?id=%s" style="color:white;text-decoration:none;opacity:0.5;">
        &#x21A9</a></p>""" %(id))

print("""
    <p class="par1" style="color:white;position:absolute;margin-top:570px;margin-left:420px;font-size:15px;
    text-align:center;opacity:0.5;">By Registering,you agree to our <a href="#"style="color:white;opacity:0.5;text-decoration:none;">
    Terms & Condition</a> and acknowledge you've read our <a href="#" style="color:white;opacity:0.5;text-decoration:none;">Privacy Policy.</a> </p>
    </body>
    </html>
      """)