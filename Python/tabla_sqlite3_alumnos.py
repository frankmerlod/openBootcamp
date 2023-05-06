import sqlite3

def connexion():
    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE alumnos (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL
    )
                   ''')
    cursor.close()
    conn.close()
    
def nuevo_alumno(nombre, apellido):
    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO alumnos (nombre, apellido) VALUES ('{nombre}', '{apellido}')")
    conn.commit()
    cursor.close()
    conn.close()
    
def buscar_alumno(nombre, apellido):
    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()
    rows =cursor.execute(f"SELECT * FROM alumnos WHERE nombre='{nombre}' AND apellido='{apellido}'")
    alumno = rows.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    if alumno != None:
        print(alumno)
    else:
        print('No encontrado')
    

def main():
    connexion()
    nuevo_alumno('Frank', 'Merlo')
    nuevo_alumno('David', 'Monsalve')
    nuevo_alumno('Daniela', 'Monsalve')
    nuevo_alumno('Gabriela', 'Cordero')
    nuevo_alumno('Julio', 'Delgado')
    nuevo_alumno('Luis', 'Baez')
    nuevo_alumno('Eduardo', 'Martinez')
    nuevo_alumno('Oscar', 'Brito')
    buscar_alumno('Frank', 'Merlo')



if __name__ == "__main__":
    main()