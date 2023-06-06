import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if not path_file.endswith('.txt'):
        # Caso a extensão do arquivo seja diferente de .txt,
        # deve ser exibida a mensagem Formato inválido na stderr
        print('Formato inválido', file=sys.stderr)
    try:
        with open(path_file, 'r') as file:
            # A função deve retornar uma lista contendo as linhas do arquivo.
            return file.read().split('\n')
        # .split('\n) é para dividir o arquivo em linhas
    except FileNotFoundError:
        # Caso o arquivo TXT não exista, deve ser exibida a mensagem
        # Arquivo {path_file} não encontrado na stderr,
        # em que {path_file} é o caminho do arquivo;
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
