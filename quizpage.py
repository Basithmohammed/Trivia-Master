#!C:\Users\USER\AppData\Local\Programs\Python\Python312\python.exe
print("content-type:text/html\r\n\r\n")

import pymysql
import cgi,os
connection = pymysql.connect(host="localhost", user="root", password="", database="project")
cur = connection.cursor()
f=cgi.FieldStorage()
id=f.getvalue("id")


print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <link rel="icon" href="files/images.jpeg">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <style>
            body{
            background-image: url('files/mainbackground.jpg');
          background-repeat:no-repeat;
          background-size:cover;
        }
        .box{
        display: grid;
        grid-template-columns: repeat(2,1fr);
        padding: 10px;
        margin-top:60px;
        }

        .box1{
          margin: 30px;
          margin-left:-225px;
          font-size:25px;
          padding: 15px;
          text-align:center;
          border:2px solid white;
          border-radius:10px;
          width:350px;
          color:grey;
            
        }
        a{
            color:grey;
            margin-left:-20px;
        }
        .box1:hover {
          background-color: lightgreen;  
          
        }
        
        a:focus{
            color:red;
        }
        .box{
             margin-left:530px;       
        }    
        .w3-xxlarge{
                margin-top:-530px;
                margin-left:-20px;
                position:relative;
                font-size:29px;
            }
        .class{
            
            margin-top:10px;
            margin-left:100px;
        }
        .back{
                margin-top:-120px;
                margin-left:-20px;
                position:relative;
                font-size:29px;
            }
        .backbtn{
            margin-left:40px;
        }
        </style>

    </head>
    <body>
   
    <div class="box">
    <div class="box1" id="id1"><a href="firstpage.py?id=%s" style="text-decoration:none;">&nbsp; &nbsp; General Knowledge</a></div>
    <div class="box1" id="id2"><a href="history_play.py?id=%s" style="text-decoration:none">&nbsp; &nbsp; History</a></div>
    <div class="box1" id="id3"><a href="technology_play.py?id=%s" style="text-decoration:none">&nbsp; &nbsp; Technology</a></div>
    <div class="box1" id="id4"><a href="science_play.py?id=%s" style="text-decoration:none">&nbsp; &nbsp; Science and Nature</a></div>
    <div class="box1" id="id5"><a href="" style="text-decoration:none">&nbsp; &nbsp; Sports</a></div>
    <div class="box1" id="id6"><a href="" style="text-decoration:none">&nbsp; &nbsp; Movies and Entertainment</a></div>
    <div class="box1" id="id7"><a href="" style="text-decoration:none">&nbsp; &nbsp; Literature</a></div>
    <div class="box1" id="id8"><a href="" style="text-decoration:none">&nbsp; &nbsp; Geography</a></div>
    </div>"""%(id,id,id,id))


print("""
    
    <p class="class"><a href="settings.py?id=%s" style="color:white;opacity:0.5;">
        <li class="w3-xxlarge"><i class="fa fa-cog"></i></li></a></p>
   
    """%(id))
print("""
    <div class="backbtn">
    <p class="back"><a href="userpage.py?id=%s" style="color:white;text-decoration:none;opacity:0.5;">&#x21A9</a></p>
    </div>"""%(id))

print("""   <p class="par1" style="color:white;position:absolute;margin-top:600px;margin-left:400px;font-size:15px;
    text-align:center;opacity:0.5;">By Registering,you agree to our &nbsp &nbsp &nbsp<a href="#"style="color:white;opacity:0.5;text-decoration:none;">
    Terms & Condition</a> and acknowledge you've read our <a href="#" style="color:white;opacity:0.5;text-decoration:none;">&nbsp &nbsp &nbsp Privacy Policy.</a> </p>
    </body>
    </html>
""" )