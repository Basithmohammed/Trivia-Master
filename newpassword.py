#!C:\Users\USER\AppData\Local\Programs\Python\Python312\python.exe
print("content-type:text/html\r\n\r\n")

import pymysql

connection = pymysql.connect(host="localhost", user="root", password="", database="project")
cur = connection.cursor()
import cgi

f = cgi.FieldStorage()
id = f.getvalue("id")
print("""
<!doctype html>
<html>
<head>
    <link rel="icon" href="files/images.jpeg">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <style>
    body{
        background-image: url('files/mainbackground.jpg');
          background-repeat:no-repeat;
          background-size:cover;
    }
    div{
        width: 400px;
        height: 150px;
        margin-left: 540px;
        border-radius: 10px;
        background-color: rgba(125,55,5,0.1);
        margin-top: 270px;
        box-shadow: 5px 5px 5px #2b2626;
        background-image: url("");
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
        margin-top:30px;
        opacity: 0.5;
        color: black;
    }
   put[type="submit"]{
        background-color: darkolivegreen;
        color: whitesmoke; font-size: 20px;
    }
    input[type="submit"]:hover{
        background-color: rgb(17, 19, 14);
        color: whitesmoke;
        font-size: 20px;
    }
     .w3-xxlarge{
                margin-top:-430px;
                position:relative;
                margin-left:-20px;
            }
</style>
</head>

  <body>
  <div>
     <form method="post">

            <input type="password" name="pass" placeholder="Enter New Password">
            <input type="submit" value="UPDATE" name="sub">

        </form>
  </div>
   <p class="class"><a href="otpvalidation.py" style="color:white;text-decoration:none;opacity:0.5;">
        <li class="w3-xxlarge"><i class="fa fa-arrow-left"></i></li></a></p>
  <p class="par1" style="color:white;position:absolute;margin-top:600px;margin-left:400px;font-size:15px;text-align:center;opacity:0.5;">
    By Registering,you agree to our <a href="#"style="color:white;opacity:0.5;text-decoration:none;">Terms & Condition</a> 
    and acknowledge you've read our <a href="#" style="color:white;opacity:0.5;text-decoration:none;">Privacy Policy.</a> </p>  
</body>
</html>
""")

password = f.getvalue("pass")
psub = f.getvalue("sub")
if psub != None:
    q = """update users set password='%s' where sno='%s'""" % (password, id)
    cur.execute(q)
    connection.commit()
    print("""
        <script>
                location.href="login.py";
                alert("Password Reset Successfully!!!!!");
            </script>
    """)