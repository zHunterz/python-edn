"""
Crie um programa que verifique se uma senha é forte. Uma
senha forte deve ter pelo menos 8 caracteres e conter pelo
menos um número. O programa deve continuar pedindo
senhas até que uma válida seja inserida ou o usuário digite
'sair'.
"""

def senha_forte(senha):
    # Verifica se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        return False
    # Verifica se a senha contém pelo menos um número
    if not any(char.isdigit() for char in senha):
        return False
    return True

senha = input("Digite uma senha (ou 'sair' para encerrar): ")
while senha.lower() != 'sair':
    if senha_forte(senha):
        print("Senha forte!")
        break
    else:
        print("Senha fraca. Tente novamente.")
        senha = input("Digite uma senha (ou 'sair' para encerrar): ")
else:
    print("Programa encerrado.")