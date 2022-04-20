#  Copyright (c) 2020 EyeOnText, All Rights Reserved.
#  NOTICE:  All information contained herein is, and remains the property of EyeOnText.

from eot.wowool.native import Language, Domain
from eot.wowool.annotation import Concept
from eot.wowool.error import Error
from eot.wowool.tool.entity_graph import EntityGraph

# fmt: off
graph_config = {
  "slots" : { "USER" : { "uri":"USER" }, "Document" : {} },
  "links" : [
          {   "from"      : { "uri" : "Person"  , "attributes" : ["gender"]  },
              "to"        : { "uri" : "Company" , "attributes" : ["country"] } ,
              "relation"  : { "label": "P2C" }
          }
          ,
          {   "from"      : { "uri" : "Person" },
              "to"        : { "uri" : "Company"},
              "relation"  : { "uri" : "Position" , "label" :"stem" }
          }
          ,
          {   "from"      : { "slot" : "USER" ,  "label": "USER"},
              "to"        : { "uri" : "Person"},
              "relation"  : { "label": "Mentions"  }
          },
          {   "from"      : { "uri" : "USER" },
              "to"        : { "slot" : "Document", "label": "Document"} ,
              "relation"  : { "label": "Mentions"  }
          }
      ]
}

# fmt: on
try:
    english = Language("dutch")
    entities = Domain("dutch-entity")
    myrule = Domain(source=""" rule:{ 'user' '\:' {(<>)+}=USER }; """)
    doc = english("user:John \n\nJan Van Den Berg werkte als hoofdarts bij Omega Pharma.")
    doc = entities(doc)
    doc = myrule(doc)
    graphit = EntityGraph(graph_config)
    graphit.slots["Document"] = {"data": "hello"}
    doc = graphit(doc)

    results = doc.entity_graph.merge()

    print('-' * 80)
    print(f'relations : {results.headers}')
    print('-' * 80)
    for relation in results.rows:
        print(relation)

    print('-' * 80)
    print('neo4j output:')
    print('-' * 80)
    from eot.wowool.tool.entity_graph.cypher import CypherStream

    cs = CypherStream("EOT")
    for neo4j_query in cs(doc.entity_graph):
        print(neo4j_query)

except Error as ex:
    print("Exception:", ex)
