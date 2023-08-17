# MySQL Python Console

The MySQL Python Console is a customized version of the MySQL shell that allows you to interact with a MySQL database using Python. It provides a user-friendly interface for executing SQL queries and managing your database, while leveraging the power and flexibility of the Python programming language.

This project is built on top of the `mysql-connector` library for Python and enhances the console experience using the `rich` library for enhanced text formatting and visualization.

## Features

- Execute SQL queries interactively.
- Display query results in a visually appealing format using `rich` formatting.
- Perform CRUD (Create, Read, Update, Delete) operations on your MySQL database.
- Manage database schema and table structures.
- Customized command-line interface for a more intuitive user experience.

## Installation

Before running the MySQL Python Console, make sure you have the following requirements installed:

- [mysql-connector](https://pypi.org/project/mysql-connector/): A MySQL driver for Python.
- [rich](https://pypi.org/project/rich/): A library for rich text and beautiful formatting in the terminal.

You can install these requirements using the following commands:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone this repository or download the source code.
2. Navigate to the project directory.

```bash
cd MySQL-Python-Console
```

3. Run the Python script to start the MySQL Python Console.

```bash
python mysql_python_console.py
```

4. Change **config.py** and enter your MySQL database credentials (host, username, password, database name).
5. Once connected, you can start entering your SQL queries and interacting with the database at **main.py**.

## Commands

The MySQL Python Console supports a set of commands for various operations:

- `SELECT`: Execute SELECT queries.
- `INSERT`: Execute INSERT queries to add data.
- `UPDATE`: Execute UPDATE queries to modify data.
- `DELETE`: Execute DELETE queries to remove data.
- `SHOW TABLES`: Display a list of tables in the database.
- `DESCRIBE <table_name>`: Display the schema of a specific table.
- `EXIT` : Exit the MySQL Python Console.
- `--CLEAR` : To clear off console.

## Contributions

Contributions to this project are welcome! If you have any improvements or new features to add, feel free to open a pull request on the GitHub repository.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as per the terms of the license.

## Acknowledgments

- This project was inspired by the need for a more user-friendly MySQL shell with Python integration.
- The `mysql-connector` and `rich` libraries made this project possible by providing the necessary tools for connecting to MySQL databases and enhancing the console's text output.
- Special thanks to the open-source community for their continuous support and contributions.

---

Happy querying with the MySQL Python Console! If you encounter any issues or have suggestions for improvements, please don't hesitate to reach out or open an issue on GitHub.
