#  Copyright (c) 2020 EyeOnText, All Rights Reserved.
#  NOTICE:  All information contained herein is, and remains the property of EyeOnText.

from eot.wowool.native import PipeLine
from eot.wowool.error import Error

try:
    # pipeline = PipeLine("english,entity,dates")
    # more resent version 2.4.4>= you can add applications
    pipeline = PipeLine("english,entity,dates")
    doc = pipeline("Published on the 3/Nov/2000\n\nJohn Smith was in London on the 20/Sep/2020. He took a cab yesterday to the Victoria station in London")
    print("-" * 80)
    print(doc)
except Error as ex:
    print("Exception:", ex)
