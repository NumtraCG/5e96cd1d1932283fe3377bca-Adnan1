import sys
import json
import Connectors
import Transformations
import AutoML
try:
    Adnan-1_DBFS = Connectors.DBFSConnector.fetch([], {}, "5e96cd1d1932283fe3377bcb", spark, "{'url': '', 'file_type': 'Delimeted', 'dbfs_token': '', 'dbfs_domain': '', 'delimiter': ',', 'is_header': 'Use Header Line'}")

except Exception as ex:
    print(ex)
try:
    Adnan-1_AutoFE = Transformations.TransformationMain.run(["5e96cd1d1932283fe3377bcb"], {"5e96cd1d1932283fe3377bcb": Adnan-1_DBFS}, "5e96cd1d1932283fe3377bcc", spark, json.dumps({"FE": []}))

except Exception as ex:
    print(ex)
try:
    AutoML.functionClassification(Adnan-1_AutoFE, [], "")

except Exception as ex:
    print(ex)
