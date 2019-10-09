#!/usr/bin/python3
"""
This is the "to json string" module.

The to json string module defines one function, to_json_string().
"""


def to_json_string(my_obj):
    """Return the JSON representation of an object."""
    import json
    return json.dumps(my_obj)
