import unittest

import requests

from .. import DixHuitScraper


class TestDixHuitScraper(unittest.TestCase):
    scraper = DixHuitScraper()

    def test_count(self):
        self.assertTrue(self.scraper.count() > 0)

    def test_page(self):
        numbers = self.scraper.page(1)

        self.assertTrue(len(numbers) > 0)

    def test_search(self):
        pass
