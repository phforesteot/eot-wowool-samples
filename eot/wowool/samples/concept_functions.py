#  Copyright (c) 2020 EyeOnText, All Rights Reserved.
#  NOTICE:  All information contained herein is, and remains the property of EyeOnText.

from eot.wowool.native import Analyzer, Domain
from eot.wowool.annotation import Concept
from eot.wowool.error import Error

try:
    english = Analyzer(language="dutch")
    entities = Domain( "dutch-entity" )

    doc = english("Jan Van Den Berg en Jeff Jansens.")
    doc = entities(doc)
    print(doc)
    concept_filter = lambda concept : concept.uri == 'Person'
    for person in Concept.iter(doc, concept_filter) :
        print( "flat: ", {**person} )
        print("-"  * 40 )
        print( f"tokens: {person.tokens}" )
        for token in person.tokens:
            print( f"  - stem: {token.stem}, pos: {token.pos}, prop:{token.properties}" )
        print( f"literal: {person.literal}" )
        print( f"offsets: ({person.begin_offset},{person.end_offset})" )
        print( f"attributes: {person.attributes}" )
        print( f"gender: {person.attributes['gender'][0]}" )
        # Accessing sub annotations
        print("-"  * 40 )
        print("- Accessing sub annotations")
        print( f"  person.GivenName :{person.GivenName}")
        print( f"  person.GivenName.literal :{person.GivenName.literal}")
        # Accessing sub annotations
        print("- Accessing sub annotations using find")
        for given in person.find("GivenName"):
            print(f"  person.find(GivenName) :{given.literal}")

    print("-"  * 40 )
    print("- using find " )
    for sentence in doc :
        for pers in sentence.find("Person"):
            print(f"  {pers.literal}")




except Error as ex:
    print("Exception:",ex)
