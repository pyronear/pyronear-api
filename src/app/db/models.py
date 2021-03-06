# Copyright (C) 2021, Pyronear contributors.

# This program is licensed under the Apache License version 2.
# See LICENSE or go to <https://www.apache.org/licenses/LICENSE-2.0.txt> for full license details.

import enum
from .session import Base
from sqlalchemy.sql import func
from sqlalchemy import Column, DateTime, Integer, Float, String, Enum, Boolean, ForeignKey, MetaData
from sqlalchemy.orm import relationship


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    login = Column(String(50), unique=True)
    access_id = Column(Integer, ForeignKey("accesses.id", ondelete="CASCADE"), unique=True)
    created_at = Column(DateTime, default=func.now())

    access = relationship("Accesses", uselist=False, back_populates="user")
    device = relationship("Devices", uselist=False, back_populates="owner")

    def __repr__(self):
        return "<User(login='%s', created_at='%s'>" % (self.login, self.created_at)


class AccessType(str, enum.Enum):
    user: str = 'user'
    admin: str = 'admin'
    device: str = 'device'


class Accesses(Base):
    __tablename__ = "accesses"

    id = Column(Integer, primary_key=True)
    login = Column(String(50), unique=True, index=True)  # index for fast lookup
    hashed_password = Column(String(70), nullable=False)
    scope = Column(Enum(AccessType), default=AccessType.user, nullable=False)
    group_id = Column(Integer, ForeignKey("groups.id", ondelete="CASCADE"), nullable=False)

    user = relationship("Users", uselist=False, back_populates="access")
    device = relationship("Devices", uselist=False, back_populates="access")
    group = relationship("Groups", uselist=False, back_populates="accesses")

    def __repr__(self):
        return "<Access(login='%s', scope='%s', group_id='%s')>" % (self.login, self.scope, self.group_id)


class Groups(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)

    accesses = relationship("Accesses", back_populates="group")
    sites = relationship("Sites", back_populates="group")

    def __repr__(self):
        return "<Group(name='%s')>" % (self.name)


class SiteType(str, enum.Enum):
    tower: str = 'tower'
    station: str = 'station'
    no_alert: str = 'no_alert'


class Sites(Base):
    __tablename__ = "sites"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    group_id = Column(Integer, ForeignKey("groups.id", ondelete="CASCADE"), nullable=False)
    lat = Column(Float(4, asdecimal=True))
    lon = Column(Float(4, asdecimal=True))
    country = Column(String(5), nullable=False)
    geocode = Column(String(10), nullable=False)
    type = Column(Enum(SiteType), default=SiteType.tower)
    created_at = Column(DateTime, default=func.now())

    installations = relationship("Installations", back_populates="site")
    group = relationship("Groups", uselist=False, back_populates="sites")

    def __repr__(self):
        return "<Site(name='%s', group_id='%s', lat='%s', lon='%s', country='%s', geocode='%s', type='%s')>" % (
            self.name, self.group_id, self.lat, self.lon, self.country, self.geocode, self.type)


class EventType(str, enum.Enum):
    wildfire: str = 'wildfire'


class Events(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    lat = Column(Float(4, asdecimal=True))
    lon = Column(Float(4, asdecimal=True))
    type = Column(Enum(EventType), default=EventType.wildfire)
    start_ts = Column(DateTime, default=None, nullable=True)
    end_ts = Column(DateTime, default=None, nullable=True)
    created_at = Column(DateTime, default=func.now())

    alerts = relationship("Alerts", back_populates="event")

    def __repr__(self):
        return "<Event(lat='%s', lon='%s', type='%s')>" % (
            self.lat, self.lon, self.type)


# Linked tables
class Devices(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True)
    login = Column(String(50), unique=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    access_id = Column(Integer, ForeignKey("accesses.id", ondelete="CASCADE"), unique=True)
    specs = Column(String(50))
    software_hash = Column(String(16), default=None, nullable=True)
    angle_of_view = Column(Float(2, asdecimal=True))
    elevation = Column(Float(1, asdecimal=True), default=None, nullable=True)
    lat = Column(Float(4, asdecimal=True), default=None, nullable=True)
    lon = Column(Float(4, asdecimal=True), default=None, nullable=True)
    yaw = Column(Float(1, asdecimal=True), default=None, nullable=True)
    pitch = Column(Float(1, asdecimal=True), default=None, nullable=True)
    last_ping = Column(DateTime, default=None, nullable=True)
    created_at = Column(DateTime, default=func.now())

    access = relationship("Accesses", uselist=False, back_populates="device")
    owner = relationship("Users", uselist=False, back_populates="device")
    media = relationship("Media", back_populates="device")
    alerts = relationship("Alerts", back_populates="device")
    installation = relationship("Installations", back_populates="device")

    def __repr__(self):
        return "<Device(login='%s', owner_id='%s', access_id='%s', specs='%s', software_hash='%s', last_ping='%s')>" % (
            self.login, self.owner_id, self.access_id, self.specs, self.software_hash, self.last_ping)


class MediaType(str, enum.Enum):
    image: str = 'image'
    video: str = 'video'


class Media(Base):
    __tablename__ = "media"

    id = Column(Integer, primary_key=True)
    device_id = Column(Integer, ForeignKey("devices.id"))
    bucket_key = Column(String(100), nullable=True)
    type = Column(Enum(MediaType), default=MediaType.image)
    created_at = Column(DateTime, default=func.now())

    device = relationship("Devices", uselist=False, back_populates="media")
    alerts = relationship("Alerts", back_populates="media")

    def __repr__(self):
        return "<Media(device_id='%s', bucket_key='%s', type='%s'>" % (
            self.device_id, self.bucket_key, self.type)


class Installations(Base):
    __tablename__ = "installations"

    id = Column(Integer, primary_key=True)
    device_id = Column(Integer, ForeignKey("devices.id"))
    site_id = Column(Integer, ForeignKey("sites.id"))
    start_ts = Column(DateTime, nullable=False)
    end_ts = Column(DateTime, default=None, nullable=True)
    is_trustworthy = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())

    device = relationship("Devices", back_populates="installation")
    site = relationship("Sites", back_populates="installations")

    def __repr__(self):
        return "<Installation(device_id='%s', site_id='%s', is_trustworthy='%s'>" % (
            self.device_id, self.site_id, self.is_trustworthy)


class Alerts(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True)
    device_id = Column(Integer, ForeignKey("devices.id"))
    event_id = Column(Integer, ForeignKey("events.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=True)
    media_id = Column(Integer, ForeignKey("media.id"), default=None)
    azimuth = Column(Float(4, asdecimal=True), default=None)
    lat = Column(Float(4, asdecimal=True))
    lon = Column(Float(4, asdecimal=True))
    is_acknowledged = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())

    device = relationship("Devices", back_populates="alerts")
    event = relationship("Events", back_populates="alerts")
    media = relationship("Media", back_populates="alerts")

    def __repr__(self):
        return "<Alert(device_id='%s', event_id='%s', media_id='%s', is_acknowledged='%s'>" % (
            self.device_id, self.event_id, self.media_id, self.is_acknowledged)


class Webhooks(Base):
    __tablename__ = "webhooks"

    id = Column(Integer, primary_key=True)
    callback = Column(String(50), nullable=False)
    url = Column(String(100), nullable=False)

    def __repr__(self):
        return "<Webhook(callback='%s', url='%s'>" % (
            self.callback, self.url)
