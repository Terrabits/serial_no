import argparse
from   rohdeschwarz.instruments.genericinstrument import GenericInstrument
import sys
import xml.etree.ElementTree as ET


def main():
    # command line interface
    parser = argparse.ArgumentParser(description='Retrieves full DeviceId from R&S instrument')
    parser.add_argument('ip-address', default='localhost')
    args = parser.parse_args()

    # connect to instrument
    instr = GenericInstrument()
    instr.open_tcp(args.ip_address)
    instr.print_info()

    # get DeviceFootprint.xml
    device_footprint_xml = instr.query('SYST:DFPR?')

    # parse device id
    root        = ET.fromstring(device_footprint_xml)
    device_data = root.find('DeviceData')
    device_id   = device_data.get('deviceId')

    print(f'DeviceId: {device_id}')
    sys.exit(0)
