#  Copyright (c) 2020 EyeOnText, All Rights Reserved.
#  NOTICE:  All information contained herein is, and remains the property of EyeOnText.

from eot.wowool.native.core import Language, Domain
from eot.wowool.error import Error
from eot.wowool.annotation import Concept
from eot.wowool.annotation import Token

try:
    analyzer = Language("swedish")
    rule_source ="""
// Compound Sample:
// capture all the word with verzekering
lexicon:(input="component"){
    försäkring } = INSURANCE_COMPONENT;

// capture only the real verzekering not verzekeringsmaatschapijen
lexicon:(input="head"){
    försäkring } = INSURANCE_HEAD;

// capture the cost of the insurance.
rule:{ {h'försäkring'} = INSURANCE_TYPE { Num +currency } = INSURANCE_PRICE };
    """
    compounds = Domain(source=rule_source)
    input = "Det finns försäkringsbolag 40000 euro och försäkring: bilförsäkring 100 euro, cykelförsäkring 200 SEK "
    doc = compounds(analyzer(input))
    print(doc)

    print("-" * 80)
    print(rule_source)
    print("-" * 80)
    print(input)
    print("-" * 80)
    print(f"{'uri':<20s} | {'literal':<30s} | {'stem'}")
    print("-" * 80)
    for concept in Concept.iter(doc, lambda concept : concept.uri == "INSURANCE_COMPONENT" ):
        print(f"{concept.uri:<20s} | {concept.literal:<30s} | {concept.stem}")
    print("-" * 80)
    for concept in Concept.iter(doc, lambda concept : concept.uri == "INSURANCE_HEAD" ):
        print(f"{concept.uri:<20s} | {concept.literal:<30s} | {concept.stem}")
    print("-" * 80)
    for concept in Concept.iter(doc, lambda concept : concept.uri == "INSURANCE_PRICE" or concept.uri == "INSURANCE_TYPE"):
        print(f"{concept.uri:<20s} | {concept.literal:<30s} | {concept.stem}")

except Error as ex:
    print("Exception:",ex)


