#!/usr/bin/env python3.9

import logging
import os

def file_reading(file):
    lines = []
    if(not os.path.isfile(file)):
        logging.error("El archivo no puede ser leído.")
    else:
        file_opened = open(file, 'r')
        for line in file_opened:
            lines.append(line)
            logging.info(line)
        file_opened.close()
    return (lines)