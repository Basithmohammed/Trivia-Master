#!C:\Users\USER\AppData\Local\Programs\Python\Python312\python.exe
print("content-type:text/html\r\n\r\n")
import cgi
import pymysql
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
          color:grey;
          font-size:20px;
        }
            .div1{
                width: 550px;
                height: 500px;
                margin-left: 450px;
                
                border-radius: 10px;
                background-color: rgba(125,55,5,0.1);
                margin-top: 100px;
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
            
            label{
                opacity: 0.5;
                font-size: 15px;
                margin-left: 90px;
                margin-top: -16px;
            }
            
            .w3-xxlarge{
                margin-top:-530px;
                margin-left:-20px;
                position:relative;
                font-size:29px;
            }

            select{
                width:150px;
                border-radius:6px;
            }
            .back{
                margin-top:-570px;
                position:relative;
                font-size:29px;
            }
            label{
                font-size:29px;
            }
            .radio{
                font-size:15px;
                margin-left:300px;
            }
            .audio{
                font-size:15px;
                margin-left:15px;
                margin-top:6px;
                position:absolute;
                color:white;
            }
            .two{
                margin-left:102px;
            }
        </style>

    </head>
    <body>
    <div class="main">

        <div class="div1">
        <form name="form-1" method="post" action="" >
        
            <h1 style="margin-top:10px;margin-left:-20px;"><strong>Settings</strong></h1><br>
            <label for="timerDuration" style="margin-left:10px;color:white;">Select Timer Duration:</label>
            <input type="radio" name="timerDuration" value="15" class="radio"> <span style="margin-left:300px;margin-top:-30px;">15 seconds</span><br>
            <input type="radio" name="timerDuration" value="20" class="radio"> <span style="margin-left:300px;margin-top:-30px;">20 seconds</span><br>
            <input type="radio" name="timerDuration" value="30" class="radio"> <span style="margin-left:300px;margin-top:-30px;">30 seconds</span>
            
            <br>
            <label for="audio" style="margin-left:15px;margin-top:5px;color:white;">Audio:
            <input type="radio" name="audio" value="1" class="audio"> <span style="margin-left:100px;margin-top:-100px;
            font-size:15px;">ON</span><br>
            <input type="radio" name="audio" value="0" class="audio two"> <span style="margin-left:180px;margin-top:-100px;
            font-size:15px;">OFF</span>
           
            <br><br>
            
        <input type="submit" value="Save Settings" name="sub" style="margin-left:130px;"> <br>    
            
        </div>
       <p class="back"><a href="quizpage.py?id=%s" style="color:white;text-decoration:none;opacity:0.5;">
        &#x21A9</a></p>"""%(id))

print("""   </div>   
    <p class="par1" style="color:white;position:absolute;margin-top:520px;margin-left:450px;font-size:15px;
    text-align:center;opacity:0.5;">By Registering,you agree to our <a href="#"style="color:white;opacity:0.5;text-decoration:none;">
    Terms & Condition</a> and acknowledge you've read our <a href="#" style="color:white;opacity:0.5;text-decoration:none;">Privacy Policy.</a> </p>
    
    
    
    
    </body>
    </html>
""")

timer_duration = f.getvalue("timerDuration")

if timer_duration:
    q = """UPDATE users SET timer= '%s' WHERE sno= '%s' """% (timer_duration, id)
    cur.execute(q)


audio_file=f.getvalue("audio")

if audio_file:
    p="""UPDATE users SET sound= '%s' WHERE sno= '%s' """% (audio_file, id)
    cur.execute(p)

    print("""
                    <script>
                        alert("Success!!");
                    </script>
                """)
connection.commit()

