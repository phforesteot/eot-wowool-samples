#  Copyright (c) 2020 EyeOnText, All Rights Reserved.
#  NOTICE:  All information contained herein is, and remains the property of EyeOnText.

from eot.wowool.native.core import Language, Domain
from eot.wowool.annotation import Concept
from eot.wowool.error import Error
from eot.io import InputProviders
from eot.wowool.entity_mapper import EntityMapper
try:
    dutch = Language("dutch")
    entities = Domain( "dutch-entity" )

    doc = dutch("Jan Van Den Berg werkte als hoofdarts bij Omega Pharma.")
    doc = entities(doc)

    mapper = EntityMapper(  lhs = 'Person', rhs = [ 'Position', 'Company' ] )
    doc = mapper(doc )
    print( doc.results(EntityMapper.ID) )

except Error as ex:
    print("Exception:",ex)
