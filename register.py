#!C:\Users\USER\AppData\Local\Programs\Python\Python312\python.exe
print("content-type:text/html\r\n\r\n")

import pymysql

connection = pymysql.connect(host="localhost", user="root", password="", database="project")
cur = connection.cursor()

print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <link rel="icon" href="files/images.jpeg">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
        <style>
            body{
            background-image: url('files/bg1.jpg');
          background-repeat:no-repeat;
          background-size:cover;
        }
            .div1{
                width: 400px;
                height: 450px;
                margin-left: 200px;
                border-radius: 10px;
                background-color: rgba(125,55,5,0.1);
                margin-top: 140px;
                box-shadow: 5px 5px 5px #2b2626;
                background-image: url("");
            }
            h1{
                text-align: center;
                font-size: 45px;
                
                color: white;
                opacity: 0.5;
            }
            form{
                display: flex;
                flex-direction: column;    
            }
            input{
                border-radius: 5px;
                height: 30px;
                width: 280px;
                text-align: center;
                border-top: 0;
                border-left: 0;
                border-right: 0;
                border-bottom-color: gray;
                margin-left: 60px;
                opacity: 0.5;
                color: black;
            }
            input[type="checkbox"]{

                height: 10px;
                margin-left: -70px;
            }
            label{
                opacity: 0.5;
                font-size: 15px;
                margin-left: 90px;
                margin-top: -16px;
            }
            input[type="submit"]{
                background-color: darkolivegreen;
                color: whitesmoke; font-size: 20px;
            }
            input[type="submit"]:hover{
                background-color: rgb(17, 19, 14);
                color: whitesmoke;
                 font-size: 20px;
            }
            .header{
                background-color: black;
                width: 100%;
                height: 100px;
                grid-area: header;
            }
            .one{
                color:darkolivegreen;

                margin-top:-120px;
                font-size:60px;
            }
            .img1{
                margin-left:30px;
            }
            .two{
                color:darkolivegreen;
                margin-left:1265px;
                margin-top:-50px;
            }
            .footer{
                background-color: black;
                grid-area: footer;
                height: 100px;
                position: fixed;

                bottom: 0;
                width: 99%;
            }
            .w3-xxlarge{
                margin-top:-590px;
                position:relative;
            }
        </style>

    </head>
    <body>
    <div class="main">

        <div class="div1">
        <form name="form-1" method="post" enctype="multipart/form-data" >
            <h1><strong>Register Here</strong></h1><br>
            <input type="text"  name="uname"  placeholder="Enter Your Name"><br>
            <input type="email"  name="email"  placeholder="Enter Your Email"><br>
            <input type="text"  name="pass" placeholder="Enter Your password"><br>
            <input type="password"  name="cpass" placeholder="Confirm Your password"><br>
            <label>Upload Profile Photo</label><input type="file"  name="file" ><br>
            <input type="submit" value="SUBMIT" name="sub"><br>

            
            </form>
        </div>
        <p class="class"><a href="index.html" style="color:white;text-decoration:none;opacity:0.5;"><li class="w3-xxlarge"><i class="fa fa-home"></i></li></a></p>
    </div>
    <p class="par1" style="color:white;position:absolute;margin-top:520px;margin-left:150px;font-size:15px;text-align:center;opacity:0.5;">
    By Registering,you agree to our <a href="#"style="color:white;opacity:0.5;text-decoration:none;">Terms & Condition</a> 
    and acknowledge you've read our <a href="#" style="color:white;opacity:0.5;text-decoration:none;">Privacy Policy.</a> </p>   
    </body>
    </html>
""")

import cgi,os   #cgitb  #to set profile import os
#cgitb to find error
#cgitb.enable()
f=cgi.FieldStorage()
sname=f.getvalue("uname")
semail=f.getvalue("email")
spass=f.getvalue("pass")
cpass=f.getvalue("cpass")
sprofile=f['file']
ssub=f.getvalue("sub")
if ssub != None:
    if spass == cpass:
        fn=os.path.basename(sprofile.filename)
        open("files/"+fn,"wb").write(sprofile.file.read())
        q="""insert into users(name,email,password,profile)values('%s','%s','%s','%s')"""%(sname,semail,spass,fn)
        cur.execute(q)
        connection.commit()
        print("""
            <script> 
                location.href="index.html";
                alert("registered successfully!");
            </script>
        """)
    else:
        print("""
            <script> 
                
                alert("passwords not matching!");
            </script>
        """)