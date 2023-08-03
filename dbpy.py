import sqlite3

def criar_banco_dados():
    # Conecta ao banco de dados (cria um novo se não existir)
    conexao = sqlite3.connect('usuarios.db')
    cursor = conexao.cursor()

    # Cria a tabela de usuários (se não existir)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            nome TEXT,
            email TEXT
        )
    ''')

    # Insere alguns registros de exemplo
    usuarios = [
        ('Carlos', 'carlos@example.com'),
        ('Gabriel', 'gabriel@example.com'),
        ('Chacal', 'chacal@example.com')
    ]
    cursor.executemany('INSERT INTO usuarios VALUES (?, ?)', usuarios)

    # Salva as alterações e fecha a conexão com o banco de dados
    conexao.commit()
    conexao.close()

def obter_nomes_emails():
    # Conecta ao banco de dados
    conexao = sqlite3.connect('usuarios.db')
    cursor = conexao.cursor()

    # Executa uma consulta para obter os nomes e e-mails
    cursor.execute('SELECT nome, email FROM usuarios')
    registros = cursor.fetchall()

    # Formata os registros em uma string
    resultado = ''
    for nome, email in registros:
        resultado += f'Nome: {nome}\nE-mail: {email}\n\n'

    # Fecha a conexão com o banco de dados
    conexao.close()

    return resultado

# Cria o banco de dados (se ainda não foi criado)
criar_banco_dados()

# Obtém os nomes e e-mails formatados em uma string
nomes_emails = obter_nomes_emails()

# Imprime a string formatada
print(nomes_emails)