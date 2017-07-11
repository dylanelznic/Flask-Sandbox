class BaseConfig(object):
	DEBUG = False

class DevConfig(BaseConfig):
	DEBUG = True

class ProdConfig(BaseConfig):
	DEBUG = False