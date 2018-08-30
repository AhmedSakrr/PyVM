def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]
        
REG_VAL2NAME = {
	0xff-0:"ret",
	0xff-1:"cou",
	0xff-2:"ma0",
	0xff-3:"ma1",
	0xff-4:"ip"
}