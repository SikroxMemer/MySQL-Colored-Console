from tabulate import tabulate
from rich.console import Console
from mysql.connector.errors import Error
from mysql.connector.connection import MySQLConnection
import os


class Connection(MySQLConnection):
    """
    Standard MySQL Connection 
    """
    # This Is Sensible Data Don't Share it if you are working in a production server
    __SQL_INFO = {"host": "localhost", "user": "root",
                  "password": "YOUR_SUPER_SECRET_PASSWORD"}
    _CONSOLE = Console()

    def __init__(self, **kwargs) -> None:
        try:
            super().__init__(**self.__SQL_INFO)
        except Error as error:
            self._CONSOLE.print("[red]{}[/]".format(error))


class MySQLColoredConsole():

    _REVERSE_STATE = True
    _CONSOLE = Console()
    _CONNECTION = Connection()
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

                        self.cursor = self._CLIENT.cursor(dictionary=True)
                        self.cursor.execute(self.sql)
                        self._CONSOLE.log(f"<success> [green]{self.sql}[/]")
                        result: list[dict] = self.cursor.fetchall()

                        if len(result) > 0:

                            self._CONSOLE.print(
                                f"\n{tabulate(result , headers='keys',tablefmt='simple')}\n")

                    except Error as error:

                        self._CONSOLE.log(f"<error>[red]{error.msg}[/]")

        except KeyboardInterrupt:
            self._CONSOLE.print("\n[red]Ouch :([/]")


sql_client = MySQLColoredConsole()
