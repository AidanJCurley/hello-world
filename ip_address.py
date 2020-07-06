# importing module socket
import socket


def get_ip_address(url):
    first_ip_address = socket.gethostbyname(url)
    return first_ip_address
