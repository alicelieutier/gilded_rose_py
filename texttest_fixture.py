# -*- coding: utf-8 -*-
from __future__ import print_function

from gilded_rose import *

if __name__ == "__main__":
    print ("OMGHAI!")
    items = [
            # typical items degrade by one every day,
            # twice as fast after sell-in
             Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
             Item(name="Long Sword", sell_in=0, quality=20),
             Item(name="Elixir of the Mongoose", sell_in=5, quality=7),

            # Aged Brie - increases in quality every day,
            # twice as fast after sell-in
            # max quality = 50
             Item(name="Aged Brie", sell_in=2, quality=0),
             Item(name="Aged Brie", sell_in=2, quality=50),
             Item(name="Aged Brie", sell_in=0, quality=10),

            # Sulfuras - sell-in does not change, and neither does quality
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),

            # Backstage passes:
            #   increase by 1 until 10 days to concert
            #   increase by 2 until 5 days to concert
            #   increase by 3 until concert
            #   quality of 0 after concert
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=20),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=1, quality=10),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=10),

            # Conjured items degrade twice as fast as typical items (-2, -4)
            # /!\ not implemented yet
             Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
             Item(name="Conjured Mana Cake", sell_in=0, quality=6),  # <-- :O
            ]

    days = 2
    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        GildedRose(items).update_quality()
