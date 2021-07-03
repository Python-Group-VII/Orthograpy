#!/usr/bin/env python3.9

import logging
import os

def file_reading(file):
    lines = []
    if(not os.path.isfile(file)):
        logging.error("El archivo no puede ser leído.")
    else:
        file_opened = open(file, 'r', encoding='utf-8')
        for line in file_opened:
            if(line.endswith('\n')):
                line=line.removesuffix('\n')
            lines.append(line)
        file_opened.close()
    return (lines)