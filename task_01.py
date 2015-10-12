#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module creates a list of versus matchups for players in a tournament."""


def get_matches(players):
    """
    This function takes players and assigns them to matches in a tournament.

    Args:
        players (str): number of players in the tournament

    Returns:
        str: each match in the tournment

    Examples:
        >>> import task_01
        >>> task_01.get_matches(['Harry', 'Howard', 'Hugh'])
        [('Harry', 'Howard'), ('Harry', 'Hugh'), ('Howard', 'Hugh')]

    """
    matchups = []
    for pool1, match1 in enumerate(players):
        if pool1 < (len(players)-1):
            for pool2, match2 in enumerate(players):
                if pool1 < pool2:
                    matchups.append([match1, match2])
    return matchups
