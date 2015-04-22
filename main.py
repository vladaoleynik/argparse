__author__ = 'vladaoleynik'

import argparse
import re


class ValidateInt(argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):
        if type(values) is int:
            print 'Everything is ok. %r - integer.' % values
        else:
            print '%r - is not integer. It\'s a bad sign! :)' % values


class ValidateFloat(argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):
        pattern = '(((-[1-9])([0-9]+)?)|(([1-9]+)?[0-9]))\.[0-9]+'
        if re.match(pattern, values):
            print 'Everything is ok. %r - float.' % values
        else:
            print '%r - is not float. It\'s a bad sign! :)' % values


class ValidateEmail(argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):
        pattern = '^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$'
        if re.match(pattern, values):
            print 'Everything is ok. %r - valid email.' % values
        else:
            print '%r - is not valid email. It\'s a bad sign! :)' % values


class ValidateIsoDate(argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):
        pattern = '((.*)(-[0-9]{8})?)'
        if re.match(pattern, values):
            print 'Everything is ok. %r - valid iso date.' % values
        else:
            print '%r - is not valid iso date. It\'s a bad sign! :)' % values


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--int', dest='checkInt', type=int, action=ValidateInt,
                        help='Check if argument is integer')
    parser.add_argument('--float', dest='checkFloat', action=ValidateFloat,
                        help='Check if argument is float')
    parser.add_argument('--email', dest='checkEmail', action=ValidateEmail,
                        help='Check if argument is valid email')
    parser.add_argument('--date', dest='checkDate', action=ValidateIsoDate,
                        help='Check if argument is valid IsoDate')
    args = parser.parse_args()


