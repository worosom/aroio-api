from functools import lru_cache as cache
from system.calls import Calls


class Network:
    @property
    def lan_ipv4addr(self):
        return Calls.call('IPv4_ADDR_ETH')

    @property
    def lan_ipv6addr(self):
        return Calls.call('IPv6_ADDR_ETH')

    @property
    def lan_netmask(self):
        return Calls.call('NETMASK_ETH')

    @property
    def lan_gateway(self):
        return Calls.call('GATEWAY_ETH')

    @property
    @cache()
    def lan_macaddr(self):
        return Calls.call('MAC_ADDR_ETH')

    @property
    def has_wlan(self):
        return Calls.call('HAS_WLAN')

    @property
    @cache()
    def wlan_macaddr(self):
        if self.has_wlan:
            return Calls.call('MAC_ADDR_WLAN')

    @property
    def wlan_ipv4addr(self):
        if self.has_wlan:
            return Calls.call('IPv4_ADDR_WLAN')

    @property
    def wlan_ipv6addr(self):
        if self.has_wlan:
            return Calls.call('IPv6_ADDR_WLAN')

    @property
    def wlan_netmask(self):
        return Calls.call('NETMASK_ETH')

    @property
    def wlan_gateway(self):
        return Calls.call('GATEWAY_ETH')

    def iwlist(self):
        if self.has_wlan:
            return Calls.call('IWLIST')
        else:
            return []
