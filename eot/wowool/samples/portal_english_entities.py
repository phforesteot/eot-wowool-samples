#!/usr/bin/env python3
#  Copyright (c) 2021 EyeOnText, All Rights Reserved.
#  NOTICE:  All information contained herein is, and remains the property of EyeOnText.
from eot.portal.client import Portal, Pipeline
from eot.portal.client import Error

# !!! Note
# Make sure you have the correct api_key and that you have created a pipeline names english-entity

try:

    portal = Portal(api_key="***************")
    english_entities = Pipeline(name="english-entity", portal=portal)
    document =  english_entities("John Smith was in London on the 3/11/2020.")

except Error as ex:
    print("Exception:",ex)

# or using with
try:

    with Portal(api_key="***************"):
        english_entities = Pipeline(name="english-entity")
        document =  english_entities("John Smith was in London on the 3/11/2020.")
        print(document)

except Error as ex:
    print("Exception:",ex)


# or if you have set the environment variable which we recommend.
# EOT_PORTAL_API_KEY
try:

    with Portal():
        english_entities = Pipeline(name="english-entity")
        document =  english_entities("John Smith was in London on the 3/11/2020.")
        print(document)

except Error as ex:
    print("Exception:",ex)
