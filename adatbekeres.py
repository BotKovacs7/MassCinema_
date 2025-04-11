from Adatbázis import get_connection

def uj_foglalas(vezeteknev, keresztnev, teremszam, szek):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO foglalasok (vezeteknev, keresztnev, teremszam, szekszam)
        VALUES (%s, %s, %s, %s)
    """, (vezeteknev, keresztnev, teremszam, szek))
    conn.commit()
    conn.close()


def foglalasok_szama(teremszam):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM foglalasok WHERE teremszam = %s", (teremszam,))
    db_count = cursor.fetchone()[0]
    conn.close()
    return db_count


def torol_foglalas(foglalasi_szam):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM foglalasok WHERE foglalasszam = %s", (foglalasi_szam,))
    conn.commit()
    conn.close()
