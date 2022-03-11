#  Copyright (c) 2020 EyeOnText, All Rights Reserved.
#  NOTICE:  All information contained herein is, and remains the property of EyeOnText.

from eot.wowool.native import PipeLine
from eot.wowool.error import Error

try:
    # more resent version 2.4.4>= you can add applications, like geotags
    pipeline = PipeLine("english,entity,dates,rules/geotags,app-eot.wowool.tool.geocoordinates.GeoCoordinates")
    doc = pipeline("John Smith was in London on the 3/11/2020. He took a cab yesterday to the Victoria station in London")
    print('-' *80)
    print(doc)
except Error as ex:
    print("Exception:", ex)
