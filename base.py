#!/usr/bin/python

import os
import sys
import logger

PYTHON_BACKUP_DIR = '.py_bak'

def check_result(ret, command = '', exit_on_fail = True, always_print = False):
    msg = ''
    if len(command) > 0:
        msg = '[' + command + '] '
    else:
        msg = '[command] '
    if ret != 0:
        msg += 'Failed!'
        logger.error(msg)
        if exit_on_fail:
            sys.exit(0)
    elif always_print:
        msg += 'Succeed!'
        logger.debug(msg)

def exit_on_fail(ret, msg = ''):
    if ret != 0:
        if len(msg) > 0:
            logger.error(msg)
        sys.exit(0)

def backup(file_name):
    if not os.path.exists(PYTHON_BACKUP_DIR):
        os.mkdir(PYTHON_BACKUP_DIR)
    full_file_name = os.path.abspath(file_name)
    pre_dir = os.getcwd()
    command = 'cd ' + PYTHON_BACKUP_DIR + '; cp -rf ' + full_file_name + ' .; cd ' + pre_dir
    ret = os.system(command)
    check_result(ret, command)
