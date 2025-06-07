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

* **Rota 3:** Buscar universidades brasileiras (`/universidades/brasil`) e aplicar filtros locais por:

  * Estado (a partir do nome ou domínio, com regras manuais)
  * Domínio (ex: `.edu.br`, `.com`)
  * Tipo estimado (pública ou privada, por nome)
* **Rota 4:** Marcar universidades como favoritas (com persistência em banco ou JSON)
* **Rota 5:** Integração com RESTCountries para exibir dados extras do país
* **Rota 6:** Armazenar dados localmente (cache) para permitir filtragens mais avançadas

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