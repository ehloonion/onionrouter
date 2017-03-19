from __future__ import print_function
import socket
import multiprocessing
import atexit
import olib


def close_socket(sock):
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()


def resolve(rerouter, conn, resolve_callback=lambda q, a: (q, a)):
    try:
        while True:
            addr = conn.recv(1024).strip()
            if not addr:
                # connection ended
                return
            if addr == 'get *':
                conn.sendall("500 Request key is not an email address\n")
            else:
                result = rerouter.run(addr)
                resolve_callback(addr, result)
                conn.sendall("{0}\n".format(result))
    except socket.timeout:
        return
    except BaseException as err:
        # todo log
        conn.sendall("500 {0}".format(err))


def daemonize_server(rerouter, host, port, resolver=resolve):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
            sock.sendall(addr)
            print(sock.recv(1024).strip())
