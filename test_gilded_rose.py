# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):

    # test typical items
    def test_typical(self):
        expected_decay = [(9, 9), (8, 8), (7, 7), (6, 6)]
        self.assertDecayOverNDays(
            Item("foo", 10, 10),
            expected_decay
        )

    def test_end_of_sellin(self):
        # decay is two times faster after sell-in date
        expected_decay = [(1, 9), (0, 8), (-1, 6), (-2, 4), (-3, 2)]
        self.assertDecayOverNDays(
            Item("foo", 2, 10),
            expected_decay
        )

    def test_end_of_sellin_and_quality_0(self):
        expected_decay = [(0, 1), (-1, 0), (-2, 0)]
        self.assertDecayOverNDays(
            Item("foo", 1, 2),
            expected_decay
        )

    def test_min_quality_0(self):
        expected_decay = [(9, 1), (8, 0), (7, 0), (6, 0), (5, 0)]
        self.assertDecayOverNDays(
            Item("foo", 10, 2),
            expected_decay
        )

    # defensive testing
    def test_quality_negative(self):
        expected_decay = [(9, 0)]
        self.assertDecayOverNDays(
            Item("foo", 10, -10),
            expected_decay
        )

    def test_quality_more_than_50(self):
        expected_decay = [(9, 50)]
        self.assertDecayOverNDays(
            Item("foo", 10, 200),
            expected_decay
        )

    # test special items
    def test_conjured_item(self):
        expected_decay = [(9, 8), (8, 6), (7, 4)]
        self.assertDecayOverNDays(
            Item("Conjured Mana Cake", 10, 10),
            expected_decay
        )

    def test_conjured_item(self):
        expected_decay = [(0, 8), (-1, 4), (-2, 0), (-3, 0)]
        self.assertDecayOverNDays(
            Item("Conjured Mana Cake", 1, 10),
            expected_decay
        )

    def test_aged_brie(self):
        expected_decay = [(1, 1), (0, 2), (-1, 4), (-2, 6)]
        self.assertDecayOverNDays(
            Item("Aged Brie", 2, 0),
            expected_decay
        )

    def test_aged_brie_max_quality(self):
        expected_decay = [(0, 49), (-1, 50), (-2, 50)]
        self.assertDecayOverNDays(
            Item("Aged Brie", 1, 48),
            expected_decay
        )

    def test_sulfuras(self):
        expected_decay = [(4, 200), (4, 200), (4, 200)]
        self.assertDecayOverNDays(
            Item("Sulfuras, Hand of Ragnaros", 4, 200),
            expected_decay
        )

    def test_sulfuras(self):
        expected_decay = [(-4, 200), (-4, 200), (-4, 200)]
        self.assertDecayOverNDays(
            Item("Sulfuras, Hand of Ragnaros", -4, 200),
            expected_decay
        )

    def test_backstage_passes(self):
        expected_decay = [
            (11, 11), (10, 12),
            (9, 14), (8, 16), (7, 18), (6, 20), (5, 22),
            (4, 25), (3, 28), (2, 31), (1, 34), (0, 37),
            (-1, 0), (-2, 0)
        ]
        self.assertDecayOverNDays(
            Item("Backstage passes to a TAFKAL80ETC concert", 12, 10),
            expected_decay
        )

    def test_backstage_passes_max_quality(self):
        self.assertDecayOverNDays(
            Item("Backstage passes to a TAFKAL80ETC concert", 15, 49),
            [(14, 50)]
        )
        self.assertDecayOverNDays(
            Item("Backstage passes to a TAFKAL80ETC concert", 10, 49),
            [(9, 50)]
        )
        self.assertDecayOverNDays(
            Item("Backstage passes to a TAFKAL80ETC concert", 5, 49),
            [(4, 50)]
        )

    # decay expects an array of pairs on expected sell-in and quality value over the next n days
    def assertDecayOverNDays(self, item, expected_decay):
        gilded_rose = GildedRose([item])
        for (expected_sellin, expected_quality) in expected_decay:
            gilded_rose.update_quality()
            self.assertItemSellInAndQuality(
                gilded_rose.items[0],
                (expected_sellin, expected_quality)
            )

    def assertItemSellInAndQuality(self, item, (expected_sellin, expected_quality)):
        self.assertEquals(
            item.sell_in,
            expected_sellin,
            '{}: incorrect sell_in value {}, expected {}'.format(item, item.sell_in, expected_sellin)
        )
        self.assertEquals(
            item.quality,
            expected_quality,
            '{}: incorrect quality value {}, expected {}'.format(item, item.quality, expected_quality)
        )

if __name__ == '__main__':
    unittest.main()
