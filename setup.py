import os

if __name__ == '__main__':
    os.system('pip install flask mysql-connector-python pymsgbox openpyxl tzlocal simple_log arrow')

from mysql import connector

host = input('Enter localhost for mysql: ')
usr = input('Enter the username for mysql: ')
passw = input('Enter your password for mysql: ')
databases = []
conn = connector.connect(host=host, user=usr, password=passw)
cursor = conn.cursor()
cursor.execute('SHOW DATABASES;')
for i in cursor.fetchall():
    databases.append(i[0])

if 'vehicle_management_system' not in databases:
    cursor.execute('CREATE DATABASE vehicle_management_system;')
    conn.commit()

else:
    pass

conn = connector.connect(host=host, user=usr, password=passw, database='vehicle_management_system')
cursor = conn.cursor()

tables = []
cursor.execute("SHOW TABLES;")
for i in cursor.fetchall():
    tables.append(i[0])

if 'users' not in tables:
    cursor.execute(
        "CREATE TABLE users(`id` INT AUTO_INCREMENT PRIMARY KEY, `name` VARCHAR(255), `account` VARCHAR(255), "
        "`password` VARCHAR(255), `phone_number` VARCHAR(255), `currently_active` VARCHAR(255));")
    cursor.execute("INSERT INTO users(name, account, password, phone_number, currently_active) "
                   "VALUES('admin', NULL, 'admin123', NULL, 'false');")
    conn.commit()
if 'service_request' not in tables:
    cursor.execute("CREATE TABLE `service_request` (`id` int NOT NULL AUTO_INCREMENT,`vehicle_category` varchar(255) "
                   "DEFAULT NULL,`vehicle_name` varchar(255) DEFAULT NULL,`vehicle_model` varchar(255) DEFAULT NULL,"
                   "`vehicle_brand` varchar(255) DEFAULT NULL,`vehicle_registration_number` varchar(255) DEFAULT NULL,"
                   "`service_date` varchar(255) DEFAULT NULL,`service_time` varchar(255) DEFAULT NULL,`service_type` "
                   "varchar(255) DEFAULT NULL,`delivery_date` varchar(255) DEFAULT NULL,`delivery_time` varchar(255) "
                   "DEFAULT NULL,`delivery_address` varchar(255) DEFAULT NULL,`bill` int DEFAULT NULL,`status` "
                   "varchar(255) DEFAULT NULL,PRIMARY KEY (`id`))")
    conn.commit()
    print('You\'re ready to run vehicle service management.py!')

else:
    print('You\'re ready to run vehicle service management.py!')
