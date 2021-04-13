from sqlalchemy import Column, String, Table, MetaData, Enum, ForeignKey, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
import models


metadata = MetaData()

users = Table('users', metadata,
              Column('user_id', UUID, primary_key=True, server_default=func.uuid_generate_v1()),
              Column('username', String(20)),
              Column('first_name', String(100)),
              Column('last_name', String(100)),
              Column('hashed_password', String(100)),
              Column('salt', String(64)),
              )


friends = Table('friends', metadata,
                Column('user_id_1', UUID, ForeignKey('users.user_id'), primary_key=True),
                Column('user_id_2', UUID, ForeignKey('users.user_id'), primary_key=True),
                Column('action_user_id', UUID, ForeignKey('users.user_id')),
                Column('relationship', Enum(models.friend_relationship), server_default='pending')
                )


events = Table('events', metadata,
               Column('event_id', UUID, primary_key=True, server_default=func.uuid_generate_v1()),
               Column('name', String),
               Column('creator', UUID, ForeignKey('users.user_id')),
               Column('visibility', Enum(models.event_visibility)),
               Column('time_created', DateTime, server_default=func.now()),
               Column('venue', String),
               Column('time', DateTime)
               )
