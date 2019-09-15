from subprocess import check_output

_calls = {
    'MAC_ADDR_ETH': {
        'call': 'cat /sys/class/net/eth0/address',
        'returns': str
    },
    'IP_ADDR_ETH': {
        'call': 'ifconfig eth0 | grep inet | grep -v 127 | awk -F: \'{ print $2 }\' | awk \'{ print $1 }\'',
        'returns': str
    },
    'NETMASK_ETH': {
        'call': 'ifconfig eth0 | sed -rn \'2s/ .*:(.*)$/\\1/p\'',
        'returns': str
    },
    'MAC_ADDR_WLAN': {
        'call': 'cat /sys/class/net/wlan0/address',
        'returns': str
    },
    'IP_ADDR_WLAN': {
        'call': 'ifconfig wlan0 | grep inet | grep -v 127 | awk -F: \'{ print $2 }\' | awk \'{ print $1 }\'',
        'returns': str
    },
    'NETMASK_WLAN': {
        'call': 'ifconfig wlan0 | sed -rn \'2s/ .*:(.*)$/\\1/p\'',
        'returns': str
    },
    'HAS_WLAN': {
        'call': 'dmesg | grep -qe WLAN -e Realtek',
        'returns': bool
    },
    'IWLIST': {
        'call': 'ifconfig wlan0 up && iwlist scan 2>/dev/null | sed \'s/"//g\' | awk -F":" \'/ESSID/{print $2}\' | sort -f',
        'returns': list
    }
}

DEV = False


class Calls:
    @staticmethod
    def call(_call):
        call = _calls[_call]
        if DEV:
            cmd = call["call"].replace("'", "\'")
            call['call'] = f'ssh -q root@10.0.1.37 \'{cmd}\''
        try:
            output = check_output(call['call'], shell=True).decode('utf-8')
            if call['returns'] == list:
                output = output.splitlines()
            return call['returns'](output)
        except Exception as e:
            print(e)
            return str(e)
