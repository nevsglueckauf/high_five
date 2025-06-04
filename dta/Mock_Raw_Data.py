import streamlit as st
import pyquiz.mock
import pyquiz.app
import pyquiz.entity

mock = pyquiz.mock.Mock()
#dta = mock.questions['category'].unique()



#dta = mock.filter_by('Category').equals('History')
#my_app = pyquiz.app.App()



st.markdown('# Mock data')
st.markdown("""Rohdaten aus JSON (
    - **nicht** gemerged und 
    - **nicht random sorted**)""")
#dta = mock.filterable
dta = mock.filterable.head(22)
#ql = pyquiz.entity.QuestionList(mock.questions)
mock.filter_by('category').equals('Geography')
edited = st.data_editor(dta,  hide_index=True, use_container_width=False)
        
         
if st.button("Speichern"):
    msg = "Daten gespeichert 💾"
    st.write(msg)
    st.sidebar.success(msg)        