#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module aks for a login."""


import authentication
import getpass


def login(username, maxattempts=3):
    """
    This function prompts a username and password login.

    Args:
        username (str): username of the login
        maxattempts (int): # of attempts default = 3

    Returns:
        bool: True or False

    Examples:
        >>> import task_02
        >>> task_02.login('mike', 4)
        Please enter your password:
        Incorrect username or password. You have 3 attempts left.
        Please enter your password:
        Incorrect username or password. You have 2 attempts left.
        Please enter your password:
        Incorrect username or password. You have 1 attempts left.
        Please enter your password:
        Incorrect username or password. You have 0 attempts left.
        False

        >>> import task_02
        >>> task_02.login('veruca', 2)
        Please enter your password:
        Incorrect username or password. You have 1 attempts left.
        Please enter your password:
        True

    """
    authorization = False
    attempts = 1
    prompt = 'Please enter your password:'
    fail_msg = 'Incorrect username or password. You have {} attempts left.'
    while not authorization and attempts <= maxattempts:
        authorization = authentication.authenticate(username,
                                                    getpass.getpass(prompt))
        if authorization is True:
            authorization = True
        else:
            print fail_msg.format(maxattempts - attempts)
            attempts += 1
    return authorization
