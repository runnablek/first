from socket import *

def client(ip, port):

    sock = socket(AF_INET, SOCK_DGRAM )
    sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)


    #print(dir(sock.setsockopt))

    #baddr = (ip, port)
    #print(type(baddr), baddr)

    
    host = gethostbyname(gethostname())
    sock.bind((host, 0))

    data, addr = sock.recvfrom(1024)
    print(data)

    '''
    

    #sock.bind(('', port))

    while True:

        print('111')
        


    '''

    sock.close()


if __name__ == "__main__":


   
    '''
    [pibcmbfu] # [cts] future
    15572  233.37.54.171   * KP200 real
    16572   233.37.54.171   * KP200 test
    1234   233.37.54.171   * KP200 virtual sise


    #define IP_FUTURE                       ("231.2.2.11")
    #define PORT_FUTURE                     (35572)
    #define PORT_FUTURE_SEND                (1234)

    #define IP_CALL                         ("231.2.2.11")
    #define PORT_CALL                       (35515)
    #define PORT_CALL_SEND                  (1235)

    #define IP_PUT                          ("231.2.2.11")
    #define PORT_PUT                        (35516)
    #define PORT_PUT_SEND                   (1236)




    '''


    ip = '231.2.2.11'
    port =  35572

    client(ip, port)

    

   


