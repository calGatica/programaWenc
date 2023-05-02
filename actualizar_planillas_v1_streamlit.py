import os
import numpy as np
import pandas as pd
import streamlit as st

st.title('Programa bacán para Wenc :the_horns: :sunglasses:')
st.markdown('***')
col1, col2 = st.columns(2)
col1.subheader('Subir planilla Luis :point_down:')
LCV_file = col1.file_uploader('', label_visibility='collapsed', key='LCV')
col2.subheader('Subir planilla Gabriel :point_down:')
GAB_file = col2.file_uploader('', label_visibility='collapsed', key='GAB')

ignoreRows = np.array([7, 8, 9, 10, 21, 28, 38, 50, 56, 72, 76, 87, 98, 105, 116, 121, 125, 134, 145, 165, 179, 192, 196, 201, 208, 214, 217, 220, 222, 259, 263, 280, 286, 288, 314, 336, 338, 385, 387, 405, 409, 421]) - 1

if LCV_file is not None and GAB_file is not None:
    LCV_df = pd.read_excel(LCV_file, sheet_name='Detalle Proyección', usecols='A:B, K', header=5, skiprows=ignoreRows)
    GAB_df = pd.read_excel(GAB_file, sheet_name='Gastos Futuros', usecols='D, F', header=0)
    st.success('¡Archivos subidos correctamente!')
    if st.button('Proceder'):
        LCV_df = LCV_df.rename(columns = {'Unnamed: 0': 'PEPconNombre', 'Unnamed: 1': 'PEP'})
        LCV_df = LCV_df.dropna()

        values = []
        for pep in GAB_df.PEPconNombre:
            val = round(sum(LCV_df['TOTAL GASTOS FUTUROS'][LCV_df.PEPconNombre==pep]))
            values.append(val)

        GAB = GAB_df.copy()
        GAB['Por Contratar'] = np.array(values)
        GAB.to_excel('POR_CONTRATAR.xlsx', index=False)
        directory = os.getcwd()
        st.subheader('Se ha generado un nuevo archivo excel "POR_CONTRATAR.xlsx" en la carpeta donde está este programa:')
        st.subheader(directory)
        # st.download_button('Descargar', data = archivo, file_name='Por_Contratar.xlsx')
else:
    st.write('Debes subir ambas planillas')
# GAB_df = pd.read_excel(path+'Proyeccion_Gabriel.xlsx', sheet_name='Gastos Futuros', usecols='D, F', header=0)
# LCV_df = pd.read_excel(path+'Proyeccion_LCV.xlsx', sheet_name='Detalle Proyección', usecols='A:B, K', header=5, skiprows=ignoreRows)
