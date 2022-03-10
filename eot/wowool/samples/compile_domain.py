#  Copyright (c) 2020 EyeOnText, All Rights Reserved.
#  NOTICE:  All information contained herein is, and remains the property of EyeOnText.
from eot.wowool.native import Language, Domain, Compiler
from eot.wowool.annotation import Concept
from eot.wowool.error import Error
from pathlib import Path

this_folder  = Path(__file__).parent
try:
    project_folder = this_folder /'..' / '..' / '..' / 'domains'
    compiler = Compiler()
    compiler.add_file( project_folder / 'helloworld.wow')
    compiler.add_source( """ rule:{ GREETING } = EXTRA_GREETING; """)
    results = compiler.save( project_folder / 'extra_greeting.dom')
    if not results.status:
        print(results)
        exit(-1)

    dutch = Language("dutch")
    helloworld = Domain( project_folder / 'extra_greeting.dom' )

    doc = dutch("greetings world.")
    doc = helloworld(doc)
    print( doc )
except Error as ex:
    print("Exception:",ex)
