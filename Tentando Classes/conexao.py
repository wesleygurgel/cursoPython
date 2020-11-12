import psycopg2

SELO_JUSTICA = {
    'mhost' : 'srv-bd-natal-a.trt21.local', 
    'db' : 'selo_justica', 
    'usr' : 'usr_app_selo_justica', 
    'pwd' : 'eN410k4n0s-prd',
    'port' : 5440,
}

def get_con_selo_justica():
    return Conexao(**SELO_JUSTICA)

class Conexao(object):
    _db=None    
    def __init__(self, mhost, db, usr, pwd, port):
        self._db = psycopg2.connect(host=mhost, database=db, user=usr,  password=pwd, port=port)
    def manipular(self, sql):
        try:
            cur=self._db.cursor()
            cur.execute(sql)
            cur.close();
            self._db.commit()
        except:
            return False;
        return True;
    def consultar(self, sql):
        rs=None
        try:
            cur=self._db.cursor()
            cur.execute(sql)
            rs=cur.fetchall();
        except:
            return None
        return rs
    def proximaPK(self, tabela, chave):
        sql='select max('+chave+') from '+tabela
        rs = self.consultar(sql)
        pk = rs[0][0]  
        return pk+1
    def fechar(self):
        self._db.close()