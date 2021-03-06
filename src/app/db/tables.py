# Copyright (C) 2021, Pyronear contributors.

# This program is licensed under the Apache License version 2.
# See LICENSE or go to <https://www.apache.org/licenses/LICENSE-2.0.txt> for full license details.


from .session import Base
from .models import (Users, Accesses, Alerts, Devices, Events,
                     Groups, Installations, Media, Sites, Webhooks, EventType, AccessType, SiteType, MediaType)

__all__ = ['metadata', 'users', 'accesses', 'groups', 'sites', 'events',
           'devices', 'media', 'installations', 'alerts', 'webhooks']

users = Users.__table__
accesses = Accesses.__table__
groups = Groups.__table__
sites = Sites.__table__
events = Events.__table__
devices = Devices.__table__
media = Media.__table__
installations = Installations.__table__
alerts = Alerts.__table__
webhooks = Webhooks.__table__

metadata = Base.metadata
