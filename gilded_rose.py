# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            special_items = {
                "Aged Brie": self.aged_brie_decay,
                "Backstage passes to a TAFKAL80ETC concert": self.backstage_passes_decay,
                "Sulfuras, Hand of Ragnaros": (lambda x : x),
            }
            if item.name in special_items:
                special_items[item.name](item)
            else:
                self.typical_decay(item)
            pass

        
    def typical_decay(self, item):
        self.update_sell_in(item)
        if item.sell_in >= 0:
            item.quality -=1
        else:
            item.quality -= 2
        self.readjust_quality_in_bounds(item)

    def aged_brie_decay(self, item):
        self.update_sell_in(item)
        if item.sell_in >= 0:
            item.quality +=1
        else:
            item.quality +=2
        self.readjust_quality_in_bounds(item)

    def backstage_passes_decay(self, item):
        self.update_sell_in(item)
        if item.sell_in >= 0:
            item.quality += self.backstage_passes_increase_rate_for_sell_in(item.sell_in)
        else: # concert has passed
            item.quality = 0
        self.readjust_quality_in_bounds(item)

    def backstage_passes_increase_rate_for_sell_in(self, sell_in):
        ## hacky one-liner:
        # return 3 - min(10, sell_in) / 5
        if sell_in >= 10:
            return 1
        if sell_in in range(5, 10):
            return 2
        if sell_in in range(0, 5):
            return 3

    # TODO implement conjured items
    def conjured_item_decay(self, item):
        self.typical_decay(item)


    def update_sell_in(self, item):
        item.sell_in -= 1
        self

    def readjust_quality_in_bounds(self, item):
        item.quality = max(0, item.quality)
        item.quality = min(50, item.quality)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
