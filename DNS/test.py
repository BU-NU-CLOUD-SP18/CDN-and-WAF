#!/usr/bin/env python3

import json
import logging
import os
import signal
from datetime import datetime
from pathlib import Path
from textwrap import wrap
from time import sleep

zone_file = Path('./zones.txt')

print(zone_file.exists())
