from subprocess import check_output
from functools import lru_cache as cache
from system.calls import Calls


class Network:
    @property
    def ip_addr_eth(self):
        try:
            return Calls.call('IP_ADDR_ETH')
        except Exception as e:
            print(e)
            return None

    @property
    def netmask_eth(self):
        try:
            return Calls.call('NETMASK_ETH')
        except Exception as e:
            print(e)
            return None

    @property
    @cache()
    def mac_addr_eth(self):
        try:
            return Calls.call('MAC_ADDR_ETH')
        except Exception as e:
            print(e)
            return None

    @property
    @cache()
    def has_wlan(self):
        try:
            ret = Calls.call('HAS_WLAN')
        except Exception as e:
            print(e)
            return False
        return bool(ret)

    @property
    @cache()
    def mac_addr_wlan(self):
        if self.has_wlan:
            try:
                return Calls.call('MAC_ADDR_WLAN')
            except Exception as e:
                print(e)
                return None

    @property
    def ip_addr_wlan(self):
        if self.has_wlan:
            try:
                return Calls.call('IP_ADDR_WLAN')
            except Exception as e:
                print(e)
                return None

    def iwlist(self):
        if self.has_wlan:
            try:
                return Calls.call('HAS_WLAN')
            except Exception as e:
                print(e)
            return None
