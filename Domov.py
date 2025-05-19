import streamlit as st
st.set_page_config(layout="wide")

st.title('Predstavenie projektu')

st.subheader('Zadanie:')
st.html("""<p>V súčasnosti firmy využívajú služby množstva cloudových služieb, ktoré komunikujú s používateľmi aj pomocou emailov. Pritom v prípade prijatia emailu z externej domény, nie je zrejmé, či sa jedná o legitímnu požiadavku alebo hackerský bezpečnostný útok na zamestnancov.
Cieľom práce je vyvinúť MS Outlook plugin, ktorý rozpozná a indikuje, či sa jedná o mail zaslaný firemnému užívateľovi poskytovateľom autorizovaným voči danej firme alebo o email pochádzajúci z nerozpoznanej domény. Riešenie by malo pokrývať základné procesy pre premapovanie autorizovaných providerov voči firme, firme voči pluginu u používateľa použitím kryptografických primitív pri predpoklade použitia použivateľského počítača v prostredí otvoreného internetu (teda s možnosťou manipulácie nechráneného toku údajov).</p>""")

st.subheader('Stránka admin panelu:')
st.markdown('Odkaz na admin panel je [tu](%s)' % "https://timovy-projekt.polandcentral.cloudapp.azure.com/")
st.caption('Pre zapnutie stránky, napíšte členom tímu')

st.subheader('Manifest na pridanie pluginu do Outlooku:')
st.download_button('Stiahnuť manifest', data='files/manifest_fajnl_2.xml', file_name='manifest.xml', mime='application/xml')
