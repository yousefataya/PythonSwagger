from flask_sqlalchemy import SQLAlchemy

# instantiate database object
db = SQLAlchemy()

from sqlalchemy import create_engine
import cx_Oracle

host='localhost'
port=1521
sid='ORCL'
user='purpose'
password='opc@2020'
sid = cx_Oracle.makedsn(host, port, sid=sid)

cstr = 'oracle+cx_oracle://{user}:{password}@{sid}'.format(
    user=user,
    password=password,
    sid=sid
)

engine = create_engine(
    cstr,
    convert_unicode=False,
    pool_recycle=10,
    pool_size=50,
    echo=True
)
