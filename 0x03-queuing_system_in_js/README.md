0x03-queuing_system_in_js

Download, extract, and compile Redis:
bash
Copy code
$ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
$ tar xzf redis-6.0.10.tar.gz
$ cd redis-6.0.10
$ make
Start Redis server:
bash
Copy code
$ src/redis-server &
Check if Redis server is running:
bash
Copy code
$ src/redis-cli ping
Expected output:

Copy code
PONG
Set a key-value pair in Redis:
bash
Copy code
$ src/redis-cli set Holberton School
Expected output:

Copy code
OK
Retrieve the value for the key:
bash
Copy code
$ src/redis-cli get Holberton
Expected output:

arduino
Copy code
"School"
Note the process id (PID) of the Redis server and kill it:
bash
Copy code
$ ps aux | grep redis-server
Identify the PID from the output and then:

bash
Copy code
$ kill [PID_OF_Redis_Server]
Copy the dump.rdb file from the redis-6.0.10 directory to the Queuing project root:
bash
Copy code
$ cp redis-6.0.10/dump.rdb /path/to/Queuing/project
