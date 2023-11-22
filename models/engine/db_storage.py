#!/usr/bin/python3
"""DataBase Engine"""

from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate objects created from DBStorage class """

        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                                           HBNB_MYSQL_USER,
                                           HBNB_MYSQL_PWD,
                                           HBNB_MYSQL_HOST,
                                           HBNB_MYSQL_DB
                                       ), pool_pre_ping=True)


        if HBNB_ENV == "test":
            Base.metadate.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session (self.__session) all
           objects depending of the class name (argument cls)
        """
        n_dict = {}
        classes = {"Amenity": Amenity, "City": City,
                  "Place": Place, "Review": Review, "State": State, "User": User}
        for cl in classes.keys():
            if not cls or cls == cl or cls == classes[cl]:
                objects = self.__session.query(classes[cl]).all()
                for obj in objects:
                    key = obj.__class__.__name__ + "." + str(obj.id)
                    n_dict[key] = obj
        return (n_dict)
    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)
    def save(self):
        """ commit all changes of the current database session"""
        self.__session.commit()
    def delete(self, obj=None):
        """delete from the current database session"""
        if obj:
            self.__session.delete(obj)
    def reload(self):
        """ query data from the database"""
        Base.metadata.create_all(self.__engine)
        session_maker = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_maker)
        self.__session = Session()
    def close(self):
        """Handle remove method"""
        self.__session.remove()
