#  Copyright (c) 2020 EyeOnText, All Rights Reserved.
#  NOTICE:  All information contained herein is, and remains the property of EyeOnText.
from eot.wowool.error import Error
from eot.io import InputProviders
import sys


if len(sys.argv) <= 1:
    print("usage: python3 input_providers.py [folder] ")
    exit(-1)


for ip in InputProviders(sys.argv[1], exclude_extensions=['.xml'] ):
    try:
        print(ip.id(), ip.text())
    except Exception as ex:
        print(f"Exception in {ip.id()}")
