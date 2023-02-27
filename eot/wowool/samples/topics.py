#  Copyright (c) 2020 EyeOnText, All Rights Reserved.
#  NOTICE:  All information contained herein is, and remains the property of EyeOnText.
#  requirements.txt
#
from eot.wowool.error import Error
from eot.wowool.topic_identifier import TopicIdentifier
from eot.wowool.document import Document

try:
    topic_it = TopicIdentifier(language="english")
    doc = Document( "Every bamboo cut down is re-planted and excess material is used to heat up the factory." )
    doc = topic_it( doc )
    print(doc.results(TopicIdentifier.ID))
except Error as ex:
  print("Exception:",ex)