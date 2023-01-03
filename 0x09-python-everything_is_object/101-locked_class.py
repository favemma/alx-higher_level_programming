#!/usr/bin/python3
class LockedClass:
    """A locked class that only lets the user dynamically create the instance
        attribute 'first_name'"""
    ___slots__ = ['first_name']
    def __init__(self):
        pass
