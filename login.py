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
        
        <style>
            body{
            background-image: url('files/bg1.jpg');
          background-repeat:no-repeat;
          background-size:cover;
        }
            .div1{
                width: 400px;
                height: 400px;
                margin-left: 200px;
                border-radius: 10px;
                background-color: rgba(125,55,5,0.1);
                margin-top: 140px;
                box-shadow: 5px 5px 5px #2b2626;
                
            }
            h1{
                text-align: center;
                font-size: 45px;
                padding-top: 30px;
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
            .w3-xxlarge{
                margin-top:-530px;
                margin-left:-20px;
                position:relative;
                font-size:29px;
            }
          
            
          
            
        </style>

    </head>
    <body>
    <div class="main">

        <div class="div1">
        <form name="form-1" method="post" action="" >
            <h1><strong>Login Here</strong></h1>
            <input type="email"  name="email"  placeholder="Enter Your Email Address"><br>
            <input type="password"  name="pass" placeholder="Enter Your password"><br>
            <input type="checkbox" id="condition1" name="condition1" value="nill">
            <label for="condition1" style="color:white;opacity: 0.5;"> Agree with <a href="#" style="color:white;opacity: 0.5;text-decoration:none;">Terms & Condition</a></label><br>
            <input type="submit" value="LOGIN" name="sub"><br>

            <p style="color:white;opacity: 0.5;font-size: 13px;margin-left:40px;">New Member? 
            <a href="register.py" style="color:white;opacity: 0.5; text-decoration:none;">Create Account</a></p>
            <p style="opacity: 0.5;font-size: 13px; margin-left: 270px; margin-top: -31px;"><a href="forgotpassword.py" 
            style="color:white;opacity: 0.5;text-decoration:none;">Forget password</a></p>

            </form>
        </div>
        <p class="class"><a href="index.html" style="color:white;text-decoration:none;opacity:0.5;">
        <li class="w3-xxlarge"><i class="fa fa-home"></i></li></a></p>

    </div>   
    <p class="par1" style="color:white;position:absolute;margin-top:520px;margin-left:150px;font-size:15px;
    text-align:center;opacity:0.5;">By Registering,you agree to our <a href="#"style="color:white;opacity:0.5;text-decoration:none;">
    Terms & Condition</a> and acknowledge you've read our <a href="#" style="color:white;opacity:0.5;text-decoration:none;">Privacy Policy.</a> </p>
    </body>
    </html>
""")

import cgi

f = cgi.FieldStorage()
pmail= f.getvalue("email")
psw = f.getvalue("pass")
psub = f.getvalue("sub")
# print(puname,ppass)
if psub != None:
    q = """select sno, email from users where email='%s' and password='%s' """ % (pmail, psw)
    cur.execute(q)
    r = cur.fetchone()
    print(r)
    if r != None:
        print("""
            <script>
                alert("Login success!!!");
                location.href="userpage.py?id=%s&mail=%s";
            </script>
        """ % (r[0],r[1]))
    else:
        print("""
            <script>
                alert("incorrect username and password!!");
            </script>
        """)