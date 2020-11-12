import json
import requests
import conexao
from datetime import datetime
from time import time, sleep

class ProtocolosCNJ:

    _url = None
    _arquivo = None
    _append_arquivo = False
    _grava_bd = None
    _tribunal = None
    _senha_tribunal = None
    _conexao_selo = None

    def __init__(self, url, arquivo, append_arquivo, grava_bd, tribunal, senha_tribunal):
        self._url = url
        self._arquivo = arquivo
        if arquivo != None:
            self._append_arquivo = append_arquivo
        self._grava_bd = grava_bd
        self._tribunal = tribunal
        self._senha_tribunal = senha_tribunal

        self.__carrega_protocolos_arquivo_anterior()

        if self._grava_bd:
            self._conexao_selo = conexao.get_con_selo_justica()

    def buscar_paginas(self, params):
        params['page'] = 0

        i = 0
        while i < 10:
            try:
                t0 = time()
                headers = requests.utils.default_headers()
                headers['User-Agent'] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'
                r = requests.get(self._url, auth=(self._tribunal, self._senha_tribunal), params=params, timeout=150, headers=headers)
                if r.status_code == requests.codes.ok:
                    total_registros = r.json()['totalRegistros']
                    registros_por_pagina = len(r.json()['resultado'])

                    #Se não tiver registros
                    if total_registros == 0:
                        print('Nenhum registro encontrado para os parâmetros selecionados. Nada a processar.')
                        return {}

                    paginas = int(total_registros / registros_por_pagina) + 1
                    print('Total de registros encontrados: ' + str(total_registros))
                    print('Quantidade de registros retornados por página: ' + str(registros_por_pagina))
                    print('Total de páginas a serem processadas: ' + str(paginas))
                    return {
                        'total_registros' : total_registros,
                        'registros_por_pagina' : registros_por_pagina,
                        'paginas' : paginas
                    }
                else :
                    print('Erro ao tentar definir quantidade de páginas. Tentativa ' + str(i+1) + '/10 em %0.1fs!' % (time() - t0))
            except (requests.exceptions.Timeout):
                print('Erro (timeout) ao tentar definir quantidade de páginas. Tentativa ' + str(i+1) + '/10 em %0.1fs!' % (time() - t0))

            i += 1

        return {}
    
    def executar(self, params, lista_paginas):
        paginas_erro = []
        constante_msg_tempo = ' em %0.1fs!'
        for pagina in lista_paginas:
            params['page'] = pagina
            sleep(5)

            if not self.executar_pagina(params):
                paginas_erro.append(pagina)

            # A cada 30 páginas, imprime as páginas que deram erro para não perder o fio da meada
            if pagina % 30 == 0:
                print('Páginas com erro até aqui: ')
                print(paginas_erro)

        print('Páginas com erro: ')
        print(paginas_erro)
        return paginas_erro

    def executar_pagina(self, params):
        constante_msg_tempo = ' em %0.1fs!'
        pagina = params['page']

        t0 = time()
        try:
            headers = requests.utils.default_headers()
            headers['User-Agent'] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'
            r = requests.get(self._url, auth=(self._tribunal, self._senha_tribunal), params=params, timeout=150, headers=headers)
            if r.status_code == requests.codes.ok:
                if self.__atualiza_protocolos(r.json()):
                    print('Retornou protocolos da página ' + str(pagina) + constante_msg_tempo % (time() - t0))
                else:
                    print('Erro ao gravar protocolos da página ' + str(pagina) + constante_msg_tempo % (time() - t0))
                    return False
            else :
                print('Erro ao buscar página ' + str(pagina) + constante_msg_tempo % (time() - t0))
                return False
        except (requests.exceptions.Timeout):
            print('Erro timeout ao buscar página ' + str(pagina) + constante_msg_tempo % (time() - t0))
            return False
        
        return True


    def __carrega_protocolos_arquivo_anterior(self):

        if self._append_arquivo:
            try:
                with open(self._arquivo) as json_file:
                    self._prot_json = json.load(json_file)
            except FileNotFoundError:
                self._prot_json = {'protocolos' : []}
        else:
            self._prot_json = {'protocolos' : []}

    def __atualiza_protocolos(self, content_json: dict):

        for prot in content_json['resultado']:
            self._prot_json['protocolos'].append(prot)
            if self._grava_bd and not self.__gravar_no_bd(prot):
                return False
            #Só atualiza se houver arquivo definido
            if self._arquivo != None and len(self._arquivo) > 0:
                with open(self._arquivo, 'w') as json_file:
                    json.dump(self._prot_json, json_file)
        
        return True

    def __gravar_no_bd(self, protocolo):
        data_envio = datetime.fromtimestamp(protocolo['datDataEnvioProtocolo']/1000)

        if self.__protocolo_existe_no_bd(protocolo['seqProtocolo']):
            sql = "update selo_justica.tb_protocolo_cnj \n" \
                + "   set num_protocolo = '" + protocolo['numProtocolo'] + "' \n" \
                + "     , hash_arquivo = '" + protocolo['codHash'] + "' \n" \
                + "     , status = '" + str(protocolo['tipStatusProtocolo']) + "' \n" \
                + "     , tam_arquivo = '" + str(protocolo['tamanhoArquivo']) + "' \n" \
                + "     , data_envio = '" + data_envio.strftime('%Y-%m-%d %H:%M:%S') + "' \n" \
                + "     , qtd_processos = " + str(protocolo['qtdProcessosLote']) + "\n" \
                + "     , qtde_processos_sucesso = " + str(protocolo['qtdProcessosSucesso']) + "\n" \
                + "     , qtd_processos_erro = " + str(protocolo['qtdProcessosErro']) + "\n" \
                + " where id_protocolo_cnj = " + str(protocolo['seqProtocolo'])
                
        else:
            sql = "insert into selo_justica.tb_protocolo_cnj " \
                + "(id_protocolo_cnj, num_protocolo, hash_arquivo, status, tam_arquivo, data_envio, qtd_processos" \
                + ", qtde_processos_sucesso, qtd_processos_erro) " \
                + "values (" + str(protocolo['seqProtocolo']) + ", '" \
                + protocolo['numProtocolo'] + "', '" \
                + protocolo['codHash'] + "', '" \
                + str(protocolo['tipStatusProtocolo']) + "', '" \
                + str(protocolo['tamanhoArquivo']) + "', '" \
                + data_envio.strftime('%Y-%m-%d %H:%M:%S') + "', " \
                + str(protocolo['qtdProcessosLote']) + ", " \
                + str(protocolo['qtdProcessosSucesso']) + ", " \
                + str(protocolo['qtdProcessosErro']) + ")"

        if self._conexao_selo.manipular(sql):
            print('Protocolo ' + protocolo['numProtocolo'] + ' inserido/atualizado com sucesso!')
            return True
        else : 
            print('Protocolo ' + protocolo['numProtocolo'] + ' não inserido!')
            return False

    def __protocolo_existe_no_bd(self, id_protocolo_cnj):
        sql = "select 1 from selo_justica.tb_protocolo_cnj where id_protocolo_cnj = " + str(id_protocolo_cnj)
        rs = self._conexao_selo.consultar(sql)

        return (rs != None and len(rs) > 0)


