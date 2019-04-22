### Simple crawler to acquire data from https://pemilu2019.kpu.go.id/

#### How to use?
1. Create database using `MySQL` with name `pemilu2019`
>>> You can change database name with your own name, don't forget to change database name in `connection.py` file
2. Set your `MySQL` password on your `environment`
>>> `export MYSQL_PASSWORD=YourMySQLPassword`
3. Run file `main.py` with command
>>> `python main.py time_interval_every_request (in second)` <br><br>
>>> Ex : `python main.py 300`