class BaseConfig(object):
	SECRET_KEY = 'dummy_key'
	DEBUG = False

class DevConfig(BaseConfig):
	DEBUG = True

class ProdConfig(BaseConfig):
	DEBUG = False