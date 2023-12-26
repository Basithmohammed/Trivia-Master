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
    <link rel="icon" href="files/images.jpeg">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>
            body{
            background-image: url('files/quizbg6.jpg');
          background-repeat:no-repeat;
          background-size:cover;
        }
            .div1{
                width: 400px;
                height: 400px;
                margin-left: 540px;
                border-radius: 10px;
                background-color: rgba(0,184,255,0.2);
                margin-top: 100px;
                box-shadow: 5px 5px 5px #2b2626;
               
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
            
            
            label{
                opacity: 0.5;
                font-size: 15px;
                margin-left: 60px;
                margin-top: 50px;
            }
            h1{
                text-align: center;
                font-size: 45px;
                padding-top: 30px;
                color: white;
                opacity: 0.5;
            }
            input[type="submit"]{
                background-color: darkolivegreen;
                color: whitesmoke; font-size: 20px;
            }
            input[type="submit"]:hover{
                background-color: rgb(27, 89, 14);
                color: whitesmoke;
                 font-size: 20px;
            }
            
            .back{
                margin-top:-490px;
                position:relative;
                font-size:29px;
            }
        </style>

    </head>
    <body>
<div class=div1>
<form action="#" method="post" enctype="multipart/form-data">
    <h1>Update Profile</h1>
    
    <input type="text" name="newname" placeholder="New Username">
    <label style="margin-top:20px; color:white; font-size:16px;">New Profile Photo:<input type="file" name="newprofile"></label>
    <br><br>
    
    <input type="submit" name="submit" value="Save Changes">
</form>
</div>
<p class="back"><a href="manage_acc.py?id=%s" style="color:white;text-decoration:none;opacity:0.5;">
        &#x21A9</a></p>

<p class="par1" style="color:white;position:absolute;margin-top:600px;margin-left:420px;font-size:15px;
    text-align:center;opacity:0.5;">By Registering,you agree to our <a href="#"style="color:white;opacity:0.5;text-decoration:none;">
    Terms & Condition</a> and acknowledge you've read our <a href="#" style="color:white;opacity:0.5;text-decoration:none;">Privacy Policy.</a> </p>
</body>
</html>
"""%(id))

new_username = f.getvalue("newname")
new_profile = f['newprofile']
sub= f.getvalue("submit")
if sub!=None:
    fn=os.path.basename(new_profile.filename)
    open('files/'+fn, "wb").write(new_profile.file.read())
    q="""update users set name='%s',profile='%s' where sno='%s'""" %(new_username, fn,id)
    print(q)
    cur.execute(q)
    connection.commit()
    print("""
            <script>
                    location.href="userpage.py?id=%s";
                    alert("Updated Successfully!!!!!");
                </script>
        """%(id))
