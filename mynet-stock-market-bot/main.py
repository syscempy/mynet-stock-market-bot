#!/usr/bin/env python3
import sys
from src.scraper import Scraper

scraper = Scraper(url="https://finans.mynet.com/borsa/hisseler/")
result = scraper.start()
scraper.save_file(result)
