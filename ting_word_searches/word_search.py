def exists_word(word, instance):
    """Aqui irá sua implementação"""
    res_busca = []
    # lista vazia para os resultados da busca

    for indice in range(len(instance)):
        # percorre os indices da instancia de dados
        nome_arq = instance.search(indice)["nome_do_arquivo"]
        # define o nome do arquivo, que vem do indice da nusca
        res_busca.append({
            "arquivo": f"{nome_arq}",
            "ocorrencias": [],
            "palavra": word.lower()
        })
        # cria um dicionario com info sobre o arquivo e a palavra buscada
        for indice, line in enumerate(
                instance.search(indice)["linhas_do_arquivo"]):
            # percorre as linhas do arquivo correspondente ao i da busca
            if word in line.lower():
                # verifica se a palavra buscada esta presente na linha
                # ela é convertida para caixa baixa
                res_busca[len(res_busca) - 1]["ocorrencias"].append({
                    "linha": indice + 1
                })
                # Add um dicionário representando a ocorrencia
                # da palavra na linha atual a lista de ocorrencias do arquivo

    if len(res_busca) == 0:
        return []
    #  Verifica se não houve nenhuma ocorrencia da palavra buscada

    return [i for i in res_busca if len(i["ocorrencias"]) > 0]
    # Retorna uma lista contendo os resultados da busca,
    # excluindo aqueles em que não houve ocorrencias da palavra.


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
