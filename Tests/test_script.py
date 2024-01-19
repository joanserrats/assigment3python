import unittest
from scripts.scriptafterclass3 import Film

"""
TEST 1- FILTER BY PRICE
"""
def test_filter_by_price():
    filtering_class = FilteringClass(load_dataset("filmgenrestats.csv"))     #en el caso de tener otro dataset lo sustituiriamos por filmgenrestats.csv
    filtered_df = filtering_class.filter_price(100)
    assert all(filtered_df['Price Starting With ($)'] < 100)


"""
TEST 2- FILTER BY GENRE
"""
def test_filter_by_genre():
    filtering_class = FilteringClass(load_dataset("filmgenrestats.csv"))
    filtered_df = filtering_class.filter_genre("Action")
    assert all(filtered_df['genre'] == "Action")

"""
TEST 3- TICKETS SOLD
"""
def test_filter_by_tickets_sold():
    filtering_class = FilteringClass(load_dataset("filmgenrestats.csv"))
    filtered_df = filtering_class.filter_tickets_sold(50000)
    assert all(filtered_df['tickets_sold'] >= 50000)

"""
TEST 4- FILTER BY YEAR
"""
def test_filter_by_year():
    filtering_class = FilteringClass(load_dataset("filmgenrestats.csv"))
    filtered_df = filtering_class.filter_year(2000)
    assert all(filtered_df['year'] == 2000)

