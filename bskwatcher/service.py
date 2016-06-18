# coding=utf-8


from django.conf import settings
import beanstalkc


bsc_client = beanstalkc.Connection(host=settings.BEANSTALKD_HOST, port=settings.BEANSTALKD_PORT)


def server_stat():
	"""服务器总的运行状态,比如
		tube的状态,jobs消费的状态,jobs投递的状态
	"""
	return bsc_client.stats()
