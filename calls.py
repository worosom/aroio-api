from subprocess import run, check_output


def get_filter_fmt(ret): return int(ret.split(':')[-1])//2


_calls = {
    'CHECKSOUNDCARD': {
        'call': 'checksoundcard'
    },
    'HEARTBEAT_LED': {
        'call': 'echo heartbeat >/sys/class/leds/led0/trigger'
    },
    'REBOOT': {
        'call': 'reboot -d 1 &'
    },
    'MAC_ADDR_ETH': {
        'call': 'cat /sys/class/net/eth0/address',
        'returns': str
    },
    'IPv4_ADDR_ETH': {
        'call': 'ifconfig eth0 | grep inet | grep -v 127 | grep -v inet6 | awk -F: \'{ print $2 }\' | awk \'{ print $1 }\'',
        'returns': str
    },
    'IPv6_ADDR_ETH': {
        'call': 'ifconfig eth0 | grep inet6 | grep -v 127 | grep -v inet | awk -F: \'{ print $2 }\' | awk \'{ print $1 }\'',
        'returns': str
    },
    'NETMASK_ETH': {
        'call': 'ifconfig eth0 | sed -rn \'2s/ .*:(.*)$/\\1/p\'',
        'returns': str
    },
    'GATEWAY_ETH': {
        'call': 'ip route show default 0.0.0.0/0 | grep eth0 | awk \'/default/ {print $3}\'',
        'returns': str
    },
    'MAC_ADDR_WLAN': {
        'call': 'cat /sys/class/net/wlan0/address',
        'returns': str
    },
    'IPv4_ADDR_WLAN': {
        'call': 'echo test',
        'returns': str
    },
    'IPv6_ADDR_WLAN': {
        # 'call': 'ifconfig wlan0 | grep inet6 | grep -v Link | awk -F: \'{ print $2 }\' | awk \'{ print $1 }\'',
        'returns': str
    },
    'NETMASK_WLAN': {
        'call': 'ifconfig wlan0 | sed -rn \'2s/ .*:(.*)$/\\1/p\'',
        'returns': str
    },
    'GATEWAY_WLAN': {
        'call': 'ip route show default 0.0.0.0/0 | grep wlan0 | awk \'/default/ {print $3}\'',
        'returns': str
    },
    'HAS_WLAN': {
        'call': 'dmesg | grep -qe WLAN -e Realtek && echo "1"',
        'returns': bool
    },
    'IWLIST': {
        'call': 'ifconfig wlan0 up && iwlist scan 2>/dev/null | sed \'s/"//g\' | awk -F":" \'/ESSID/{print $2}\' | sort -f',
        'returns': list
    },
    'GET_FILTER': {
        'call': '/usr/bin/controlbrutefir getFilter',
        'returns': int,
        'format': get_filter_fmt
    },
    'SET_FILTER': {
        'call': '/usr/bin/controlbrutefir chgFilter'
    },
    'GET_VOLUME': {
        'call': '/usr/bin/controlbrutefir getVol',
        'returns': int
    },
    'SET_VOLUME': {
        'call': '/usr/bin/controlbrutefir volControl'
    }
}


class Calls:
    @staticmethod
    def call(_call):
        call = _calls[_call]
        try:
            output = Calls.check_output(call)
            if call['returns'] in (str, list):
                output = output.decode('utf-8')
            if call['returns'] == list:
                output = output.splitlines()
            if 'returns' in call:
                output = call['returns'](output)
            if 'format' in call:
                output = call['format'](output)
            return output
        except Exception as e:
            print(_call, e)
            return str(e)

    @staticmethod
    def check_output(call):
        return check_output(call['call'], shell=True)

    @staticmethod
    def run(_call, *args):
        try:
            cmd = _calls[_call]['call']
            if args:
                for arg in args:
                    cmd = f'{cmd} {arg}'
            run(cmd, shell=True)
        except Exception as e:
            print(_call, e)
            return e
