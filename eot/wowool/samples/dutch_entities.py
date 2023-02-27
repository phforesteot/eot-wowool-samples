#  Copyright (c) 2020 EyeOnText, All Rights Reserved.
#  NOTICE:  All information contained herein is, and remains the property of EyeOnText.

from eot.wowool.native.core import Language, Domain
from eot.wowool.error import Error

try:
    dutch = Language("dutch")
    entities = Domain("dutch-entity")

    doc = dutch("Jan Van Den Berg werkte als hoofdarts bij Omega Pharma.")
    doc = entities(doc)

    print(doc)
except Error as ex:
    print("Exception:",ex)
