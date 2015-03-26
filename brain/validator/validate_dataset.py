#!/usr/bin/python

## @validate_dataset.py
#  This script performs validation on the svm data.
import json
import sys
from jsonschema.validators import Draft4Validator
from brain.schema.jsonschema_definition import jsonschema_string

## Class: Validate_Dataset, explicitly inherit 'new-style' class
#
#  Note: this class is invoked within 'base_data.py'
class Validate_Dataset(object):

    ## constructor: saves a subset of the passed-in form data
    def __init__(self, data, svm_session=None):
        self.data        = data
        self.svm_session = svm_session
        self.list_error  = []

    ## validate_label: validate either the dependent variable (observation) label,
    #                  or the independent variable (feature) label.
    def validate_label(self):
        try:
            Draft4Validator(jsonschema_string()).validate({'value': self.data})
        except Exception, error:
            self.list_error.append(str(error))

    ## validate_value: validate the independent variable (feature) value.
    def validate_value(self):
        try:
            float(self.data)
        except Exception, error:
            self.list_error.append(str(error))

    # get_errors: get all current errors.
    def get_errors(self):
        if len(self.list_error) > 0:
            return self.list_error
        else:
            return None
