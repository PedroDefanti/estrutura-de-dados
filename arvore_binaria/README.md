# 🌲 Visualizador de Árvore Binária de Busca (BST) - Django

Este projeto é uma aplicação web interativa desenvolvida com **Django** (Python) e **D3.js** (JavaScript) para visualizar, manipular e otimizar Árvores Binárias de Busca (BST).

---

## ✨ Funcionalidades Principais

| Funcionalidade | Descrição | Implementação |
| :--- | :--- | :--- |
| **Inserção** | Adiciona um novo valor à árvore, mantendo a propriedade BST. | `core/views.py` (`insert_value`) |
| **Exclusão** | Remove um nó da árvore (tratando casos de 0, 1 ou 2 filhos). | `core/views.py` (`delete_value`) |
| **Busca** | Permite buscar um valor e destacá-lo visualmente na árvore. | `core/views.py` (`search_value`) |
| **Inicialização/Reset** | Cria ou reinicia a árvore com uma lista de valores, forçando o balanceamento. | `core/views.py` (`initialize_tree`) |
| **Balanceamento** | Aplica o algoritmo **Day-Stout-Warren (DSW)** para transformar a BST em uma estrutura o mais balanceada possível, otimizando o desempenho de busca. | `core/models.py` (`balance`) |
| **Visualização** | Renderiza a estrutura da árvore dinamicamente no navegador. | `core/templates/home.html` (D3.js) |
| **Persistência** | O estado da árvore é salvo no banco de dados por sessão, garantindo que a árvore permaneça a mesma ao recarregar a página. | `core/models.py` (`BSTSession`) |

---

## 💻 Tecnologias

O projeto é construído com um *stack* de tecnologias web padrão:

* **Backend:** Python 3.x, **Django 5.x**
* **Frontend:** HTML5, CSS3, JavaScript
* **Visualização:** **D3.js** (para a renderização dos gráficos da árvore)
* **Banco de Dados:** **SQLite** (padrão para desenvolvimento)

---

## 🚀 Configuração e Execução

Siga os passos abaixo para configurar e rodar o projeto localmente.

### Pré-requisitos

Certifique-se de ter o **Python 3.** instalado em seu sistema.


# OS COMANDOS A SEGUIR SÃO PARA SEREM FEITOS PELO TERMINAL DO VISUAL STUDIO CODE:

# 1. Crie o seu ambiente virtual

# Cria o ambiente virtual
python -m venv .venv


# 2. Ative o seu ambiente virtual

# Ativa o ambiente virtual
# Linux/macOS
source venv/bin/activate
# Windows
.\venv\Scripts\activate

# 3. Instale esse framework

pip install django OU pip install requirements.txt

# 4. Digite esses comandos para fazer a atualização

python manage.py makemigrations core
python manage.py migrate


 # 5. Digite esse comando para o programa funcionar 
python manage.py runserver


# 6.Clique com o mouse segurando o Ctrl no IP


Watching for file changes with StatReloader
Performing system checks...
System check identified no issues (0 silenced).
You have 18 unapplied migration(s). ... 
Starting development server at --------->http://127.0.0.1:8000/ <--------- # Aparecer um IP assim,clique nele segurando o botão Ctrl
Quit the server with CTRL-BREAK (Windows) or CTRL-C (Mac/Linux).
