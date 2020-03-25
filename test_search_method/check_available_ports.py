import os
import re
import argparse

parser = argparse.ArgumentParser(description="Check available ports")
parser.add_argument("--sp", type=int, default=8140, help="start port")
parser.add_argument("--ep", type=int, default=8145, help="end port")
parser.add_argument("--k", type=int, default=0, help="if kill")

args = parser.parse_args()

start = args.sp
end = args.ep
available_ports = []
for i in range(end-start+1):
    stream = os.popen(f'lsof -i :{start+i}')
    out = stream.read()
    if not re.compile('.+').match(out):
        available_ports.append(start+i)
        print(f'{start+i}')

if args.k:
    print(args.k)
    for i in range(end-start+1):
        if start + i not in available_ports:
            s = os.popen(f'kill $(lsof -t -i:{start+i}) & > /dev/null')
    print(f'All the processes in port from {start} to {end} are killed!')
