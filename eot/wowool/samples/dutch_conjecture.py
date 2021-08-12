#  Copyright (c) 2020 EyeOnText, All Rights Reserved.
#  NOTICE:  All information contained herein is, and remains the property of EyeOnText.

from eot.wowool.native import Analyzer, Domain
from eot.wowool.error import Error

try:
    dutch = Analyzer(language="dutch")
    entities = Domain( "dutch-entity" )

    conjecture = Domain(source="""


namespace conjecture {

    rule :
    {
        'het' { <> }= Info
        'bedrijf'
        {(Prop)+} = Company@(info=f"{rule.Info.stem().upper()}")
    };
}
    """)

    doc = dutch("Het Vlaams bedrijf NietGekent werkt samen met EyeOnText.")
    doc = entities(doc)
    doc = conjecture(doc)
    # doc = conjecture(entities(dutch("Het Vlaams bedrijf NietGekent werkt samen met EyeOnText.")))
    print(doc)
except Error as ex:
    print("Exception:",ex)


