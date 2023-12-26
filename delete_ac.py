#!C:\Users\USER\AppData\Local\Programs\Python\Python312\python.exe
print("content-type:text/html\r\n\r\n")
import cgi,os
import pymysql
connection = pymysql.connect(host="localhost", user="root", password="", database="project")
cur = connection.cursor()
f=cgi.FieldStorage()
id=f.getvalue("id")
# print(id)
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Delete Account</title>
    <link rel="icon" href="files/images.jpeg">
    <style>
        body{
            background-image: url('files/quizbg6.jpg');
          background-repeat:no-repeat;
          background-size:cover;
          color:black;
        }
        .main{
                width: 400px;
                height: 360px;
                margin-left:500px;
                display:flex;
                align-item:center;
                border-radius: 10px;
                background-color: #2929a3;
                margin-top: 140px;
                box-shadow: 5px 5px 5px #2b2626;
                
            }
            input[type="submit"]{
                border-radius:10px;
                color: black; font-size: 17px;
                background-color: #c2c2f0;
                width:150px;
            }
            #yes:hover{
                background-color: #ff4d4d;
            }
             #no:hover{
                background-color: lightgreen;
            }
            h1{
            margin-left:-120px;
            }
            
            
    </style>
</head>

<body>
<div class="main">
    <span style='font-size:100px; margin-top:140px;margin-left:30px;'>&#128560</span>
    <h1 style='font-size:38px;'>Delete Your Account !!</h1>
    
    <form action="#" method="post">
        <p style='margin-top:140px; margin-left:-30px;color:grey;'>Are you sure you want to delete your account?<br><br>   
        <input type="submit" id="yes" name="yes" value="Remove Account"><br><br>
        <input type="submit" id="no" name="no" value="Keep Account"></p>
        
    </form>
    <p class="par1" style="color:white;position:absolute;margin-top:540px;margin-left:-100px;font-size:15px;
    text-align:center;opacity:0.5;">By Registering,you agree to our <a href="#"style="color:white;opacity:0.5;text-decoration:none;">
    Terms & Condition</a> and acknowledge you've read our <a href="#" style="color:white;opacity:0.5;text-decoration:none;">Privacy Policy.</a> </p>
    <div>
    
</body>
</html>
""")


user_id = f.getvalue("id")
submit_yes = f.getvalue("yes")
submit_no = f.getvalue("no")
if submit_yes !=None:
    #  SQL DELETE statement
    delete_query = "DELETE FROM users WHERE sno = %s"%(user_id)
    cur.execute(delete_query)
    connection.commit()

    print("""
    <script>
        location.href="index.html";
        alert("deleted Successfully!!!!!");
    </script>
    """)
elif submit_no !=None:
    print("""
        <script>
            location.href="manage_acc.py?id=%s";
        </script>
        """%(id))
