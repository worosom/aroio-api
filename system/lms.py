import asyncio
from shell import run

RESTART_LMS = 'killall startstreamer.sh && killall shairport && killall squeezelite && /usr/bin/startstreamer.sh &> /dev/null &'


class LMS:
    def restart(self):
        asyncio.run(
            run(RESTART_LMS)
        )
