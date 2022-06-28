#  Copyright (c) 2020 EyeOnText, All Rights Reserved.
#  NOTICE:  All information contained herein is, and remains the property of EyeOnText.

from eot.wowool.native import PipeLine
from eot.wowool.error import Error
import json

try:
    # more resent version 2.4.4>= you can add applications, like geotags
    pipeline = PipeLine("english,entity,sentiment,sentiments.app")
    doc = pipeline("John Smith and Mary Janssens are nice people. He is liked by a lot of people. But she hated John.")
    print('-' *80)
    print(json.dumps(doc.results("eot_sentiments"), indent=2))
except Error as ex:
    print("Exception:", ex)
