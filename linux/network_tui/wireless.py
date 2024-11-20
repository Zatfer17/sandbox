import os
import pandas as pd

def get_networks():

    command = """iw dev wlp2s0 scan | grep 'SSID:\|signal:' | tac"""
    result = os.popen(command)
    terminal_output = result.read()

    print('Scan completed')


    lines = terminal_output.strip().split("\n")
    networks = []
    for i in range(0, len(lines), 2):
        ssid = lines[i].replace("SSID: ", "").strip()
        signal = lines[i + 1].replace("signal: ", "").replace(" dBm", "").strip()
        networks.append((ssid, float(signal)))

    return networks

