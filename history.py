#!C:\Users\USER\AppData\Local\Programs\Python\Python312\python.exe
print("content-type:text/html\r\n\r\n")

import pymysql
import cgi, os

connection = pymysql.connect(host="localhost", user="root", password="", database="project")
cur = connection.cursor()
f = cgi.FieldStorage()
id = f.getvalue("id")

q = "select * from history where sno=1"
cur.execute(q)
r = cur.fetchone()

p = """SELECT timer FROM users WHERE sno ='%s'""" %(id)
cur.execute(p)
x = cur.fetchone()

p = """SELECT sound FROM users WHERE sno ='%s'""" %(id)
cur.execute(p)
y = cur.fetchone()

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
        
        .question{
            width:700px;
            height:100px;
            border-radius: 10px;
            border:2px solid white;

            margin-top:-530px;
            margin-left:300px;
        }
        .div1{
            margin: 30px;

              font-size:25px;
              padding: 15px;
              justify-content:center;
              align-item:center;
              display:flex;
              border:2px solid white;
              border-radius:10px;

              color:grey;
              cursor:pointer;
        }

        .main{
            margin-top:-50px;
        }
        input[type=submit]{
            display:flex;
            margin-left:310px;
            margin-top:30px;
            height:65px;
            width:290px;
            background-color: transparent;
        }
        
        #opt1.clicked{
            background-color:green;
        }
        #opt2.clicked{
            background-color:red;
        }
        #opt3.clicked{
            background-color:red;
        }
        #opt4.clicked{
            background-color:red;
        }
        #opt3{
            margin-left:690px;
            margin-top:-190px;
        }
        #opt4{
            margin-left:690px;

        }

        .next {
              background-color: #04AA6D;
              color: white;
            }

        .round {
              border-radius: 50%;
            }
            a {
                  text-decoration: none;
                  display: inline-block;
                  padding: 8px 16px;
                  margin-left:1000px;
                }

            a:hover {
                  background-color: #ddd;
                  color: black;
                }

        </style>

    </head>
    <body >""")
print("""
         <div id="timer" style="text-align: center; color: white; font-size: 24px;margin-top:30px;">Time left: 30 Seconds</div>
        <div class="main">


            <img src="files/qmark.png" width="1400" height="720">
            <div class="question">
                <h2 style="text-align:center;color:white;">%s</h2>
            </div>
            <form method="post" action="#" class="options">
                <input type="submit" name="sub" class="div1" id="opt1"value="%s" onclick="changeColor1()"></div>
                <input type="submit" name="sub" class="div1" id="opt2" value="%s"onclick="changeColor2()"></div>
                <input type="submit" name="sub" class="div1" id="opt3"value="%s"onclick="changeColor3()"></div>
                <input type="submit" name="sub" class="div1" id="opt4"value="%s"onclick="changeColor4()"></div>               
            </form>

            <a href="history2.py?id=%s" class="next round">&#8250;</a>
        </div>""" % (r[1], r[2], r[3], r[4], r[5], id))
print("""
    
        <script>
        
            let timerSeconds = %s;
      """%(x))

print(""" 


            const timerElement = document.getElementById("timer");

            function updateTimer() {
                timerElement.textContent = `Time left: ${timerSeconds} seconds`;
                timerSeconds--;

                if (timerSeconds < 0) {

                    location.href="history2.py?id=%s"

                } else {

                    setTimeout(updateTimer, 1000);
                }
            }

            updateTimer();


            </script>


    <script>
        function changeColor1(){

            var button=document.getElementById("opt1");
            button.classList.add("clicked");
        }
        function changeColor2(){
            var button=document.getElementById("opt2");
            button.classList.add("clicked");
        }
        function changeColor3(){
            var button=document.getElementById("opt3");
            button.classList.add("clicked");
        }
        function changeColor4(){
            var button=document.getElementById("opt4");
            button.classList.add("clicked");
        }
    </script>
    """%(id))

print("""
<script>
    if (%s == 1) {
        var audio = new Audio("countdown.mp3");
        audio.play();
    }
</script>
""" % (y))

print("""
</body>
</html>
""")

psub = f.getvalue("sub")
# print(puname,ppass)
if psub != None:
    print("""
        <script>
            location.href="history2.py?id=%s"
        </script>
    """ % (id))