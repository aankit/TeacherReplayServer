from sqlalchemy import Column, ForeignKey, Integer, String, Table, Text, DateTime, Interval
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from replaydb.database import Base

category_replay = Table('category_replay', Base.metadata,
        Column('category_id', Integer, ForeignKey('category.id'), nullable=False),
        Column('replay_id', Integer, ForeignKey('replay.id'), nullable=False))

class Time(Base):
    __tablename__ = 'time'
    id = Column(Integer, primary_key=True)
    day = Column(String(10), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    section_id = Column(Integer, ForeignKey('section.id'), nullable=False)
    section = relationship('Section', backref='times')

    def __repr__(self):
        return '<Time {}>'.format(self.start_time)

class Section(Base):
    __tablename__ = 'section'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)

    def __repr(self):
        return '<Section {}>'.format(self.class_name)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    section_id = Column(Integer, ForeignKey('section.id'), nullable=False)
    section = relationship('Section', backref='times')

    def __repr__(self):
        return '<User {}>'.format(self.name)

class Marker(Base):
    __tablename__ = 'marker'
    id = Column(Integer, primary_key=True)
    time = Column(DateTime, nullable=False)
    duration = Column(DateTime, nullable=False)
    mode = Column(Integer, nullable=False)
    raw_video_id = Column(Integer, ForeignKey('raw_video.id'), nullable=False)

class RawVideo(Base):
    __tablename__ = 'raw_video'
    id = Column(Integer, primary_key=True)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    time_id = Column(Integer, ForeignKey('time.id'), nullable=False)

class Replay(Base):
    __tablename__ = 'replay'
    id = Column(Integer, primary_key=True)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    time_id = Column(Integer, ForeignKey('time.id'), nullable=False)

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    category = Column(String(200), nullable=False)
    replays = relationship('Replay', backref='categories', secondary='category_replay')

    def __repr(self):
        return '<Category {}>'.format(self.category)










