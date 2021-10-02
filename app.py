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




            #hourPlanned = st.selectbox('Hora', ['23H30','08H30'])

        if st.button('Añadir OT'):
            add_data(crq_name,detalle,fecha,estado,alcance,tipoEjecucion,recurrente,n2Aprobador,fechaInicio,fechaFin,fechaAprobacion,hora,responsable,plataforma,servicio,solicitante,respDocumentacion,horaInicio,horaFin,horaAprobacion,respEjecucion,inicioEjecucion,finEjecucion,horaEjecucion,horaFinEjecucion )
            st.success('Adicionado Correctamente CRQ:{}'.format(crq_name))



    elif choice == 'Revisar':
        st.subheader('Revisar OTs Normales')
        result = view_all_data()
        #st.write(result)
        df = pd.DataFrame(result)#, columns=['CRQ NOMBRE', 'ESTADO', 'FECHA'])
        with st.expander('OTs NORMALES TOTAL'):
            st.dataframe(df)

        with st.expander('OTs NORMALES ESTADO'):
            estado_df = df['ESTADO'].value_counts().to_frame()

            st.dataframe(estado_df)


    elif choice == 'Modificar':
        st.subheader('Modificar OTs Normales')
        result = view_all_data()
        #st.write(result)
        df = pd.DataFrame(result, columns=['CRQ NOMBRE', 'ESTADO', 'FECHA'])
        with st.expander('OTs NORMALES ACTUALES'):
            st.dataframe(df)
        
        #st.write(view_unique_crq())
        list_of_crq = [i[0] for i in view_unique_crq()]
        #st.write(list_of_crq)
        select_crq = st.selectbox("CRQ para editar", list_of_crq)
        selected_result = get_crq(select_crq)
        #st.write(selected_result)

        if selected_result:
            crq_name = selected_result[0][0]
            estado = selected_result[0][1]
            datePlanned = selected_result[0][2]

            # Layout
            col1, col2 = st.columns(2)

            with col1:
                new_crq_name = st.text_area('CRQ Nombre', crq_name)
                

            with col2:
                new_estado = st.selectbox(estado, ['INGRESADO','ENVIADO N2','APROBADO','EXITOSO','REPLANIFICADO'])
                new_datePlanned = st.date_input(datePlanned)
                #hourPlanned = st.selectbox('Hora', ['23H30','08H30'])

            if st.button('Modificar OT'):
                edit_crq(new_crq_name,new_estado,new_datePlanned,crq_name,estado,datePlanned)
                st.success('Modificado Correctamente:: de {} hacia :: {}'.format(crq_name,new_crq_name))

        result2 = view_all_data()
        #st.write(result)
        df2 = pd.DataFrame(result2, columns=['CRQ NOMBRE', 'ESTADO', 'FECHA'])
        with st.expander('OTs NORMALES MODIFICADAS'):
            st.dataframe(df2)










    elif choice == 'Eliminar':
        st.subheader('Eliminar OTs Normales')
        result = view_all_data()
        #st.write(result)
        df = pd.DataFrame(result, columns=['CRQ NOMBRE', 'ESTADO', 'FECHA'])
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
        df2 = pd.DataFrame(new_result, columns=['CRQ NOMBRE', 'ESTADO', 'FECHA'])
        with st.expander('OTs NORMALES ACTUALES'):
            st.dataframe(df2)

    else:
        st.subheader('PAP')



if __name__ == '__main__':
    main()