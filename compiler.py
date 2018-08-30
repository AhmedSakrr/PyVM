from vm.PyVM import VM
from vm.PyVM import __DEBUG_FLOW
from lib.ISA import *
from pprint import pprint
OPCODE = [

	JUMP,3,RV, # jump to call
	# function x(void) -> void
	MOV_RV,REGISTERS["ma0"],1, # mov ma0,3
	RET,NOP,NOP,
	CALL,REGISTERS["ma0"],RR, # call function x(void)
	MOV_RV,REGISTERS["ma1"],4, # mov ma1,4
	ADD_RR,REGISTERS["ma0"],REGISTERS["ma1"], # add ma0,ma1 = 6

	EXIT,0xc0,0xde # call _exit
]


#open("x.bin","wb").write(bytearray(OPCODE))

VM(OPCODE)
pprint(__DEBUG_FLOW)