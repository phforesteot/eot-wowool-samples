#  Copyright (c) 2020 EyeOnText, All Rights Reserved.
#  NOTICE:  All information contained herein is, and remains the property of EyeOnText.

from eot.wowool.native import Language, Domain
from eot.wowool.error import Error

try:
    english = Language("english")
    entities = Domain( "english-entity" )

    conjecture = Domain(source="""


namespace conjecture {

    rule :
    {
        'the' { <> }= Info
        'company'
        {(Prop)+} = Company@(info=f"{rule.Info.stem().upper()}")
    };
}
    """)

    doc = english("The Flemish company NietGekent is located in Antwerp.")
    doc = entities(doc)
    doc = conjecture(doc)
    print(doc)
except Error as ex:
    print("Exception:",ex)


