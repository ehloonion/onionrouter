from __future__ import print_function
import socket
import multiprocessing
import atexit
from onionrouter import olib


def close_socket(sock):
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()


def resolve(rerouter, conn, resolve_callback=lambda q, a: (q, a)):
    try:
        while True:
            addr = conn.recv(1024).decode().strip()
            if not addr:
                # connection ended
                return
            if addr == 'get *':
                conn.sendall(
                    "500 Request key is not an email address\n".encode()
                )
            else:
                result = rerouter.run(addr)
                resolve_callback(addr, result)
                conn.sendall("{0}\n".format(result).encode())
    except socket.timeout:
        return
    except BaseException as err:
        # todo log
        conn.sendall("500 {0}\n".format(err).encode())


def daemonize_server(rerouter, host, port, resolver=resolve):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(1)
    atexit.register(close_socket, sock=sock)
    while True:
        conn, address = sock.accept()
        process = multiprocessing.Process(target=resolver,
                                          args=(rerouter, conn))
        process.daemon = True
        process.start()


def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    atexit.register(close_socket, sock=sock)
    while True:
        addr = olib.cross_input("Enter an email address: ")
        if addr == 'get *':
            print("500 Request key is not an email address")
        else:
            sock.sendall(addr.encode())
            print(sock.recv(1024).decode().strip())
