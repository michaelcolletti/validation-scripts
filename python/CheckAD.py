#!/usr/bin/env python

import schedule
import time
from pyad import *
import os

# Read the sensitive data from environment variables
# 
ldap_server = os.environ.get("LDAP_SERVER")
ldap_username = os.environ.get("LDAP_USERNAME")
ldap_password = os.environ.get("LDAP_PASSWORD")
ad_group_name = os.environ.get("AD_GROUP_NAME")

def check_ad_group():
    # Connect to Active Directory
    pyad.set_defaults(ldap_server=ldap_server)
    pyad.set_defaults(username=ldap_username, password=ldap_password)

    # Search for the AD group
    group = pyad.adgroup.ADGroup.from_cn(ad_group_name)

    # Print the group's members
    print(f"Members of {ad_group_name}:")
    for member in group.get_members():
        print(member)

# Schedule the job to run every day at 9:00 AM
schedule.every().day.at("09:00").do(check_ad_group)

# Run the scheduled job indefinitely
while True:
    schedule.run_pending()
    time.sleep(1)
