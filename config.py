import os

class Config(object):
    EMOJIFY_SECRET = os.environ.get('EMOJIFY_SECRET') or 'super-secret-key'
