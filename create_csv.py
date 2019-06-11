#!/usr/bin/env python
import sys
import random
if __name__ == "__main__":
    suffix = random.randint(1000,9999)
    name= "pnp-{}".format(suffix)
    serial = "223344a{}".format(suffix)
    print("""name,serial,pid,siteName,templateName,hostname,loopback
{},{},WS-C3650,Global/EU/Barcelona,basic,pnp-stack,10.10.100.200""".format(name, serial))
