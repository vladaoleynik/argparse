__author__ = 'vladaoleynik'

import argparse
import re


# super class
class Validate(object):

    def __call__(self, parser, namespace, values):
        if re.match(self.pattern, values):
            print 'Everything is ok. %s - %s.' % (values, self.element)
        else:
            print '%s - is not %s. It\'s a bad sign! :)' % (values, self.element)


class ValidateInt(Validate, argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):
        # regular expression for integer
        self.pattern = '^[-]*[1-9]\d*$'
        self.element = 'integer'
        super(ValidateInt, self).__call__(parser, namespace, values)


class ValidateFloat(Validate, argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):
        # regular expression for float
        self.pattern = '(((-[1-9])([0-9]+)?)|(([1-9]+)?[0-9]))\.[0-9]+'
        self.element = 'float'
        super(ValidateFloat, self).__call__(parser, namespace, values)


class ValidateEmail(Validate, argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):
        # regular expression for email
        self.pattern = '^[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}$'
        self.element = 'valid email'
        super(ValidateEmail, self).__call__(parser, namespace, values)


class ValidateIsoDate(Validate, argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):
        # regular expression for iso date
        # YYYY-MM-DD
        self.pattern = '([0-9]{4})-([0-9]{1,2})-([0-9]{1,2})'
        self.element = 'iso date'
        super(ValidateIsoDate, self).__call__(parser, namespace, values)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--int', dest='checkInt', action=ValidateInt,
                        help='Check if argument is integer')
    parser.add_argument('--float', dest='checkFloat', action=ValidateFloat,
                        help='Check if argument is float')
    parser.add_argument('--email', dest='checkEmail', action=ValidateEmail,
                        help='Check if argument is valid email')
    parser.add_argument('--date', dest='checkDate', action=ValidateIsoDate,
                        help='Check if argument is valid IsoDate')
    args = parser.parse_args()


