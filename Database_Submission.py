import sqlite3


##CREATEING THE DATABASE AND ESTABLISHING A CONNECTION
conn = sqlite3.connect('fileList.db')

#CREATING THE TABLE, POPULATING IT, AND RETRIEVING THE NECESSARY INFORMATION FOR THE ASSIGNMENT
with conn:
    cur = conn.cursor()
    list_of_files = ('information.docx', 'Hello.txt', 'myImage.png', \
                     'myMovie.mpg', 'world.txt', 'data.pdf', 'myPhoto.jpg')

    cur.execute('CREATE TABLE IF NOT EXISTS tbl_files (ID INTEGER PRIMARY KEY AUTOINCREMENT, col_FileName TEXT)')

    ##TABLE POPULATION
    for i in list_of_files:
        cur.execute('INSERT INTO tbl_files(col_fileName) VALUES(?)', (i,))
    
    #CREATING A VARIABLE THAT RECIEVES THE RETURNED DATA FROM THE 'SELECT' STATEMENT, THEN PRINTING IT TO THE SCREEN
    cur.execute('SELECT * FROM tbl_files WHERE col_FileName LIKE "%.txt" ')
    theList = cur.fetchall()
    print(theList)


conn.close()
