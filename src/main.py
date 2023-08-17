# Modules :

import sys , os
sys.dont_write_bytecode = True

from config import connection
from rich.console import Console

from rich.table import Table
import rich.box as bx

from mysql.connector import Error as Err
from tabulate import tabulate

# # # # # # # # # # # # # # # # #

current = Console()

while True:
    query_state = current.input(f"<{connection._host}@[yellow]{connection.user}[/]> : ")

    if query_state == "--clear":
        os.system('cls' if os.name == 'nt' else 'clear')
    elif query_state == "EXIT":
        current.print("[yellow]Bye ^^ ![/]")
        exit()
    else:
        try:

            cursor = connection.cursor(dictionary=True)
            cursor.execute(query_state)
            current.log(f"<success> [green]{query_state}[/]")

            try:
                result : list[dict] = cursor.fetchall()
                table = Table(box=bx.SQUARE)

                current.print(f"\n{tabulate(result , headers='keys',tablefmt='rounded_grid')}\n")
                
                # current.print(table)
                connection.commit() 
                
            except Err as error:
                pass
            
        
        except Err as error:

            current.log(f"<error> : [red]{error.msg}[/]")
