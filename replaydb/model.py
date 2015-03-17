from sqlalchemy import Column, ForeignKey, Integer, String, Table, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from replaydb.database import Base

replay_goals = Table('replay_goals', Base.metadata,
        Column('goal_id', Integer, ForeignKey('goal.id'), nullable=False),
        Column('replay_id', Integer, ForeignKey('replay.id'), nullable=False))

replay_outcome = Table('replay_outcome', Base.metadata,
        Column('outcome_id', Integer, ForeignKey('outcome.id'), nullable=False),
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
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', backref='times')

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
    record_id = Column(Integer, ForeignKey('record.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', backref='markers')

    def __repr__(self):
        return '<Marker(time=%s, mode=%s>' %(self.time, self.mode)

class Record(Base):
    __tablename__ = 'record'
    id = Column(Integer, primary_key=True)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    time_id = Column(Integer, ForeignKey('time.id'), nullable=False)
    time = relationship('Time', backref='records')

class Replay(Base):
    __tablename__ = 'replay'
    id = Column(Integer, primary_key=True)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    time_id = Column(Integer, ForeignKey('time.id'), nullable=False)
    section_id = Column(Integer, ForeignKey('section.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    time = relationship('Time', backref='replays')
    section = relationship('Section', backref='replays')
    user = relationship('User', backref='replays')
    goals = relationship('Goals', backref='replays', secondary='replay_goals')

    def __repr__(self):
        return '<Replay(section=%s, time_id=%s)>' %(self.section_id, time_id)

class Goal(Base):
    __tablename__ = 'goal'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    group = Column(String(100))

    def __repr__(self):
        return '<Goal {}>'.format(self.name)

class Outcome(Base):
    __tablename__ = 'outcome'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    group = Column(String(100))

    def __repr__(self):
        return '<Outcome {}>'.format(self.name)

class Holiday(Base):
    __tablename__ = 'holiday'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)

    def __repr__(self):
        return '<Holiday(name=%s)>' %(self.name)
