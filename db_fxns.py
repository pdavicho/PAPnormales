import sqlite3
conn = sqlite3.connect("NORMALES.db", check_same_thread=False)
c = conn.cursor()


#Database
#Table
#Field/Columns
#Data Type

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS otsNormales(fecha DATE,hora TEXT,crq_name TEXT,detalle TEXT,estado TEXT,responsable TEXT,alcance TEXT,plataforma TEXT,tipoEjecucion TEXT,servicio TEXT,recurrente TEXT,solicitante TEXT,n2Aprobador TEXT,respDocumentacion TEXT,fechaInicio DATE,horaInicio TEXT,fechaFin DATE,horaFin TEXT,fechaAprobacion DATE,horaAprobacion TEXT,respEjecucion TEXT,inicioEjecucion DATE,horaEjecucion TEXT,finEjecucion DATE,horaFinEjecucion TEXT,observaciones TEXT)')

def add_data(fecha,hora,crq_name,detalle,estado,responsable,alcance,plataforma,tipoEjecucion,servicio,recurrente,solicitante,n2Aprobador,respDocumentacion,fechaInicio,horaInicio,fechaFin,horaFin,fechaAprobacion,horaAprobacion,respEjecucion,inicioEjecucion,horaEjecucion,finEjecucion,horaFinEjecucion,observaciones):
    c.execute('INSERT INTO otsNormales(fecha,hora,crq_name,detalle,estado,responsable,alcance,plataforma,tipoEjecucion,servicio,recurrente,solicitante,n2Aprobador,respDocumentacion,fechaInicio,horaInicio,fechaFin,horaFin,fechaAprobacion,horaAprobacion,respEjecucion,inicioEjecucion,horaEjecucion,finEjecucion,horaFinEjecucion,observaciones) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(fecha,hora,crq_name,detalle,estado,responsable,alcance,plataforma,tipoEjecucion,servicio,recurrente,solicitante,n2Aprobador,respDocumentacion,fechaInicio,horaInicio,fechaFin,horaFin,fechaAprobacion,horaAprobacion,respEjecucion,inicioEjecucion,horaEjecucion,finEjecucion,horaFinEjecucion,observaciones))
    conn.commit()


def view_all_data():
    c.execute('SELECT * FROM otsNormales')
    data = c.fetchall()
    return data

def view_unique_crq():
    c.execute('SELECT DISTINCT crq_name, detalle FROM otsNormales')
    data = c.fetchall()
    return data

def get_crq(crq):
    c.execute('SELECT * FROM otsNormales WHERE crq_name = "{}"'.format(crq))
    #c.execute('SELECT * FROM otsNormales WHERE crq_name = ?',(crq))
    data = c.fetchall()
    return data

def edit_crq(new_fecha,new_hora,new_crq_name,new_detalle,new_estado,new_responsable,new_alcance,new_plataforma,new_tipoEjecucion,new_servicio,new_recurrente,new_solicitante,new_n2Aprobador,new_respDocumentacion,new_fechaInicio,new_horaInicio,new_fechaFin,new_horaFin,new_fechaAprobacion,new_horaAprobacion,new_respEjecucion,new_inicioEjecucion,new_horaEjecucion,new_finEjecucion,new_horaFinEjecucion,new_observaciones):
    c.execute('UPDATE otsNormales SET fecha=?,hora=?,crq_name=?,detalle=?,estado=?,responsable=?,alcance=?,plataforma=?,tipoEjecucion=?,servicio=?,recurrente=?,solicitante=?,n2Aprobador=?,respDocumentacion=?,fechaInicio=?,horaInicio=?,fechaFin=?,horaFin=?,fechaAprobacion=?,horaAprobacion=?,respEjecucion=?,inicioEjecucion=?,horaEjecucion=?,finEjecucion=?,horaFinEjecucion=?,observaciones=? WHERE fecha=? and hora=? and crq_name=? and detalle=? and estado=? and responsable=? and alcance=? and plataforma=? and tipoEjecucion=? and servicio=? and recurrente=? and solicitante=? and n2Aprobador=? and respDocumentacion=? and fechaInicio=? and horaInicio=? and fechaFin=? and horaFin=? and fechaAprobacion=? and horaAprobacion=? and respEjecucion=? and inicioEjecucion=? and horaEjecucion=? and finEjecucion=? and horaFinEjecucion=? and observaciones=?', (new_fecha,new_hora,new_crq_name,new_detalle,new_estado,new_responsable,new_alcance,new_plataforma,new_tipoEjecucion,new_servicio,new_recurrente,new_solicitante,new_n2Aprobador,new_respDocumentacion,new_fechaInicio,new_horaInicio,new_fechaFin,new_horaFin,new_fechaAprobacion,new_horaAprobacion,new_respEjecucion,new_inicioEjecucion,new_horaEjecucion,new_finEjecucion,new_horaFinEjecucion,new_observaciones))
    conn.commit()
    data = c.fetchall()
    return data

def delete_data(crq_name):
    c.execute('DELETE FROM otsNormales WHERE crq_name="{}"'.format(crq_name))
    conn.commit()
