# Fake Serial Port
**Ever written code that interacts with serial devices and wished for a way to test that code without said devices?** Use this repo as a reference to quickly set up virtual serial ports using `socat`. To get started perform the below docker steps and then any one of the examples. 

### Docker Usage:
* Build the image: 
```
docker build -t fake_serial_port .
```

* Run the container and enter a terminal session:
```
docker run --rm --name fake_serial_port -it fake_serial_port bash
```

* In a different terminal, enter a terminal session in the running container:
```
docker exec -it fake_serial_port bash
```

### Echo Example
Emulate a serial device that will echo all data sent to it. Build and Run the container as per [docker usage](#docker-usage).

* Run the "device"
```
socat -d -d pty,rawer,echo=0,link=/dev/device EXEC:./echo,pty,rawer
```

* Run the code to be tested with said "device". This code uses the python module `pyserial`.
```
python3 test_pyserial.py
```

### Talker Example
Emulate a serial device that writes data at contant rate.  Build and Run the container as per [docker usage](#docker-usage).

* Run the "device"
```
socat -d -d pty,rawer,echo=0,link=/dev/device EXEC:./talk,pty,rawer
```

* Run the code to be tested with the "device". This code uses the python module `fileinput`.
```
python3 test_fileinput.py
```

### Notes for Socat:
* Using `socat -d -d pty,rawer,echo=0,link=<serial_port> EXEC:<executable/command>,pty,rawer` will set up a virtual port and pipe the IO to this virtual port to the stdin/stdout of a process. 
* Root privileges are required to use the above command. And then  subsequently to use the serial port, unless you change permissions after running the command. 