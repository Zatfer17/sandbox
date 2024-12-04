import os
import pandas as pd
import re

def get_networks():

    command = 'iwctl station wlan0 get-networks'
    result = os.popen(command)
    terminal_output = result.read()

    text_cleaned = re.sub(r'\x1b\[[0-9;]*m', '', terminal_output)
    pattern = r"^\s*(?P<Network_name>[\w\.\,\-\_]+(?:[\s\w\-]+)?)\s+(?P<Security>\w+)\s+(?P<Signal>\*+)\s*$"

    matches = re.findall(pattern, text_cleaned, re.MULTILINE)
    matches = [(network_name.strip(), security, signal) for network_name, security, signal in matches]
    return [('Network name', 'Security', 'Signal quality')] + matches

def connect(network_name, passphrase):
    command = f'iwctl --passphrase "{passphrase}" station wlan0 connect "{network_name}"'
    result = os.popen(command)
