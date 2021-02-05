#!/usr/bin/env python
"""Working with nested data hands-on exercise / coding challenge."""

import json
import os
from pprint import pprint


# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, "programminghistorian2.json")) as file:
    # TODO: Parse the contents of the JSON file into a variable
    json_text=  file.read()

print ("json_text is a", type(json_text))
print(json_text)

json_data = json.loads(json_text)

print("json_data is a", type(json_data))
pprint(json_data)
