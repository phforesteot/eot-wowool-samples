#  Copyright (c) 2020 EyeOnText, All Rights Reserved.
#  NOTICE:  All information contained herein is, and remains the property of EyeOnText.

from eot.wowool.native.core import PipeLine
from eot.wowool.error import Error
import json

try:
    pipeline_description = "english,entity,topics.app"
    print(f"{pipeline_description=}")
    pipeline = PipeLine(pipeline_description)
    doc = pipeline("NFT scams, toxic mines and lost life savings: the cryptocurrency dream is fading fast")
    print('-' *80)
    print(json.dumps(doc.results("eot_topics"), indent=2))
except Error as ex:
    print("Exception:", ex)
