#!C:\Users\USER\AppData\Local\Programs\Python\Python312\python.exe
print("content-type:text/html\r\n\r\n")

import pymysql
connection=pymysql.connect(host="localhost",user="root",password="",database="project")
cur=connection.cursor()

# q=("INSERT INTO gk(question, option1, option2, option3, option4) VALUES "
#    "('Which is the longest river of India?','Krishna','Godavari','Brahmaputra','Ganga')")
# q="ALTER TABLE gk ADD answer varchar(255);"
# q="UPDATE gk SET answer='Ganga' WHERE sno=10;"
# cur.execute(q)

# q="create table history(sno int(10) auto_increment primary key,question varchar(255),option1 varchar(255),option2 varchar(255),option3 varchar(255),option4 varchar(255),answer varchar(255))"
# q="INSERT INTO history(question, option1, option2, option3, option4,answer) VALUES ('Battle of Plassey was fought in?','1757','1782','1748','1764','1757')"
# q="INSERT INTO history(question, option1, option2, option3, option4,answer) VALUES ('Who was the first prime minister of India?','Sardar Patel','Mahatma Gandhi','Indira gandhi','Jawaharlal Nehru','Jawaharlal Nehru')"

# val=[('Who was the last pharaoh of Egypt?','Cleopatra','Ramses','Nefertiti','Tutankhamun','Cleopatra')
#     ('Who was the first prime minister of India?','Sardar Patel','Mahatma Gandhi','Indira gandhi','Jawaharlal Nehru','Jawaharlal Nehru')]
# q="INSERT INTO technology (`question`, `option1`, `option2`, `option3`, `option4`, `answer`) (VALUES ('What does \'URL\' stand in web address?', 'Universal resource locator', 'Universal record locator', 'Uniform resource locator', 'Uniform record locator', 'universal resource locator'),
#     ('Which programming language if often used for developing mobiles apps on the iOS platform?', 'java', 'python', 'swift', 'C++', 'swift')
q="DROP TABLE science"
cur.execute(q)
connection.commit()
print("""
<script>
    alert("done!!")
</script>
""")