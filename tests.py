#!/usr/bin/env python3
"""
Author: Gurkirt Singh
Created on 29th April 2019
Please do not distribute it.
"""

import json
import os

# base_dir = '/home/gurkirt/Downloads/read/'


base_dir = './'


def main(annofile):

    with open(annofile, 'r') as f:
        db = json.load(f)

    frames = db['title']
    print(frames.keys())
    print('Number of frames annotated', len(frames.keys()))


