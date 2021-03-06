#!/usr/bin/python

'''@validate_dataset

This script performs validation on correpsonding dataset(s).

'''


class Validate_Dataset(object):
    '''Validate_Dataset

    This class provies an interface to validate provided dataset(s) during
    'data_new', and 'data_append' sessions.

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self, data, session_type=None):
        '''@__init__

        This constructor saves a subset of the passed-in form data.

        '''

        self.data = data
        self.session_type = session_type
        self.list_error = []

    def validate_value(self):
        '''@validate_value

        This method validates the independent variable (feature) value(s).

        '''

        try:
            float(self.data)
        except Exception, error:
            self.list_error.append(str(error))

    def get_errors(self):
        '''get_errors

        This method gets all current errors. associated with this class
        instance.

        '''

        if len(self.list_error) > 0:
            return self.list_error
        else:
            return False
