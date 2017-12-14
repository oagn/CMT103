import sqlite3, os

def connect(filename):
    needcreate = not os.path.exists(filename)
    db = sqlite3.connect(filename)
    if needcreate:
        cursor = db.cursor()
        cursor.execute("CREATE TABLE authors ("
                       "id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, "
                       "name TEXT UNIQUE NOT NULL)")
        cursor.execute("CREATE TABLE books ("
                       "id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, "
                       "title TEXT NOT NULL, "
                       "year INTEGER NOT NULL,"
                       "author_id INTEGER NOT NULL, "
                       "FOREIGN KEY (author_id) REFERENCES authors)")
        db.commit()
        cursor.close()
    return db

def add_author(db, name):
    try:
        cursor=db.cursor()
        cursor.execute("SELECT * FROM authors where name='"+name+"'")
        cursor.execute("INSERT INTO authors (name) VALUES ('"+name+"')")
        db.commit()
        cursor.close()
    except sqlite3.IntegrityError:
        print ("The author exists already. ")
    return

def browse_authors(db, byOrder=False):
    cursor = db.cursor()
    sql_st="SELECT * FROM authors" if not byOrder else \
            "SELECT * FROM authors ORDER BY name ASC"    
    cursor.execute(sql_st)
    db.commit()
    records = cursor.fetchall()
    print("{:>4} | {:>16}".format('id', 'Author'))
    print("{0:->4} | {0:->16}".format(''))
    for item in records:
        print ("{:>4} | {:>16}".format(item[0], item[1]))
        cursor.close()
  


def delete_author(db, ID):
    cursor = db.cursor()
    cursor.execute("DELETE FROM authors WHERE id="+str(ID))
    db.commit()
    cursor.close()

def get_author_name(db, ID):
    cursor = db.cursor()
    cursor.execute("SELECT name FROM authors WHERE id="+str(ID))
    db.commit()
    record =cursor.fetchone()
    if not record:
        return  None
    cursor.close()
    return str(record[0]) 

def update_author(db, ID): # Interactive 
    cursor = db.cursor()
    auth =get_author_name(db, ID)
    if not auth:
        print ("No such author.")
        return
    name=input("Change name ("+get_author_name(db, ID)+") to: ")
    cursor.execute("UPDATE authors SET name='"+name+"' WHERE id="+str(ID))
    db.commit()
    cursor.close()

def get_author_ID(db, name):
    cursor = db.cursor()
    cursor.execute("SELECT id FROM authors WHERE name='"+name+"'")
    db.commit()
    record = cursor.fetchone()
    ID = None if not record else record[0]
    cursor.close()
    return ID

def add_book(db):
    cursor = db.cursor()
    title=input("\nTitle: ")
    year=input("Year: ")
    author=input("Author: ")
    authorID = get_author_ID(db, author)
    if not authorID:
        add_author(db, author)
    authorID = get_author_ID(db, author)
    
    cursor.execute("INSERT INTO books (title, year, author_id) VALUES ('"+title+"', "+str(year)+", "+str(authorID)+")")
    db.commit()
    cursor.close()
    
    
def browse_books(db):
    cursor = db.cursor()
    cursor.execute("SELECT books.id, books.title, books.year, authors.name FROM books JOIN authors ON books.author_id=authors.id")
    db.commit()
    records = cursor.fetchall()
    template = "{:>4} |{:>25} |{:>7} |{:>16} "
    print (template.format('id', 'Title', 'Year','Author' ))
    print ("{0:->4} |{0:->25} |{0:->7} |{0:->16} ".format(''))  
    for item in records:
        print (template.format(item[0], item[1], item[2], item[3]))
    cursor.close()
     
def delete_book(db, ID):
    pass
        
def update_book(db, ID):
    pass

    
        
        

