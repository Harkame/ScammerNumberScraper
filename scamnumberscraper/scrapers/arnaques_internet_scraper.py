import re

import requests
from bs4 import BeautifulSoup

from .base import ScamNumberPageScraper


class ArnaquesInternetScraper(ScamNumberPageScraper):
    def __init__(self):
        self.name = "arnaques_internet"
        ScamNumberPageScraper.__init__(
            self,
            base_url="http://archive.arnaques-internet.info/modules.php?name=telephone",
            page_url="&pagenum=",
        )

    def page(self, number):
        response = requests.get(f"{self.page_url}{number}")

        page = BeautifulSoup(response.content, features="lxml")

        table = page.find("table", {"class": "table"})

        tr_tags = table.find_all("tr")

        numbers = []

        for i in range(1, len(tr_tags)):
            b = tr_tags[i].find_all("td")[0].find("b")
            numbers.append(b.text.strip().replace("\n", "").replace("\r", ""))

        return numbers

    def count(self):
        response = requests.get(f"{self.base_url}")

        page = BeautifulSoup(response.content, features="lxml")

        td_tag = page.find("td", {"align": "center"})

        content = td_tag.contents[5]

        result = re.search("soit (.*) pages", content)
        page = int(result.group(1))

        return page
