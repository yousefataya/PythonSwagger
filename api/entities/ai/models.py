from api.core import Mixin
from ...db import db
from sqlalchemy_utils import UUIDType
import uuid
import datetime
class ArticalInfo(Mixin , db.Model):
    """description of class"""


    __tablename__ = 'atifical_ai'

    id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    articalName= db.Column(db.String , nullable=False)
    writtenDate= db.Column(db.DateTime, default=datetime.datetime.utcnow)
    description = db.Column(db.String , nullable = True)
    notes = db.Column (db.String , nullable = True)
    isExpired = db.Column(db.Boolean , nullable = False , default = False)
    autherCode = db.Column(db.String , nullable = False , unique=True)
    autherName = db.Column(db.String , nullable = False)
    articalCode= db.Column(db.String , nullable = False , unique=True)
    isResereved = db.Column (db.String , nullable = False , default = False )
    reserevedBy = db.Column (db.String , nullable = False)
    publishDate = db.Column (db.DateTime, nullable = False)
    publishingHouse = db.Column (db.String , nullable = False)




