import os
import pandas as pd
import logging
import syslog
import tabula
import sys
import pandas as pd


logger = logging.getLogger()
formatter= logging.Formatter('%(asctime)s -%(lineno)s -%(levelname)s-%(message)s')
logger.setLevel(logging.DEBUG)
fhandler= logging.FileHandler(filename='../airflow/logs/extract.log', mode='w')
fhandler.setFormatter(formatter)
fhandler.setLevel(logging.INFO)
logger.addHandler(fhandler)

class Extractor:

    def __init__(self):
        pass
    def pdf_to_csv(self,pdfstatement,filename):
        # convert PDF into CSV
        tabula.convert_into(pdfstatement, filename, output_format="csv", pages='all')