''' mem_read.py - test script for writing to PRU 0 mem using PyPRUSS library'''

PRUSS0_PRU0_DATARAM    = 0
PRUSS0_PRU1_DATARAM    = 1
PRUSS0_PRU0_IRAM       = 2
PRUSS0_PRU1_IRAM       = 3
PRUSS0_SHARED_DATARAM  = 4

import pypruss								# The Programmable Realtime Unit Library
import numpy as np							# Needed for braiding the pins with the delays
import struct
import mmap

pypruss.init()								# Init the PRU
pypruss.open(0)								# Open PRU event 0 which is PRU0_ARM_INTERRUPT
pypruss.pruintc_init()						# Init the interrupt controller
pypruss.exec_program(0, "./mem_read.bin")	# Load firmware "mem_write.bin" on PRU 0
pypruss.wait_for_event(0)					# Wait for event 0 which is connected to PRU0_ARM_INTERRUPT
pypruss.clear_event(0)						# Clear the event
pypruss.exit()								# Exit

PRU_ICSS = 0x4A300000 
PRU_ICSS_LEN = 512*1024

RAM0_START = 0x00000000
RAM1_START = 0x00002000
RAM2_START = 0x00011000


with open("/dev/mem", "r+b") as f:	       
    ddr_mem = mmap.mmap(f.fileno(), PRU_ICSS_LEN, offset=PRU_ICSS) 
    local = struct.unpack('L', ddr_mem[RAM0_START:RAM0_START+4])
    print hex(local[0])
    shared = struct.unpack('L', ddr_mem[RAM2_START:RAM2_START+4])
    print hex(shared[0])
