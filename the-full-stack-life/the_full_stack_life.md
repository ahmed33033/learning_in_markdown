# Computer Talk for Dummies

For computers to talk to each other, they need an identifier. Think about how we use _names_ to call each other; computers need a name of their own as well.

Every computer that joins a network is given an identifier called an IP (Internet Protocol) Address. There are 2 main _versions_ of IP addresses:

- IPv4, where IP addresses are made up of 32 bits
- IPv6, where IP addresses are made up of 128 bits

Additionally, every computer has various logical (not hardware) channels called ports that an application can use to _listen_ in for a connection.

So, one computer to initiate contact with another, it will have to specify both an IP Address, and a port number!

> Side-note: Every computer has a local network with IP Addresses called loopback IP Addresses. These addresses identify the same computer.

The computer that sends in _requests_ is called a client, and the computer that is listening for requests is called a server. The server responds back with a _response_.
