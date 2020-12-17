import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_19_8")

dsn_tns = cx_Oracle.makedsn('bd-ora-dev.trt21.local', '1522', service_name='nataldev')
# if needed, place an 'r' before any parameter in order to address special characters such as '\'.

conn = cx_Oracle.connect(user='intra', password='intra21', dsn=dsn_tns)
# if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'

c = conn.cursor()
c.execute('SELECT * FROM intra.TB_TRANSP_ANEXO8_REQUISICAO ORDER BY id')
for row in c:
    print (row[0], '-', row[1]) # this only shows the first two columns. To add an additional column you'll need to add , '-', row[2], etc.
#conn.close()