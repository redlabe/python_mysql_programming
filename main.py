import MySQLdb

#these parameters are needed for database connection
host="localhost"
user="new_user"
password="password"
db_file="students"

class DatabaseConnection:
    def __init__(self,host,user,password, db_file):
        #initialise the parsed argument
        self.db_file=db_file
        self.host=host
        self.user=user
        self.password=password
        
        
    def Connect(self):
        #this method connects to database using provided parameters
        db=MySQLdb.connect(host=self.host, 
                           user=self.user, 
                           password=self.password ,
                           database=self.db_file)
        return db
    
    def Disconnect(self):
        return self.Connect().close()
    
class DatabaseOperations(DatabaseConnection):
    
    
    
    
    def list_students(self):
        con=self.Connect()
        #create cursor
        curr = con.cursor()
        #sql query
        s_query="SELECT * FROM students"
        #loop cursor
        curr.execute(s_query)
        for row in curr.fetchall():
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")
        
        #close cursor
        curr.close()
        #Close connection
        self.Disconnect()
        
    def list_student_by_id(self, id):
        #create cursor
        curr = self.Connect().cursor()
        #sql query
        s_query="SELECT from students where id = %s"
        s_data=(id,)
        #loop cursor
        curr.execute(s_query,s_data)
        for row in curr.fetchall():
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")
        
        self.Connect().commit()
         #close cursor
        curr.close()
        #Close connection
        self.Disconnect()
        
    def insert_student(self, id, name, phone, email):
        #create cursor
        curr = self.Connect().cursor()
        #sql query
        s_query="INSERT INTO students (id,name, phone,email) VALUES (%s, %s,%s,%s)"
        s_data=(id, name,phone,email)
        #loop cursor
        curr.execute(s_query,s_data)
        
        self.Connect().commit()
         #close cursor
        curr.close()
        #Close connection
        self.Disconnect()
        
    def delete_student(self, id):
        #create cursor
        curr = self.Connect().cursor()
        #sql query
        s_query="DELETE from students where id = %s"
        s_data=(id,)
        #loop cursor
        curr.execute(s_query,s_data)
        
        self.Connect().commit()
         #close cursor
        curr.close()
        #Close connection
        self.Disconnect()
        
    def update_student(self, name, email, phone,id):
        #create cursor
        curr = self.Connect().cursor()
        #sql query
        s_query="UPDATE students SET name=%s, email=%, phone=%s where id=%s"
        s_data=(name, phone,email,id)
        #loop cursor
        curr.execute(s_query,s_data)
        
        self.Connect().commit()
         #close cursor
        curr.close()
        #Close connection
        self.Disconnect()
        
if __name__=="__main__":
    my_db=DatabaseOperations(host, user, password, db_file)
    my_db.list_students()
    my_db.insert_student(123, "martin",123233,"marting@gmail.com")
    my_db.delete_student(1)