import helpers as R

REGISTERS = {
	"ret" :0,
	"cou" :0,
	"ma0" :0,
	"ma1" :0,
	"ip"  :0
}

STACK = []

def CALL(ip):
	PUSH(REGISTERS["ip"])
	REGISTERS["ip"] = (ip - 1) 
	
def RET():
	REGISTERS["ip"] = STACK[len(STACK)-1]
	del STACK[len(STACK)-1]

def JMP(ip):
	REGISTERS["ip"] = (ip - 1)

def POPA():
	LEN_REG = len(REGISTERS)
	POP_VAL = STACK[-LEN_REG::]
	index = 0
	for reg in REGISTERS:
		REGISTERS[reg] = POP_VAL[index]
		index += 1
		del STACK[-LEN_REG::index]

def PUSHA():
	for reg in REGISTERS:
		STACK.append(REGISTERS[reg])

def PUSH(value):
	STACK.append(value)

def POP(R0):
	REGISTERS[R.REG_VAL2NAME[R0]] = STACK[len(STACK)-1]
	del STACK[len(STACK)-1] 

def ADD_RR(R0,R1):
	REGISTERS[R.REG_VAL2NAME[R0]] += REGISTERS[R.REG_VAL2NAME[R1]]

def ADD_RV(R0,V):
	REGISTERS[R.REG_VAL2NAME[R0]] += V

def MOV_RV(R0,V):
	REGISTERS[R.REG_VAL2NAME[R0]] = V

def XOR_RR(R0,R1):
	REGISTERS[R.REG_VAL2NAME[R0]] ^= REGISTERS[R.REG_VAL2NAME[R1]]

def XOR_RV(R0,V):
	REGISTERS[R.REG_VAL2NAME[R0]] ^= V

def MOV_RR(R0,R1):
	REGISTERS[R.REG_VAL2NAME[R0]] = REGISTERS[R.REG_VAL2NAME[R1]]
