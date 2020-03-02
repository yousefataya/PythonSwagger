from api.core import Mixin
from ...db import db 
class UserToken(Mixin, db.Model):
    """User Table."""

    __tablename__ = "user_tokens_auths"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    first_name = db.Column(db.String, nullable=False, default='')
    last_name = db.Column(db.String, nullable=False, default='')
    login = db.Column(db.String, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    street = db.Column(db.String, nullable=True)
    city = db.Column(db.String, nullable=True)
    zip = db.Column(db.String, nullable=True)

    def __init__(self, email, password, name):
        if name:
            res = name.split(' ')
            self.first_name = '' if len(res) == 1 else res[0]
            self.last_name = res[0] if len(res) == 1 else ' '.join(res[1:])
        self.last_name = None
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name}>"


import uuid
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy_utils import UUIDType
import datetime
import uuid
class OperationJwtAllowed(Mixin , db.Model):
    """description of class"""
    __tablename__ = 'operations_based_role'

    id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    operationName= db.Column(db.String , nullable=False)
    createDate= db.Column(db.DateTime , nullable = False , default=datetime.datetime.utcnow)
    description = db.Column(db.String , nullable = True)
    notes = db.Column (db.String , nullable = True)
    isExpired = db.Column(db.Boolean , nullable = False , default = False)
    userCode = db.Column(db.String , nullable = False , unique=True)
    userName = db.Column(db.String , nullable = False)
    operationCode= db.Column(db.String , nullable = False , unique=True)
    isResereved = db.Column (db.String , nullable = False , default = False )
    reserevedBy = db.Column (db.String , nullable = False)
    isAllow = db.Column (db.Boolean, nullable = False)
    isPermit = db.Column (db.Boolean , nullable = False)

from api.core import Mixin
from sqlalchemy_utils import UUIDType
import datetime
class UrlsPatterns(Mixin , db.Model):
    """description of class"""
    __tablename__ = 'url_patterns_auth'

    id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    urlLink = db.Column (db.String , nullable = False)
    createdDate = db.Column(db.DateTime ,  nullable = False , default=datetime.datetime.utcnow)
    isExpired = db.Column(db.Boolean , nullable = False , default = False)
    controller= db.Column (db.String , nullable = False)
    method= db.Column (db.String , nullable = False)
    Description= db.Column(db.String , nullable = True)
    notes = db.Column(db.String , nullable = True)

from api.core import Mixin
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy import UniqueConstraint
from sqlalchemy_utils import UUIDType
from sqlalchemy.ext.automap import automap_base
import uuid
class JwtTokenCronJob(Mixin , db.Model):
    """description of class"""
    __tablename__ = 'token_jwt_cron_jobs'
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    jobName= Column(String , nullable = False)
    JobCode = Column (String , nullable = False , unique = True)
    startDate = Column( DateTime , nullable = False)
    status= Column(db.Boolean , nullable = False , default = False)
    createdDate = Column (DateTime , nullable = False)
    cronExpression=Column ( String , nullable = False)

from api.core import Mixin
from sqlalchemy.ext.declarative import declarative_base
Base = automap_base()
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy import UniqueConstraint
from sqlalchemy_utils import UUIDType
from sqlalchemy.ext.automap import automap_base
class JwtTokenLookup(Mixin , db.Model):
    """description of class"""
    __tablename__ = 'token_lookup'
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    lookupKey= Column(String , nullable = False)
    lookupValue = Column(String , nullable = False)


from api.core import Mixin
from sqlalchemy.ext.declarative import declarative_base
Base = automap_base()
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy import UniqueConstraint
from sqlalchemy_utils import UUIDType
from sqlalchemy.ext.automap import automap_base
import uuid
import datetime
class JwtUserHistory(Mixin , db.Model):
    """description of class"""
    __tablename__ = 'jwt_user_history'
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    jwtName= Column(String , nullable = False)
    jwtCode = Column (String , nullable = False , unique = True)
    jwtKey = Column( DateTime , nullable = False)
    status= Column(db.Boolean , nullable = False , default = False)
    createdDate = Column (DateTime , nullable = False , default=datetime.datetime.utcnow)
    Description =Column ( String , nullable = True)
    Notes = Column (String , nullable = True)

from api.core import Mixin
from sqlalchemy.ext.declarative import declarative_base
Base = automap_base()
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy import UniqueConstraint
from sqlalchemy_utils import UUIDType
from sqlalchemy.ext.automap import automap_base
class JwtTransactionLookup(Mixin , db.Model):
    """description of class"""
    __tablename__ = 'transaction_lookup'
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    lookupKey= Column(String , nullable = False)
    lookupValue = Column(String , nullable = False)

from api.core import Mixin
from sqlalchemy.ext.declarative import declarative_base
Base = automap_base()
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy import UniqueConstraint
from sqlalchemy_utils import UUIDType
import uuid
import datetime
from sqlalchemy.ext.automap import automap_base
class JwtHistoryToken(Mixin , db.Model):
    """description of class"""
    __tablename__ = 'transaction_history_token'

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    jwtCode= Column(String , nullable=False)
    jwtDate= Column(DateTime, default=datetime.datetime.utcnow)
    description = Column(String , nullable = True)
    notes = Column (String , nullable = True)
    isExpired = Column(db.Boolean , nullable = False , default = False)
    jwtName = Column(String , nullable = False , unique=True)
    jwtKey = Column(String , nullable = False)
    jwtOperationName= Column(String , nullable = False , unique=True)
    isResereved = Column (String , nullable = False , default = False )
    reserevedBy = Column (String , nullable = False)
    operationCode = Column (DateTime, nullable = False)
    operationGuid = Column (String , nullable = False)

from api.core import Mixin
from sqlalchemy.ext.declarative import declarative_base
Base = automap_base()
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy import UniqueConstraint
from sqlalchemy_utils import UUIDType
from sqlalchemy.ext.automap import automap_base
class JwtTokenSignatureLookup(Mixin , db.Model):
    """description of class"""
    __tablename__ = 'jwt_token_signature_lookup'
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    lookupKey= Column(String , nullable = False)
    lookupValue = Column(String , nullable = False)


from api.core import Mixin
from sqlalchemy.ext.declarative import declarative_base
Base = automap_base()
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy import UniqueConstraint
from sqlalchemy_utils import UUIDType
from sqlalchemy.ext.automap import automap_base
import datetime
import uuid
class JwtTokenSignature(Mixin , db.Model):
    """description of class"""
    __tablename__ = 'jwt_token_signature'
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    signatureName= Column(String , nullable = False)
    signCode = Column (String , nullable = False , unique = True)
    signKey = Column( String , nullable = False)
    status= Column(db.Boolean , nullable = False , default = False)
    createdDate = Column (DateTime , nullable = False , default=datetime.datetime.utcnow)
    Description =Column ( String , nullable = True)
    Notes = Column (String , nullable = True)


from api.core import Mixin
from sqlalchemy.ext.declarative import declarative_base
Base = automap_base()
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy import UniqueConstraint
from sqlalchemy.ext.automap import automap_base
from sqlalchemy_utils import UUIDType
import datetime
import uuid
class JwtTokenTransactions(Mixin , db.Model):
    """description of class"""
    __tablename__ = 'jwt_token_transaction'
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    tansactionCode= Column(String , nullable = False)
    tansactionKey = Column (String , nullable = False , unique = True)
    status= Column(db.Boolean , nullable = False , default = False)
    createdDate = Column (DateTime , nullable = False , default=datetime.datetime.utcnow)
    Description =Column ( String , nullable = True)
    Notes = Column (String , nullable = True)


from api.core import Mixin
from sqlalchemy.ext.declarative import declarative_base
Base = automap_base()
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy import UniqueConstraint
from sqlalchemy_utils import UUIDType
import datetime
import uuid
from sqlalchemy.ext.automap import automap_base
class JwtTokenExpire(Mixin , db.Model):
    """description of class"""
    __tablename__ = 'token_jwt_expire'

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    jwtCode = Column (String , nullable = False)
    createdDate = Column(DateTime ,  default=datetime.datetime.utcnow)
    isExpired = Column(db.Boolean , nullable = False , default = False)
    Description= Column(String , nullable = True)
    notes = Column(String , nullable = True)
from api.core import Mixin
from sqlalchemy.ext.declarative import declarative_base
Base = automap_base()
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy import UniqueConstraint
from sqlalchemy_utils import UUIDType
import datetime
import uuid
from sqlalchemy.ext.automap import automap_base
class JwtTokenExpireLookup(Mixin , db.Model):
    """description of class"""
    __tablename__ = 'token_jwt_expire_lookup'

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    keywork = Column (String , nullable = False)
    createdDate = Column(DateTime ,  default=datetime.datetime.utcnow)
    isExpired = Column(db.Boolean , nullable = False , default = False)
    Description= Column(String , nullable = True)
    notes = Column(String , nullable = True)


from api.core import Mixin
from sqlalchemy.ext.declarative import declarative_base
Base = automap_base()
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy import UniqueConstraint
import uuid
from sqlalchemy_utils import UUIDType
import datetime
from sqlalchemy.ext.automap import automap_base
class JwtTokenPermit(Mixin , db.Model):
    """description of class"""
    __tablename__ = 'jwt_token_permit'

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    permitCode = Column (String , nullable = False)
    permitName = Column (String , nullable = False)
    permitKey = Column (String , nullable = False)
    createdDate = Column(DateTime ,  default=datetime.datetime.utcnow)
    isExpired = Column(db.Boolean , nullable = False , default = False)
    Description= Column(String , nullable = True)
    notes = Column(String , nullable = True)