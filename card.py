import asyncio
from subprocess import run

CARDMOUNT_RW = 'cardmount rw'
CARDMOUNT_RO = 'cardmount ro'


class Card:
    def cardmount_rw(self):
        run(CARDMOUNT_RW, shell=True)

    def cardmount_ro(self):
        run(CARDMOUNT_RO, shell=True)

    def __enter__(self):
        self.cardmount_rw()
        return self

    def __exit__(self, ex_type, ex_value, ex_traceback):
        self.cardmount_ro()
