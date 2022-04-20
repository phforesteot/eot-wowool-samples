#  Copyright (c) 2020 EyeOnText, All Rights Reserved.
#  NOTICE:  All information contained herein is, and remains the property of EyeOnText.

from eot.wowool.native import Language, Domain
from eot.wowool.annotation import Concept
from eot.wowool.error import Error

try:
    dutch = Language("dutch")
    entities = Domain("dutch-entity")

    doc = dutch("Jan Van Den Berg werkte als hoofdarts bij Omega Pharma.")
    doc = entities(doc)

    # filter some concepts
    requested_concepts = set(["Person", "Position", "Company"])
    concept_filter = lambda concept: concept.uri in requested_concepts
    for concept in Concept.iter(doc.analysis, concept_filter):
        print(f"literal: {concept.literal:<20}, stem={concept.stem}")
    # flatten concepts into dict
    print("-" * 40)
    for concept in Concept.iter(doc.analysis, concept_filter):
        print({**concept})

    print("-" * 40)
    for person in Concept.iter(doc.analysis, lambda concept: concept.uri == "Person"):
        for person_parts in Concept.iter(person, lambda concept: concept.uri.startswith("Person")):
            print(f"Person: {person_parts.uri:<20}, stem={person_parts.literal}")

    print("-" * 40)
    for concept in doc.analysis.concepts(lambda concept: concept.uri == "Person"):
        print({**concept})
    print("-" * 40)

except Error as ex:
    print("Exception:", ex)
