from api.core import Mixin
from ..db import db  
class User(Mixin, db.Model):
    """User Table."""

    __tablename__ = "user"

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
import uuid
class ArticalInfo(Mixin , db.Model):
    """description of class"""
    __tablename__ = 'select_info'

    id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    articalName= db.Column(db.String , nullable=False)
    writtenDate= db.Column(db.DateTime , nullable = False)
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

from api.core import Mixin
from sqlalchemy_utils import UUIDType
class Urls(Mixin , db.Model):
    """description of class"""
    __tablename__ = 'url_info'

    id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    urlLink = db.Column (db.String , nullable = False)
    createdDate = db.Column(db.DateTime ,  nullable = False)
    isExpired = db.Column(db.Boolean , nullable = False , default = False)
    Description= db.Column(db.String , nullable = True)
    notes = db.Column(db.String , nullable = True)

from api.core import Mixin
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy import UniqueConstraint
from sqlalchemy_utils import UUIDType
from sqlalchemy.ext.automap import automap_base
import uuid
class CronJob(Mixin , db.Model):
    """description of class"""
    __tablename__ = 'cron_job_info'
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
class JobLookup(Mixin , db.Model):
    """description of class"""
    __tablename__ = 'cron_job_lookup'
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
class FetchNewsEntity(Mixin , db.Model):
    """description of class"""
    __tablename__ = 'fetch_api_info'
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    newsName= Column(String , nullable = False)
    newsTitle = Column (String , nullable = False , unique = True)
    newsText = Column( DateTime , nullable = False)
    status= Column(db.Boolean , nullable = False , default = False)
    createdDate = Column (DateTime , nullable = False)
    Description =Column ( String , nullable = True)
    Notes = Column (String , nullable = True)

from api.core import Mixin
from sqlalchemy.ext.declarative import declarative_base
Base = automap_base()
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy import UniqueConstraint
from sqlalchemy_utils import UUIDType
from sqlalchemy.ext.automap import automap_base
class NewsLookupEntity(Mixin , db.Model):
    """description of class"""
    __tablename__ = 'news_lookup'
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
class ArticalHistoryInfo(Mixin , db.Model):
    """description of class"""
    __tablename__ = 'transaction_history_info'

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    articalName= Column(String , nullable=False)
    writtenDate= Column(DateTime, default=datetime.datetime.utcnow)
    description = Column(String , nullable = True)
    notes = Column (String , nullable = True)
    isExpired = Column(db.Boolean , nullable = False , default = False)
    autherCode = Column(String , nullable = False , unique=True)
    autherName = Column(String , nullable = False)
    articalCode= Column(String , nullable = False , unique=True)
    isResereved = Column (String , nullable = False , default = False )
    reserevedBy = Column (String , nullable = False)
    publishDate = Column (DateTime, nullable = False)
    publishingHouse = Column (String , nullable = False)

from api.core import Mixin
from sqlalchemy.ext.declarative import declarative_base
Base = automap_base()
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy import UniqueConstraint
from sqlalchemy_utils import UUIDType
from sqlalchemy.ext.automap import automap_base
class HistoryLookupEntity(Mixin , db.Model):
    """description of class"""
    __tablename__ = 'history_lookup'
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
class HistoryNewsInfo(Mixin , db.Model):
    """description of class"""
    __tablename__ = 'history_info'
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    newsName= Column(String , nullable = False)
    newsTitle = Column (String , nullable = False , unique = True)
    newsText = Column( DateTime , nullable = False)
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
class ImageEntity(Mixin , db.Model):
    """description of class"""
    __tablename__ = 'image_info'
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    imageName= Column(String , nullable = False)
    imageTitle = Column (String , nullable = False , unique = True)
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
class TopicInfo(Mixin , db.Model):
    """description of class"""
    __tablename__ = 'topic_info'

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
from sqlalchemy_utils import UUIDType
import datetime
import uuid
from sqlalchemy.ext.automap import automap_base
class EntityKeywordsInfo(Mixin , db.Model):
    """description of class"""
    __tablename__ = 'keyword_info'

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
class SubjectInfo(Mixin , db.Model):
    """description of class"""
    __tablename__ = 'subject_info'

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    keywork = Column (String , nullable = False)
    createdDate = Column(DateTime ,  default=datetime.datetime.utcnow)
    isExpired = Column(db.Boolean , nullable = False , default = False)
    Description= Column(String , nullable = True)
    notes = Column(String , nullable = True)