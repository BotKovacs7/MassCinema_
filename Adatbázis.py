def adatbazisfuggveny():

    import mysql.connector
    import mysql

    TermekMySQL = mysql.connector.connect(host="localhost", user="root", password="", database="mozi_adatbazis")

    return adatbazisfuggveny
# python.exe -m pip install --upgrade pip