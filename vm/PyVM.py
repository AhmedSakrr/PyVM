import lib.helpers   as H
import lib.Runtime   as RT
import lib.ISA		 as ISA






__DEBUG_FLOW = []

def Parser(op,v0,v1):
	__DEBUG_FLOW.append([RT.REGISTERS["ip"],op,v0,v1])

	if op == ISA.CALL:
		if (v1):
			RT.CALL(RT.REGISTERS[H.REG_VAL2NAME[v0]]+1)
		else:
			RT.CALL(v0)
		
	if op == ISA.RET:
		RT.RET()

	if op == ISA.JUMP:
		if (v1):
			RT.JMP(RT.REGISTERS[H.REG_VAL2NAME[v0]])
		else:
			RT.JMP(v0)

	if op == ISA.POPA:
		RT.POPA()

	if op == ISA.PUSHA:
		RT.PUSHA()

	if op == ISA.PUSH:
		if (v1):
			RT.PUSH(RT.REGISTERS[H.REG_VAL2NAME[v0]])
		else:
			RT.PUSH(v0)

	if op == ISA.POP:
		RT.POP(v0)

	if op == ISA.ADD_RR:
		RT.ADD_RR(v0,v1)

	if op == ISA.ADD_RV:
		RT.ADD_RV(v0,v1)

	if op == ISA.MOV_RV:
		RT.MOV_RV(v0,v1)

	if op == ISA.XOR_RR:
		RT.XOR_RR(v0,v1)

	if op == ISA.XOR_RV:
		RT.XOR_RV(v0,v1)

	if op == ISA.MOV_RR:
		RT.MOV_RR(v0,v1)

	if op == ISA.EXIT and v0 == 0xc0 and v1 == 0xde:
			return "STOP"


def VM(op):
	RT.REGISTERS["ip"] = 0
	op_chuncks  = list(H.chunks(op,3))
	while (1):
		block = op_chuncks[RT.REGISTERS["ip"] % len(op_chuncks)]
		if Parser(block[0],block[1],block[2]) == "STOP":
			break
		RT.REGISTERS["ip"] += 1




#print "==============[DEBUG]=============="
#print "ma0: " + str(RT.REGISTERS["ma0"])
#print "ma1: " + str(RT.REGISTERS["ma1"])
#print "cou: " + str(RT.REGISTERS["cou"])
#print "ret: " + str(RT.REGISTERS["ret"])
#print "ip : "  + str(RT.REGISTERS["ip"])
#print "STACK",RT.STACK
#print "==============[DEBUG]=============="
