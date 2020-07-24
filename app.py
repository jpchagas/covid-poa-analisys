import streamlit as st

def main():
    page = st.sidebar.selectbox("Escolha uma opção:",['Todas','ABEV3.SA','MGLU3.SA','BBAS3.SA','BRKM5.SA','BBDC4.SA','AZUL4.SA','ITUB4.SA','BBDC3.SA','VALE3.SA','PETR4.SA','RENT3.SA','SUZB3.SA','CIEL3.SA','GOLL4.SA','GNDI3.SA','BRAP4.SA','B3SA3.SA','BTOW3.SA','EQTL3.SA'])
    st.title("MBA CONTROLADORIA E FINANÇAS - Mercado de Capitais")
    st.header('Carteira IBOVESPA Selecionada')

if __name__ == '__main__':
    main()