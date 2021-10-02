#Core pkgs
import streamlit as st

#Eda pkgs
import pandas as pd

#DB Fxn
from db_fxns import create_table, add_data, delete_data, view_all_data, get_crq, view_unique_crq, edit_crq, delete_data

def main():
    st.title("PAP_NORMALES")

    menu = ['Ingresar', 'Revisar', 'Modificar', 'Eliminar', 'PAP']
    choice = st.sidebar.selectbox('Menu', menu)

    create_table()

    if choice == 'Ingresar':
        st.subheader('Añadir OT Normal')
        # Layout
        crq_name = st.text_input('CRQ')#, value='CRQ-')
        detalle = st.text_area('Detalle',value='NORMAL:')
        
        col1, col2 = st.columns(2)

        with col1:
            fecha = st.date_input('Fecha')
            estado = st.selectbox('Estado', ['INGRESADO','ENVIADO N2','APROBADO','EXITOSO','REPLANIFICADO'])
            alcance = st.text_input('Alcance')
            tipoEjecucion = st.selectbox('Tipo Ejecucion', ['REMOTO', 'EN SITIO','EN SITIO Y REMOTO'])
            recurrente = st.text_input('Recurrente')
            n2Aprobador = st.selectbox('N2 Aprobador',['Carlos Castillo','Cristhian Vallejo','Elizabeth Peñaloza','Fabricio Oleas','Luis Chumo','Washington Chuqui'])
            fechaInicio = st.date_input('Fecha Inicio')
            fechaFin = st.date_input('Fecha Fin') 
            fechaAprobacion = st.date_input('Fecha Aprobacion')       
            

        with col2:
            
            hora = st.text_input('Hora')
            responsable = st.selectbox('Responsable', ['N1 PAP', 'N1 SOC', 'N1 SOC/N1 PAP', 'N2'])
            plataforma = st.selectbox('Plataforma', ['AAG','BORDER GATEWAY', 'DNS', 'DPI', 'FW Datos Móviles', 'FW Servicios', 'IPBB Datos Moviles','IPBB Datos Moviles PACO','IPBB Plataformas de voz','M2M','OTA','PACO','RED DE SERVICIOS','ROAMING DE DATOS','SITE','SMSC','USSD'])
            servicio = st.selectbox('Servicio',['EJECUCION','GESTION','GESTION Y EJECUCION'])
            solicitante = st.selectbox('Solicitante',['Alex Cespedes','Carlos Castillo','Cristhian Vallejo','Darwin Gomez','Diego Gualle','Diego Rocha','Eduardo Granja','Elizabeth Peñaloza','Fabricio Oleas','Juan Carlos Chico','Luis Chumo','N1 CORE','Pablo Delgado','Rolando Arteaga','RUTINA','Washington Chuqui'])
            respDocumentacion = st.selectbox('Resp. Documentacion',['Cristopher Reza','David Minango','Marllory Cobos','Patricio Jordan','Shirley Salazar'])
            horaInicio = st.text_input('Hora Inicio')
            horaFin = st.text_input('Hora Fin')
            horaAprobacion = st.text_input('Hora Aprobacion')
        
        respEjecucion = st.selectbox('Resp. Ejecucion',['Cristopher Reza','David Minango','Marllory Cobos','Patricio Jordan','Shirley Salazar'])
        col3, col4 = st.columns(2)
        with col3:
            inicioEjecucion = st.date_input('Inicio Ejecucion')
            finEjecucion = st.date_input('Fin Ejecucion')

        with col4:
            horaEjecucion = st.text_input('Hora Ejecucion')
            horaFinEjecucion = st.text_input('Hora Fin Ejecucion')

        observaciones = st.text_input('OBSERVACIONES: ')

        if st.button('Añadir OT'):
            add_data(fecha,hora,crq_name,detalle,estado,responsable,alcance,plataforma,tipoEjecucion,servicio,recurrente,solicitante,n2Aprobador,respDocumentacion,fechaInicio,horaInicio,fechaFin,horaFin,fechaAprobacion,horaAprobacion,respEjecucion,inicioEjecucion,horaEjecucion,finEjecucion,horaFinEjecucion,observaciones)
            st.success('Adicionado Correctamente CRQ:{}'.format(crq_name))



    elif choice == 'Revisar':
        st.subheader('Revisar OTs Normales')
        result = view_all_data()
        #st.write(result)
        df = pd.DataFrame(result, columns=['FECHA','HORA','CRQ','Detalle','ESTADO','Responsable','Alcance','Plataforma','Tipo Ejecucion','SERVICIO','Recurrente','SOLICITANTE','N2APROBADOR','Resp Documentacion','FechaInicio','HoraInicio','FechaFin','HoraFin','FechaAprobacion','HoraAprobacion','Resp Ejecucion','Inicio Ejecucion','Hora Ejecucion','Fin Ejecucion','Hora Fin Ejecucion','Observaciones: '])
        with st.expander('OTs NORMALES TOTAL'):
            st.dataframe(df)

        with st.expander('OTs NORMALES ESTADO'):
            estado_df = df['ESTADO'].value_counts().to_frame()

            st.dataframe(estado_df)

########### MODIFICAR #####################

    elif choice == 'Modificar':
        st.subheader('Modificar OTs Normales')
        result = view_all_data()
        #st.write(result)
        df = pd.DataFrame(result, columns=['FECHA','HORA','CRQ','Detalle','ESTADO','Responsable','Alcance','Plataforma','Tipo Ejecucion','SERVICIO','Recurrente','SOLICITANTE','N2APROBADOR','Resp Documentacion','FechaInicio','HoraInicio','FechaFin','HoraFin','FechaAprobacion','HoraAprobacion','Resp Ejecucion','Inicio Ejecucion','Hora Ejecucion','Fin Ejecucion','Hora Fin Ejecucion','Observaciones: '])
        with st.expander('OTs NORMALES ACTUALES'):
            st.dataframe(df)
        
        #st.write(view_unique_crq())
        list_of_crq = [i[0] for i in view_unique_crq()]
        #st.write(list_of_crq)
        select_crq = st.selectbox("CRQ para editar", list_of_crq)
        selected_result = get_crq(select_crq)
        #st.write(selected_result)

        if selected_result:
            fecha = selected_result[0][0]
            hora = selected_result[0][1]
            crq_name = selected_result[0][2]
            detalle = selected_result[0][3]
            estado = selected_result[0][4]
            responsable = selected_result[0][5]
            alcance = selected_result[0][6]
            plataforma = selected_result[0][7]
            tipoEjecucion = selected_result[0][8]
            servicio = selected_result[0][9]
            recurrente = selected_result[0][10]
            solicitante = selected_result[0][11]
            n2Aprobador = selected_result[0][12]
            respDocumentacion = selected_result[0][13]
            fechaInicio = selected_result[0][14]
            horaInicio = selected_result[0][15]
            fechaFin = selected_result[0][16]
            horaFin = selected_result[0][17]
            fechaAprobacion = selected_result[0][18]
            horaAprobacion = selected_result[0][19]
            respEjecucion = selected_result[0][20]
            inicioEjecucion = selected_result[0][21]
            horaEjecucion = selected_result[0][22]
            finEjecucion = selected_result[0][23]
            horaFinEjecucion = selected_result[0][24]
            observaciones = selected_result[0][25]

            # Layout
            new_crq_name = st.text_input('CRQ', crq_name)#, value='CRQ-')
            new_detalle = st.text_area('Detalle', detalle)
            
            col1, col2 = st.columns(2)

            with col1:
                new_fecha = st.date_input('Fecha')
                new_estado = st.selectbox(estado, ['INGRESADO','ENVIADO N2','APROBADO','EXITOSO','REPLANIFICADO'])
                new_alcance = st.text_input('Alcance',alcance)
                new_tipoEjecucion = st.selectbox(tipoEjecucion, ['REMOTO', 'EN SITIO','EN SITIO Y REMOTO'])
                new_recurrente = st.text_input('Recurrente',recurrente)
                new_n2Aprobador = st.selectbox(n2Aprobador,['Carlos Castillo','Cristhian Vallejo','Elizabeth Peñaloza','Fabricio Oleas','Luis Chumo','Washington Chuqui'])
                new_fechaInicio = st.date_input('Fecha Inicio')
                new_fechaFin = st.date_input('Fecha Fin') 
                new_fechaAprobacion = st.date_input('Fecha Aprobacion')       
                

            with col2:
                
                new_hora = st.text_input('Hora', hora)
                new_responsable = st.selectbox(responsable, ['N1 PAP', 'N1 SOC', 'N1 SOC/N1 PAP', 'N2'])
                new_plataforma = st.selectbox(plataforma, ['AAG','BORDER GATEWAY', 'DNS', 'DPI', 'FW Datos Móviles', 'FW Servicios', 'IPBB Datos Moviles','IPBB Datos Moviles PACO','IPBB Plataformas de voz','M2M','OTA','PACO','RED DE SERVICIOS','ROAMING DE DATOS','SITE','SMSC','USSD'])
                new_servicio = st.selectbox(servicio,['EJECUCION','GESTION','GESTION Y EJECUCION'])
                new_solicitante = st.selectbox(solicitante,['Alex Cespedes','Carlos Castillo','Cristhian Vallejo','Darwin Gomez','Diego Gualle','Diego Rocha','Eduardo Granja','Elizabeth Peñaloza','Fabricio Oleas','Juan Carlos Chico','Luis Chumo','N1 CORE','Pablo Delgado','Rolando Arteaga','RUTINA','Washington Chuqui'])
                new_respDocumentacion = st.selectbox(respDocumentacion,['Cristopher Reza','David Minango','Marllory Cobos','Patricio Jordan','Shirley Salazar'])
                new_horaInicio = st.text_input('Hora Inicio', horaInicio)
                new_horaFin = st.text_input('Hora Fin', horaFin)
                new_horaAprobacion = st.text_input('Hora Aprobacion', horaAprobacion)
            
            new_respEjecucion = st.selectbox(respEjecucion,['Cristopher Reza','David Minango','Marllory Cobos','Patricio Jordan','Shirley Salazar'])

            col3, col4 = st.columns(2)
            with col3:
                new_inicioEjecucion = st.date_input('Inicio Ejecucion')
                new_finEjecucion = st.date_input('Fin Ejecucion')

            with col4:
                new_horaEjecucion = st.text_input('Hora Ejecucion', horaEjecucion)
                new_horaFinEjecucion = st.text_input('Hora Fin Ejecucion', horaFinEjecucion)

            new_observaciones = st.text_input('OBSERVACIONES: ', observaciones)

            if st.button('Modificar OT'):
                    edit_crq(new_fecha,new_hora,new_crq_name,new_detalle,new_estado,new_responsable,new_alcance,new_plataforma,new_tipoEjecucion,new_servicio,new_recurrente,new_solicitante,new_n2Aprobador,new_respDocumentacion,new_fechaInicio,new_horaInicio,new_fechaFin,new_horaFin,new_fechaAprobacion,new_horaAprobacion,new_respEjecucion,new_inicioEjecucion,new_horaEjecucion,new_finEjecucion,new_horaFinEjecucion,new_observaciones)
                    st.success('Modificado Correctamente:: de {} hacia :: {}'.format(crq_name,new_crq_name))

        result2 = view_all_data()
        #st.write(result)
        df2 = pd.DataFrame(result2, columns=['FECHA','HORA','CRQ','Detalle','ESTADO','Responsable','Alcance','Plataforma','Tipo Ejecucion','SERVICIO','Recurrente','SOLICITANTE','N2APROBADOR','Resp Documentacion','FechaInicio','HoraInicio','FechaFin','HoraFin','FechaAprobacion','HoraAprobacion','Resp Ejecucion','Inicio Ejecucion','Hora Ejecucion','Fin Ejecucion','Hora Fin Ejecucion','Observaciones: '])
        with st.expander('OTs NORMALES MODIFICADAS'):
            st.dataframe(df2)




################## ELIMINAR ############################

    elif choice == 'Eliminar':
        st.subheader('Eliminar OTs Normales')
        result = view_all_data()
        #st.write(result)
        df = pd.DataFrame(result, columns=['FECHA','HORA','CRQ','Detalle','ESTADO','Responsable','Alcance','Plataforma','Tipo Ejecucion','SERVICIO','Recurrente','SOLICITANTE','N2APROBADOR','Resp Documentacion','FechaInicio','HoraInicio','FechaFin','HoraFin','FechaAprobacion','HoraAprobacion','Resp Ejecucion','Inicio Ejecucion','Hora Ejecucion','Fin Ejecucion','Hora Fin Ejecucion','Observaciones: '])
        with st.expander('OTs NORMALES ACTUALES'):
            st.dataframe(df)

        list_of_crq = [i[0] for i in view_unique_crq()]
        #st.write(list_of_crq)
        select_crq = st.selectbox("CRQ para eliminar", list_of_crq)
        st.warning("Desea eliminar :: {}".format(select_crq))
        if st.button("Eliminar CRQ"):
            delete_data(select_crq)
            st.success("CRQ fue correctamente eliminada")
        new_result = view_all_data()
        #st.write(result)
        df2 = pd.DataFrame(new_result, columns=['FECHA','HORA','CRQ','Detalle','ESTADO','Responsable','Alcance','Plataforma','Tipo Ejecucion','SERVICIO','Recurrente','SOLICITANTE','N2APROBADOR','Resp Documentacion','FechaInicio','HoraInicio','FechaFin','HoraFin','FechaAprobacion','HoraAprobacion','Resp Ejecucion','Inicio Ejecucion','Hora Ejecucion','Fin Ejecucion','Hora Fin Ejecucion','Observaciones: '])
        with st.expander('OTs NORMALES ACTUALES'):
            st.dataframe(df2)

    else:
        st.subheader('PAP')



if __name__ == '__main__':
    main()