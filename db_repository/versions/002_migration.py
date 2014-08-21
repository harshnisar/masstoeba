from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
eng_orphanage = Table('eng_orphanage', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('sentence', String(length=200)),
    Column('score', Integer),
    Column('role', SmallInteger, default=ColumnDefault(0)),
    Column('crowd_score', Integer),
    Column('status', SmallInteger),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['eng_orphanage'].columns['crowd_score'].create()
    post_meta.tables['eng_orphanage'].columns['status'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['eng_orphanage'].columns['crowd_score'].drop()
    post_meta.tables['eng_orphanage'].columns['status'].drop()
