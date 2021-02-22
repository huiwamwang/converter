import requests
import json
import sys


class Converter:

    def __init__(self):
        self.dictionary = None
        self.cache = None

    def requesting(self):
        r = requests.get(f"http://www.floatrates.com/daily/{input()}.json")
        self.dictionary = json.loads(r.text)
        self.cache = ['USD', 'EUR', 'eur', 'usd']
        self.converting()

    def converting(self):
        destination_cur = input()
        if destination_cur == '':
            sys.exit()
        amount = input()
        print("Checking the cache…")
        if destination_cur in self.cache:
            print("Oh! It is in the cache!")
        else:
            print("Sorry, but it is not in the cache!")
            self.cache.append(destination_cur)
        print(f"You received {round((self.dictionary[destination_cur.lower()]['rate'] * float(amount)), 2)} "
              f"{destination_cur.upper()}.")
        self.converting()


go = Converter()
go.requesting()
