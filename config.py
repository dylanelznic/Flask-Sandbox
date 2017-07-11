class BaseConfig(object):
	SECRET_KEY = 'dummy_key'
	DEBUG = 0

class DevConfig(BaseConfig):
	DEBUG = 1

class ProdConfig(BaseConfig):
	DEBUG = 0