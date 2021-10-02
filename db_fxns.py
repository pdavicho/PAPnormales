import sqlite3
conn = sqlite3.connect("NORMALES.db", check_same_thread=False)
c = conn.cursor()


#Database
#Table
#Field/Columns
#Data Type

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS otsNormales(crq_name TEXT,detalle TEXT,fecha DATE,estado TEXT,alcance TEXT,tipoEjecucion TEXT,recurrente TEXT,n2Aprobador TEXT,fechaInicio DATE,fechaFin DATE,fechaAprobacion DATE,hora TEXT,responsable TEXT,plataform TEXT,servicio TEXT,solicitante TEXT,respDocumentacion TEXT,horaInicio TEXT,horaFin TEXT,horaAprobacion TEXT,respEjecucion TEXT,inicioEjecucion DATE,finEjecucion DATE,horaEjecucion TEXT,horaFinEjecucion TEXT )')

def add_data(crq_name,detalle,fecha,estado,alcance,tipoEjecucion,recurrente,n2Aprobador,fechaInicio,fechaFin,fechaAprobacion,hora,responsable,plataform,servicio,solicitante,respDocumentacion,horaInicio,horaFin,horaAprobacion,respEjecucion,inicioEjecucion,finEjecucion,horaEjecucion,horaFinEjecucion):
    c.execute('INSERT INTO otsNormales(crq_name,detalle,fecha,estado,alcance,tipoEjecucion,recurrente,n2Aprobador,fechaInicio,fechaFin,fechaAprobacion,hora,responsable,plataform,servicio,solicitante,respDocumentacion,horaInicio,horaFin,horaAprobacion,respEjecucion,inicioEjecucion,finEjecucion,horaEjecucion,horaFinEjecucion) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(crq_name,detalle,fecha,estado,alcance,tipoEjecucion,recurrente,n2Aprobador,fechaInicio,fechaFin,fechaAprobacion,hora,responsable,plataform,servicio,solicitante,respDocumentacion,horaInicio,horaFin,horaAprobacion,respEjecucion,inicioEjecucion,finEjecucion,horaEjecucion,horaFinEjecucion))
    conn.commit()


def view_all_data():
    c.execute('SELECT * FROM otsNormales')
    data = c.fetchall()
    return data

def view_unique_crq():
    c.execute('SELECT DISTINCT crq_name FROM otsNormales')
    data = c.fetchall()
    return data

def get_crq(crq):
    c.execute('SELECT * FROM otsNormales WHERE crq_name = "{}"'.format(crq))
    #c.execute('SELECT * FROM otsNormales WHERE crq_name = ?',(crq))
    data = c.fetchall()
    return data

def edit_crq(new_crq_name,new_estado,new_datePlanned,crq_name,estado,datePlanned):
    c.execute('UPDATE otsNormales SET crq_name=?, estado=?, datePlanned=? WHERE crq_name=? and estado=? and datePlanned=?', (new_crq_name,new_estado,new_datePlanned,crq_name,estado,datePlanned))
    conn.commit()
    data = c.fetchall()
    return data

def delete_data(crq_name):
    c.execute('DELETE FROM otsNormales WHERE crq_name="{}"'.format(crq_name))
    conn.commit()
