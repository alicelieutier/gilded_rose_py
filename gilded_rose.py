# -*- coding: utf-8 -*-

class GildedRose(object):
    def __init__(self, items):
        self.items = [self.wrapItemInClass(item) for item in items]

    def update_quality(self):
        for item in self.items:
            item.update()

    def wrapItemInClass(self, item):
        special_item_classes = {
            "Aged Brie": AgedBrie,
            "Backstage passes to a TAFKAL80ETC concert": BackstagePasses,
            "Sulfuras, Hand of Ragnaros": Sulfuras,
        }
        if item.name in special_item_classes:
            return special_item_classes[item.name](item.name, item.sell_in, item.quality)
        elif item.name.startswith('Conjured'):
            return ConjuredItem(item.name, item.sell_in, item.quality)
        else:
            return TypicalItem(item.name, item.sell_in, item.quality)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class Sulfuras(Item):
    def update(self):
        pass

class TypicalItem(Item):
    def _update_sell_in(self):
        self.sell_in -= 1
        return self

    def _update_quality(self):
        if self.sell_in >= 0:
            self.quality -=1
        else:
            self.quality -=2
        return self

    def _readjust_quality_in_bounds(self):
        self.quality = max(0, self.quality)
        self.quality = min(50, self.quality)
        return self

    def update(self):
        self._update_sell_in()
        self._update_quality()
        self._readjust_quality_in_bounds()
        return


class AgedBrie(TypicalItem):
    def _update_quality(self):
        if self.sell_in >= 0:
            self.quality +=1
        else:
            self.quality +=2
        return self

class ConjuredItem(TypicalItem):
    def _update_quality(self):
        if self.sell_in >= 0:
            self.quality -=2
        else:
            self.quality -=4
        return self

class BackstagePasses(TypicalItem):
    def _update_quality(self):
        if self.sell_in >= 0:
            self.quality += self.__backstage_passes_increase_rate_for_sell_in(self.sell_in)
        else: # concert has passed
            self.quality = 0

    @staticmethod
    def __backstage_passes_increase_rate_for_sell_in(sell_in):
        ## hacky one-liner:
        # return 3 - min(10, sell_in) / 5
        if sell_in >= 10:
            return 1
        if sell_in in range(5, 10):
            return 2
        if sell_in in range(0, 5):
            return 3

if __name__ == '__main__':
    items = [Item("Aged Brie", 1, 48)]
    gilded_rose = GildedRose(items)
    for i in range(1, 5):
        print(gilded_rose.items)
        gilded_rose.update_quality()
