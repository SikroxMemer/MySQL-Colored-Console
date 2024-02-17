# Modules :
from tabulate import tabulate
from mysql.connector import Error as Err
from rich.console import Console
from config import connection
import sys
import os
sys.dont_write_bytecode = True
# # # # # # # # # # # # # # # # #


class MySQLColoredConsole():
    _REVERSE_STATE = True
    _CONSOLE = Console()
    _CONNECTION = connection
    _CONNECTION.autocommit = True

    def __init__(self):
        try:
            while self._REVERSE_STATE:
                self.sql = self._CONSOLE.input(
                    f"<{self._CONNECTION.user}@[yellow]{self._CONNECTION._host}[/]> : ")
                if self.sql == "CLEAR":
                    os.system('cls' if os.name == 'nt' else 'clear')
                elif self.sql == "EXIT":
                    self._CONSOLE.print("[yellow]Bye ^^[/]")
                    exit()
                else:
                    try:
                        self.cursor = self._CONNECTION.cursor(dictionary=True)
                        self.cursor.execute(self.sql)
                        self._CONSOLE.log(f"<success> [green]{self.sql}[/]")
                        result: list[dict] = self.cursor.fetchall()
                        if len(result) > 0:
                            self._CONSOLE.print(
                                f"\n{tabulate(result , headers='keys',tablefmt='simple')}\n")
                    except Err as error:
                        self._CONSOLE.log(f"<error> [red]{error.msg}[/]")
        except KeyboardInterrupt:
            self._CONSOLE.print("\n[red]Ouch :([/]")


sql_client = MySQLColoredConsole()
