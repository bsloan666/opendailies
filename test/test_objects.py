from pprint import pprint
from opendailies.archive import Archive
from opendailies.pipeline import Pipeline
from opendailies.daily import Daily

d = Daily('RD9999_comp_v001', '/var/tmp/glatnick.exr', show='MAMA', sequence='RD', shot='9999', role='comp', version='001')
p = Pipeline('jpeg_default')
a = Archive(d,p)

pprint( a.__dict__)
