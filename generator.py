# -*- coding:utf-8 -*-
import getopt

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0
import sys

"""
自动生产supervisor配置文件
python generator.py
"""

__author__ = 'jinlong'
__date__ = '15/10/27'


def generator(app_name):
    """
    根据app_name生产配置文件
    :param app_name:
    :return:
    """
    config = ConfigParser()
    # add a new section and some values
    section_name = 'program:{0}'.format(app_name)
    config.add_section(section_name)
    config.set(section_name, 'command', 'python /usr/local/{0}/{0}.py'.format(app_name))
    config.set(section_name, 'autostart', "true")
    config.set(section_name, 'autorestart', "true")
    config.set(section_name, 'redirect_stderr', "true")
    config.set(section_name, 'user', "root")
    config.set(section_name, 'stdout_logfile', "/data/{0}/log/{0}.log".format(app_name))
    # save to a file
    with open('{0}.ini'.format(app_name), 'w') as configfile:
        config.write(configfile)


def main(argv):
    if not argv:
        usage()
        return
    try:
        opts, args = getopt.getopt(argv, "hn:", ["help"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt == '-n':
            app_name = arg
            generator(app_name)
        else:
            usage()


def usage():
    print "请使用 python generator.py -n app_name 来执行本文件"


if __name__ == "__main__":
    main(sys.argv[1:])
