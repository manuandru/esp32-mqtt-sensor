
def connect():
    import network
    import time
    from src.utils.config import WIFI
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(WIFI.ssid, WIFI.password)
        while not wlan.isconnected():
            print('Trying to connect...')
            time.sleep(1)
    print('network config:', wlan.ifconfig())