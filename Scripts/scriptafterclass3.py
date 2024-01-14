"""
Script to filter information about dataset film
"""

import pandas as pd
import click

@click.command()
@click.option('--title', prompt='Enter film title', help='The title of the film')
@click.option('--year', prompt='Enter release year', type=int, help='The release year of the film')
@click.option('--tickets_sold', prompt='Enter tickets sold', type=int, help='Number of tickets sold for the film')
@click.option('--ticket_price', prompt='Enter ticket price', type=float, help='Price of each movie ticket')


def main(title, year, tickets_sold, ticket_price):



if __name__ == '__main__':                              #Lo ponemos siempre!!!
    main()