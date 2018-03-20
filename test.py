#!/usr/bin/python

import logger
import logging
import requests

logger.debug('123')
logger.error('Failed...')

logger.cprint(logger.LIGHT_CYAN, 'cprint!')

logging.debug('debug 123')
#logging.info('info 123')
#logging.warning('warning 123')

import urllib2

url = 'http://10.88.15.168:9200/File/FileDownloadService.aspx?locationID=7&fileID=d08ede40-4fe5-4ebf-b548-b3225ea815bf'
file_name = urllib2.unquote(url).decode('utf8').split('/')[-1]
print(file_name)

r = requests.get(url, stream=True)
#print r.headers['Location']
print r.headers["Content-Length"]
