from dnacentersdk import api
import json
import time
import calendar
from requests.auth import HTTPBasicAuth  

dna = api.DNACenterAPI(base_url='https://sandboxdnac.cisco.com',
                       username='devnetuser', password='Cisco123!', verify=False)


##### NETWORKS AND SITES ####

# Print Site Topology
sites = dna.topology.get_site_topology()
for site in sites.response.sites:
    if site.parentId == '5f03d9a9-33df-450e-b0c3-6bcb5f721688':
        print(site.name)
        for child_sites in sites.response.sites:
            if child_sites.parentId == site.id:
                print(f'  {child_sites.name}')
            for more_children in sites.response.sites:
                if more_children.parentId == child_sites.id and child_sites.parentId == site.id:
                    print(f'    {more_children.name}')
    print(' ')

# Print Vlans
vlans = dna.topology.get_vlan_details()
for vlan in vlans.response:
    print(vlan)

# Physical Topology Details
phys_top = dna.topology.get_physical_topology()
print(json.dumps(phys_top, indent=2, sort_keys=True))


############### DEVICES #############
# Print Device Details
devices = dna.devices.get_device_list()
for device in devices.response:
    print(device.type)
    print(device.hostname)
    print(device.managementIpAddress)
    print(device.id)
    print(" ")

# Get a specific device
device = dna.devices.get_device_by_id('c069bc2c-bfa3-47ef-a37e-35e2f8ed3f01')
print(device)


######## HEALTH CHECKS ################
############# CLIENTS ##############
# Get Client Health with Epoch Datetime
epoch_datetime = calendar.timegm(time.gmtime())

client_health = dna.clients.get_overall_client_health()

print(json.dumps(client_health, indent=2, sort_keys=True))
print(' ')
# # GET NETWORK HEALTH
# net_health = dna.networks.get_overall_network_health(timestamp=str(epoch_datetime)
#                                                      )
# print(net_health)
# print(' ')
# # GET SITE HEALTH
# site_health = dna.sites.get_site_health(timestamp=str(epoch_datetime))
# print(json.dumps(site_health, indent=2, sort_keys=True))
