"""
Script to filter information about dataset film
"""

import pandas as pd
import click


class Film:
    def __iniciar__(self, title, year, tickets_sold):        #definimos una clase llamada "film" para poder crear objetos (titulo, año, ventas)
        self.title = title
        self.year = year
        self.tickets_sold = tickets_sold
    
    def calculate_profit(self, ticket_price):               #definimos una funcion para cuando le pongamos los datos, calcule el profit 
        try:
            gross_profit = self.tickets_sold * ticket_price
            return gross_profit
        except Exception as e:                                          #usamos el except porque en caso de que haya algun error durante el proceso (por ej: el dato de precio no este) printee un mensaje de error
            print(f"Error calculating profit for {self.title}: {e}")
            return None





@click.command()
@click.option('--title', prompt='Enter film title', help='The title of the film')
@click.option('--year', prompt='Enter release year', type=int, help='The release year of the film')
@click.option('--tickets_sold', prompt='Enter tickets sold', type=int, help='Number of tickets sold for the film')
@click.option('--ticket_price', prompt='Enter ticket price', type=float, help='Price of each movie ticket')


def main(title, year, tickets_sold, ticket_price):



if __name__ == '__main__':                              #Lo ponemos siempre!!!
    main()