# Documentação do Projeto: UniSearch

## 1. Visão Geral

**Tecnologias Utilizadas:**

* Python
* FastAPI
* Uvicorn
* Requests (API externa)

**Descrição:**
Sistema de busca por universidades ao redor do mundo, baseado na API pública [Hipolabs University API](http://universities.hipolabs.com/).

**Objetivo:**
Fornecer uma plataforma para pesquisa de universidades por nome ou país, com possibilidade futura de filtragem mais avançada e recursos adicionais.

---

## 2. Descrição Detalhada do Projeto

**O que é o projeto?**
Uma aplicação web que permite ao usuário pesquisar universidades usando dados da API pública Hipolabs. Retorna nome, país, domínio e site da instituição.

---

### 2.1 Funcionalidades Principais

#### Funcionalidades já implementadas (30%):

* **Rota 1:** Buscar universidades por país (`/universidades/pais`)
* **Rota 2:** Buscar universidades por nome (`/universidades/nome`)

---

#### Funcionalidades futuras planejadas:

* **Rota 3:** Buscar universidades brasileiras (`/universidades/brasil`)

---

### 2.2 Arquitetura do Código

```
unisearch/
├── main.py          # Inicia o app FastAPI
├── api.py           # Define as rotas da aplicação
├── models.py        # Modelos Pydantic
├── services.py      # Funções auxiliares e consumo da API externa
├── requirements.txt # Dependências
```

---

## 3. Etapas de Entrega (Cronograma Detalhado)

**Etapa 1 (atual – 30%)**

* Definição do escopo e estrutura do projeto
* Implementação das rotas básicas de busca por país e nome

**Etapa 2**

* Criação de rota local com dados filtrados do Brasil
* Início da persistência local (ex: JSON ou SQLite)

**Etapa 3**

* Filtros por estado e classificação (pública/privada)
* Salvamento de universidades favoritas

**Etapa 4**

* Integração com APIs externas auxiliares (RESTCountries, IBGE)
* Melhoria da exibição de dados

**Etapa 5**

* Deploy e documentação final

## 4. Requisitos

### 4.1 Requisitos funcionais

* O usuário pode buscar universidades por país.


* O usuário pode buscar universidades por nome.


* O sistema exibe nome, país, domínio e site da instituição.


* O sistema deve permitir futura filtragem por domínio ou classificação (privada/pública).


* O sistema deverá permitir login e marcação de universidades como favoritas (planejado).


* O sistema poderá armazenar e exibir resultados com cache local.

### 4.2 Requisitos não-funcionais
* Desempenho: As respostas da API devem ser processadas em até 3 segundos.


* Usabilidade: Interface amigável e clara para busca, com documentação interativa via Swagger.


* Segurança: Toda alteração de dados (favoritos) será protegida por autenticação JWT.


* A API usará controle de acesso para evitar acessos não autorizados.


* Escalabilidade: Suporte a expansão futura com banco de dados, cache e integração com múltiplas APIs.


* Compatibilidade: A aplicação será acessível via navegadores modernos.
