from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for i in range(0, len(instance)):
        # loop que irá iterar sobre os valores de i
        # no intervalo de 0 até o comprimento de "instance".
        if path_file == instance.search(i)["nome_do_arquivo"]:
            # verifica se o valor de path_file e igual ao
            # instance.search(i). Se for verdadeiro,
            # vai retornar None.
            return None
        # Deve-se ignorar arquivos que já tenham sido processados
        # anteriormente (ou seja, arquivos com o mesmo nome e caminho
        # (nome_do_arquivo) não devem ser readicionados a fila)

    # dicionario com os nomes retirados do readme
    readme = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file),
    }

    instance.enqueue(readme)
    # adiciona o dicionário readme à instance

    print(readme)
    # imprime no console


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
