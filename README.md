# 🕵️‍♂️ Sherlock CNPJ - Motor de Auditoria Corporativa

![Tech Stack](https://img.shields.io/badge/Tech-Python%20%7C%20Streamlit-blue?style=flat-square)
![Data Source](https://img.shields.io/badge/API-BrasilAPI-yellow?style=flat-square)
![Status](https://img.shields.io/badge/Status-Production-success?style=flat-square)

> **Ferramenta de investigação corporativa e compliance para extração e cruzamento de dados públicos.**

## 🎯 Arquitetura e Propósito
A verificação de fornecedores e a validação de *due diligence* são gargalos comuns em processos administrativos e auditorias financeiras. O **Sherlock CNPJ** foi desenvolvido para automatizar a triagem cadastral de empresas, mitigando riscos associados a fraudes, empresas de fachada e inconformidades fiscais.

Desenvolvido em Python, o sistema consome APIs governamentais (via BrasilAPI) para consolidar e formatar informações cruciais de governança — como o Quadro de Sócios e Administradores (QSA), viabilidade de Capital Social e endereço da sede — em um *dashboard* analítico de rápida leitura.

## ⚙️ Regras de Negócio e Funcionalidades

### 1. Extração Cadastral e Validação de Risco (Red Flags)
- Consumo via requisições HTTP (`requests`) para buscar a "capivara" completa da entidade corporativa.
- Evidenciação do Capital Social para cruzamento de capacidade financeira versus contratos licitados.

### 2. Mapeamento Societário (QSA)
- Identificação imediata dos beneficiários finais e administradores, mapeando conexões para políticas de Prevenção à Lavagem de Dinheiro (PLD) ou conflito de interesses.

### 3. Integração de Geolocalização (OSINT)
- Conversão automatizada de *strings* de endereço em *queries* parametrizadas para o Google Maps/Street View, permitindo a verificação remota da existência física da estrutura operacional da empresa.

## 💻 Stack Tecnológico
- **Python:** Motor de integração backend e tratamento de JSON.
- **Requests:** Biblioteca para roteamento HTTP assíncrono.
- **Streamlit:** Framework para a renderização reativa da interface de usuário.

## 🚀 Como Executar Localmente

1. Clone o repositório:
   ```bash
   git clone [https://github.com/othipedroso/sherlock-cnpj.git](https://github.com/othipedroso/sherlock-cnpj.git)