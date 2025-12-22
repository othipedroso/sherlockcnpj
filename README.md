# 🕵️‍♂️ Sherlock CNPJ

![GitHub deployments](https://img.shields.io/github/deployments/othipedroso/sherlock-cnpj/github-pages?label=Deploy&logo=github&style=flat-square)
![Tech Stack](https://img.shields.io/badge/Tech-HTML%20%7C%20JS%20%7C%20BrasilAPI-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

> **Investigação corporativa para cidadãos.** Uma ferramenta open source para consultar dados públicos de empresas, verificar sócios (QSA) e validar a existência física de fornecedores do governo.

---

## 🔗 [Acesse a Ferramenta Online](https://othipedroso.github.io/sherlock-cnpj/)

---

## 🎯 O Propósito
No combate à corrupção, não basta saber **quanto** um político gastou, é preciso saber **quem recebeu**. Muitas vezes, verbas públicas são destinadas a empresas de fachada, empresas com capital social incompatível ou pertencentes a "laranjas".

O **Sherlock CNPJ** foi criado para ser o "irmão" do [Radar Transparência](https://github.com/othipedroso/radar-transparencia), permitindo que qualquer cidadão audite os fornecedores citados nas notas fiscais parlamentares.

---

## ✨ Funcionalidades de Investigação

### 1. 📋 Capivara Completa (Dados Cadastrais)
- Consulta instantânea via API pública.
- Exibe **Razão Social**, **Nome Fantasia**, **Data de Abertura** e **Natureza Jurídica**.
- Alerta visual sobre a **Situação Cadastral** (Ativa/Inativa).

### 2. 👥 Quem são os donos? (QSA)
- Lista o **Quadro de Sócios e Administradores**.
- Permite identificar se a empresa pertence a parentes de políticos ou pessoas politicamente expostas.
- Diferencia visualmente sócios Pessoas Físicas (👤) de Pessoas Jurídicas (🏢).

### 3. 🚩 Análise de "Red Flags"
- **Capital Social:** Mostra o valor em destaque. (Empresas com capital baixo ganhando contratos milionários são suspeitas).
- **CNAE (Atividade):** Exibe a atividade econômica principal. (Uma padaria fornecendo equipamentos de TI?).

### 4. 📍 Verificação de Localização Real
- Gera um link direto para o **Google Street View** com o endereço exato da sede.
- Permite verificar se o local condiz com a empresa (ex: uma grande construtora sediada em uma casa residencial simples).

### 5. 🔌 Integração Automática
- O sistema aceita parâmetros via URL para integração com outros sistemas.
- Exemplo: `sherlock.html?cnpj=00000000000191` já abre a página pesquisando automaticamente.

---

## 🛠️ Tecnologias Utilizadas

Projeto *Client-Side* puro, focado em privacidade e velocidade. Não armazena dados do usuário.

- **Frontend:** HTML5, CSS3 (Variáveis e Grid), Vanilla JavaScript.
- **API Externa:** [BrasilAPI](https://brasilapi.com.br/) (Fonte de dados gratuita e aberta).
- **Design:** Interface escura ("Hacker Mode") focada em leitura de dados.

---

## 🚀 Como rodar localmente

1. Clone este repositório:
   ```bash
   git clone [https://github.com/othipedroso/sherlock-cnpj.git](https://github.com/othipedroso/sherlock-cnpj.git)
