#!/usr/bin/env python3

import os
import sys
import socket
from termcolor import colored
import time
import argparse

LOG_FILE = open('log.txt', 'at')


def log_data(client, data=''):
    global LOG_FILE

    write_data = "Time: {0}\nIP: {1}\nPort: {2}\nData: {3}\n{4}\n\n".format(time.ctime(),
                                                                            client[0], client[1],
                                                                            data, "=" * 50)
    LOG_FILE.write(write_data)


def start_honeypot(data, ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip, port))
    sock.listen(1000)

    while True:
        incoming_sock, address = sock.accept()
        if address:
            print(colored("[+] REQUEST INCOMING: {0}:{1}".format(address[0], address[1]), "blue"))

            try:
                incoming_sock.send(data.encode('ascii'))
                data = incoming_sock.recv(1024)
                data = data.decode('ascii')
                incoming_sock.close()
            except socket.error as e:
                print(colored("[-] Error! Message: {0}".format(e), "red"))
                log_data(address)
            else:
                log_data(address, data)


def get_cmd_line_arguments():
    parser = argparse.ArgumentParser(prog="Honeypoty",
                                     usage="%(prog)s [options]\n\t[-d | --trap-data] trap_data"
                                           "\n\t[-ip | --host-ip] ipv4 address"
                                           "\n\t[-p | --port] port_number",
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=""">>> | Honeypot v1.0 by Hack Hunt | <<<
    ------------------------------""")

    parser._optionals.title = "Optional Argument"

    required_arguments = parser.add_argument_group("Required Argument")

    required_arguments.add_argument('-d', '--trap-data',
                                    dest='data',
                                    metavar="",
                                    help='If someone tries to connect to the port specified this data will be sent',
                                    required=True)

    required_arguments.add_argument('-ip, --host-ip',
                                    dest='ip',
                                    metavar="",
                                    help='Specify the IPv4 Address of the Host',
                                    required=True)

    required_arguments.add_argument('-p', '--port',
                                    dest='port',
                                    metavar="",
                                    type=int,
                                    help='Specify port number to create Honeypot on',
                                    required=True)

    return parser.parse_args()


def main():
    args = get_cmd_line_arguments()
    data = args.data
    ip = args.ip
    port = args.port

    try:
        os.system("clear")
        print(colored("[+] Initializing Honeypot v1.0...\n", 'green'))
        print(colored("[*] To Quit press Keyboard Interruption Keys.", 'yellow'))
        print(colored("[*] Loading...\n", 'yellow'))

        start_honeypot(data, ip, port)

    except KeyboardInterrupt:
        print(colored("\n[+] Exiting...", "green"))
        sys.exit(0)

    except BaseException as e:
        print(colored("\n[-] Error: {0}".format(e), 'red'))
        sys.exit(1)

    finally:
        LOG_FILE.close()


##################################################################
if __name__ == '__main__':
    main()
