#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  qutrub_config.py
#  

#Database config directory - updated for development use
DB_BASE_PATH = "./data/"
# Logging file
LOGGING_CFG_FILE = "./config/logging.cfg"
LOGGING_FILE = "./logs.txt"
# in developement True in production False
MODE_DEBUG = True
# ~ MODE_DEBUG = False
def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
