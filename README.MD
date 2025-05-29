📦 Plataforma de Gestão de Dados Pessoais
Este projeto é uma aplicação em Python para gerenciar dados pessoais com foco em cibersegurança, proteção de dados (LGPD) e boas práticas de desenvolvimento, integrando validações, criptografia, controle de acesso e testes automatizados.

🚀 Funcionalidades
🔒 Cadastro com criptografia de CPF, nome e senha.

🔑 Login com autenticação segura.

👥 Diferentes permissões de usuário (admin e comum).

🗂️ Listagem, exclusão e manipulação segura dos dados.

🧪 Testes automatizados com unittest.

💾 Armazenamento local seguro via arquivo .json.

🔧 Tecnologias e Bibliotecas
Python 3.11+

cryptography – para criptografia AES dos dados sensíveis.

unittest – para testes automatizados.

json – para armazenamento dos dados.

getpass – para esconder senhas no terminal.

os, base64, uuid – utilitários do sistema e geração de chaves.

🛠️ Como Executar
Clone o repositório ou copie os arquivos para seu ambiente:


git clone https://github.com/seuusuario/nome-do-projeto.git
cd nome-do-projeto
Crie um ambiente virtual (opcional, mas recomendado):


python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
Instale a dependência de criptografia:


pip install cryptography
Execute o programa principal:


python main.py
Execute os testes:


python test_sistema.py
🧩 Estrutura de Arquivos

📁 projeto/
├── main.py               # Código principal da aplicação
├── criptografia.py       # Funções de criptografia e descriptografia
├── utils.py              # Funções auxiliares (validação, geração de chaves, etc.)
├── test_sistema.py       # Testes automatizados com unittest
├── dados.json            # Armazena os dados dos usuários criptografados
├── chave.key             # Chave de criptografia (armazenar com segurança)
└── README.md             # Este arquivo
🛡️ Segurança e LGPD
Todos os dados sensíveis são criptografados com AES-256 em repouso.

A senha é criptografada e nunca armazenada em texto puro.

Implementação de autenticação forte com validação de e-mail e senha.

Cumprimento de requisitos da LGPD:

Coleta mínima de dados

Possibilidade de exclusão (direito ao esquecimento)

Controle de acesso por níveis (admin/comum)

Transparência e consentimento

🧠 Contribuições Acadêmicas
Este projeto atende aos tópicos exigidos para o PIM II:

✅ Pensamento Lógico e Computacional com Python

✅ Cibersegurança

✅ LGPD (Lei Geral de Proteção de Dados)

✅ Infraestrutura Computacional (descrito no relatório técnico)