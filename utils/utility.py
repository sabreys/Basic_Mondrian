"""
utility functions
"""
# !/usr/bin/env python
# coding=utf-8


def cmp_str(element1, element2):
    """compare number in str format correctley
    """
    return (int(element1) > int(element2)) - (int(element1) < int(element2))
