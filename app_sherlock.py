import streamlit as st
import requests

# Configuração da Página
st.set_page_config(page_title="Sherlock CNPJ", page_icon="🕵️‍♂️", layout="wide")

def buscar_cnpj(cnpj):
    # Limpa a formatação
    cnpj_limpo = ''.join(filter(str.isdigit, cnpj))
    
    if len(cnpj_limpo) != 14:
        st.error("CNPJ inválido. Certifique-se de digitar 14 números.")
        return None
        
    url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj_limpo}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            st.error("Empresa não encontrada ou erro na base de dados (BrasilAPI).")
            return None
    except Exception as e:
        st.error(f"Erro de conexão: {e}")
        return None

# Interface Principal
st.title("🕵️‍♂️ Sherlock CNPJ")
st.markdown("Investigação e auditoria corporativa rápida: verifique sócios, capital social e situação cadastral em segundos.")

cnpj_input = st.text_input("Digite o CNPJ (apenas números):", max_chars=18)
buscar = st.button("Investigar", type="primary")

if buscar and cnpj_input:
    dados = buscar_cnpj(cnpj_input)
    
    if dados:
        st.divider()
        
        # Cabeçalho da Empresa
        situacao = dados.get("descricao_situacao_cadastral", "")
        cor_situacao = "green" if situacao == "ATIVA" else "red"
        
        st.subheader(dados.get("razao_social", "Razão Social Indisponível"))
        st.caption(f"Nome Fantasia: {dados.get('nome_fantasia', 'Não informado')} | Situação: :{cor_situacao}[{situacao}]")
        
        # Grid de Informações
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Atividade (CNAE)", dados.get("cnae_fiscal", "-"))
        with col2:
            capital = dados.get("capital_social", 0)
            capital_formatado = f"R$ {capital:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            st.metric("Capital Social", capital_formatado)
        with col3:
            abertura = dados.get("data_inicio_atividade", "-")
            if abertura != "-":
                abertura = "/".join(abertura.split("-")[::-1])
            st.metric("Abertura", abertura)
        with col4:
            st.metric("Natureza Jurídica", dados.get("natureza_juridica", "-")[:25] + "...")
            
        st.divider()
        
        # Quadro Societário (QSA)
        st.subheader("👥 Quadro Societário (QSA)")
        socios = dados.get("qsa", [])
        if socios:
            for socio in socios:
                nome = socio.get("nome_socio") or socio.get("razao_social")
                qualificacao = socio.get("qualificacao_socio", "Sócio")
                icone = "👤" if socio.get("nome_socio") else "🏢"
                st.info(f"{icone} **{nome}** - {qualificacao}")
        else:
            st.warning("Nenhum sócio informado na base de dados para este CNPJ.")
            
        st.divider()
        
        # Endereço e Geolocalização
        st.subheader("📍 Localização da Sede")
        endereco = f"{dados.get('logradouro')}, {dados.get('numero')} {dados.get('complemento', '')}, {dados.get('bairro')}, {dados.get('municipio')} - {dados.get('uf')}, CEP: {dados.get('cep')}"
        st.write(endereco)
        
        maps_url = f"https://www.google.com/maps/search/?api=1&query={requests.utils.quote(endereco)}"
        st.link_button("Ver no Google Street View", maps_url)