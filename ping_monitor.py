#!/work/astephen/venvs/ping/bin/python3

from ping3 import ping
import socket
import time

def main():
    suffix = int(time.time())
    hostname = socket.gethostname()
    with open("ping_times_%s.%s.csv" % (suffix, hostname), "w") as fh:
        while True: 
            t = time.time()
            _t = ping("1.1.1.1", timeout=10)
            if _t is not None:
                time.sleep(1)
                fh.write("%s,%s\n" % (t, _t))
            else:
                fh.write("%s,%s\n" % (t, "-1"))

if __name__ == '__main__':
    main()
