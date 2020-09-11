import sys


def write_report(device, data):
    with open(device, "rb+") as f:
        f.write(data.encode())


def K(name, ctrl=False, shift=False, alt=False):
    modifiers = chr(0)
    mod_ctrl = chr(0x1)
    mod_shift = chr(0x2)
    mod_alt = chr(0x4)
    if ctrl == True:
        modifiers = chr(0x01)
    if shift == True:
        modifiers = chr(0x02)
    if alt == True:
        modifiers = chr(0x04)
    k = {}
    
    k[""] = chr(0)*8
    k["\n"] = modifiers + chr(0)*1+chr(0x28)+chr(0)*5
    k["ESC"] = modifiers + chr(0)*1+chr(0x29)+chr(0)*5
    k[" "] =  modifiers + chr(0)*1+chr(0x2c)+chr(0)*5
    k["-"] =  modifiers + chr(0)*1+chr(0x2d)+chr(0)*5
    #k["+"] =  modifiers + chr(0)*1+chr(0x57)+chr(0)*5

    k["UP"] =     modifiers + chr(0)*1+chr(0x52)+chr(0)*5
    k["DOWN"] =   modifiers + chr(0)*1+chr(0x51)+chr(0)*5
    k["LEFT"] =   modifiers + chr(0)*1+chr(0x50)+chr(0)*5
    k["RIGHT"] =  modifiers + chr(0)*1+chr(0x4f)+chr(0)*5

    k["["] =   modifiers + chr(0)*1+chr(0x2f)+chr(0)*5
    k["]"] =  modifiers + chr(0)*1+chr(0x30)+chr(0)*5

    k["{"] =   mod_shift + chr(0)*1+chr(0x2f)+chr(0)*5
    k["}"] =  mod_shift + chr(0)*1+chr(0x30)+chr(0)*5


    k["~"] =   mod_shift + chr(0)*1+chr(0x35)+chr(0)*5
    k["TAB"] =  modifiers + chr(0)*1+chr(0x2b)+chr(0)*5

    
    k["_"] =  mod_shift + chr(0)*1+chr(0x2d)+chr(0)*5
    k["BACKSPACE"] =  modifiers + chr(0)*1+chr(0x2a)+chr(0)*5
    k["/"] =  modifiers + chr(0)*1+chr(0x38)+chr(0)*5
    k["."] =  modifiers + chr(0)*1+chr(0x37)+chr(0)*5
    k[">"] =  mod_shift + chr(0)*1+chr(0x37)+chr(0)*5
    k["<"] =  mod_shift + chr(0)*1+chr(0x36)+chr(0)*5
    k[","] =  modifiers + chr(0)*1+chr(0x36)+chr(0)*5
    k["?"] =  mod_shift + chr(0)*1+chr(0x38)+chr(0)*5
    k["\\"] =  modifiers + chr(0)*1+chr(0x31)+chr(0)*5
    k["|"] =  mod_shift + chr(0)*1+chr(0x31)+chr(0)*5
    #k["\\"] =  modifiers + chr(0)*1+chr(0x32)+chr(0)*5
    #k["|"] =  mod_shift + chr(0)*1+chr(0x32)+chr(0)*5
    k[";"] =  modifiers + chr(0)*1+chr(0x33)+chr(0)*5
    k[":"] =  mod_shift + chr(0)*1+chr(0x33)+chr(0)*5
    k["="] =  modifiers + chr(0)*1+chr(0x2e)+chr(0)*5
    k["+"] =  mod_shift + chr(0)*1+chr(0x2e)+chr(0)*5

    k["a"] =  modifiers + chr(0)*1+chr(0x04)+chr(0)*5
    k["b"] =  modifiers + chr(0)*1+chr(0x05)+chr(0)*5
    k["c"] =  modifiers + chr(0)*1+chr(0x06)+chr(0)*5
    k["d"] =  modifiers + chr(0)*1+chr(0x07)+chr(0)*5
    k["e"] =  modifiers + chr(0)*1+chr(0x08)+chr(0)*5
    k["f"] =  modifiers + chr(0)*1+chr(0x09)+chr(0)*5
    k["g"] =  modifiers + chr(0)*1+chr(0x0a)+chr(0)*5
    k["h"] =  modifiers + chr(0)*1+chr(0x0b)+chr(0)*5
    k["i"] =  modifiers + chr(0)*1+chr(0x0c)+chr(0)*5
    k["j"] =  modifiers + chr(0)*1+chr(0x0d)+chr(0)*5
    k["k"] =  modifiers + chr(0)*1+chr(0x0e)+chr(0)*5
    k["l"] =  modifiers + chr(0)*1+chr(0x0f)+chr(0)*5
    k["m"] =  modifiers + chr(0)*1+chr(0x10)+chr(0)*5
    k["n"] =  modifiers + chr(0)*1+chr(0x11)+chr(0)*5
    k["o"] =  modifiers + chr(0)*1+chr(0x12)+chr(0)*5
    k["p"] =  modifiers + chr(0)*1+chr(0x13)+chr(0)*5
    k["q"] =  modifiers + chr(0)*1+chr(0x14)+chr(0)*5
    k["r"] =  modifiers + chr(0)*1+chr(0x15)+chr(0)*5
    k["s"] =  modifiers + chr(0)*1+chr(0x16)+chr(0)*5
    k["t"] =  modifiers + chr(0)*1+chr(0x17)+chr(0)*5
    k["u"] =  modifiers + chr(0)*1+chr(0x18)+chr(0)*5
    k["v"] =  modifiers + chr(0)*1+chr(0x19)+chr(0)*5
    k["w"] =  modifiers + chr(0)*1+chr(0x1a)+chr(0)*5
    k["x"] =  modifiers + chr(0)*1+chr(0x1b)+chr(0)*5
    k["y"] =  modifiers + chr(0)*1+chr(0x1c)+chr(0)*5
    k["z"] =  modifiers + chr(0)*1+chr(0x1d)+chr(0)*5
    k["1"] =  modifiers + chr(0)*1+chr(0x1e)+chr(0)*5
    k["!"] =  mod_shift + chr(0)*1+chr(0x1e)+chr(0)*5
    k["2"] =  modifiers + chr(0)*1+chr(0x1f)+chr(0)*5
    k["@"] =  mod_shift + chr(0)*1+chr(0x1f)+chr(0)*5
    k["3"] =  modifiers + chr(0)*1+chr(0x20)+chr(0)*5
    k["#"] =  mod_shift + chr(0)*1+chr(0x20)+chr(0)*5
    k["4"] =  modifiers + chr(0)*1+chr(0x21)+chr(0)*5
    k["$"] =  mod_shift + chr(0)*1+chr(0x21)+chr(0)*5
    k["5"] =  modifiers + chr(0)*1+chr(0x22)+chr(0)*5
    k["%"] =  mod_shift + chr(0)*1+chr(0x22)+chr(0)*5
    k["6"] =  modifiers + chr(0)*1+chr(0x23)+chr(0)*5
    k["^"] =  mod_shift + chr(0)*1+chr(0x23)+chr(0)*5
    k["7"] =  modifiers + chr(0)*1+chr(0x24)+chr(0)*5
    k["&"] =  mod_shift + chr(0)*1+chr(0x24)+chr(0)*5
    k["8"] =  modifiers + chr(0)*1+chr(0x25)+chr(0)*5
    k["*"] =  mod_shift + chr(0)*1+chr(0x25)+chr(0)*5
    k["9"] =  modifiers + chr(0)*1+chr(0x26)+chr(0)*5
    k["("] =  mod_shift + chr(0)*1+chr(0x26)+chr(0)*5
    k["0"] =  modifiers + chr(0)*1+chr(0x27)+chr(0)*5
    k[")"] =  mod_shift + chr(0)*1+chr(0x27)+chr(0)*5
    k["F1"] =  modifiers + chr(0)*1+chr(0x3a)+chr(0)*5
    k["F2"] =  modifiers + chr(0)*1+chr(0x3b)+chr(0)*5
    k["F3"] =  modifiers + chr(0)*1+chr(0x3c)+chr(0)*5
    k["F4"] =  modifiers + chr(0)*1+chr(0x3d)+chr(0)*5
    k["F5"] =  modifiers + chr(0)*1+chr(0x3e)+chr(0)*5
    k["F6"] =  modifiers + chr(0)*1+chr(0x3f)+chr(0)*5
    k["F7"] =  modifiers + chr(0)*1+chr(0x40)+chr(0)*5
    k["F8"] =  modifiers + chr(0)*1+chr(0x41)+chr(0)*5
    k["F9"] =  modifiers + chr(0)*1+chr(0x42)+chr(0)*5
    k["F10"] =  modifiers + chr(0)*1+chr(0x43)+chr(0)*5
    k["F11"] =  modifiers + chr(0)*1+chr(0x44)+chr(0)*5
    k["F12"] =  modifiers + chr(0)*1+chr(0x45)+chr(0)*5
    return k[name]

#write_report("/dev/hidg0", K('z') + K('') + K("x", ctrl=True) + K(""))

def type_kbd(what):
    seq = ""
    for c in what:
        cs = ""+c
        if cs.isupper():
            seq += K(c.lower(), shift=True) + K("")
        else:
            seq += K(c) + K("")

    write_report("/dev/hidg0", seq)


def alt_f2():
    seq = K("F2", alt=True) + K("")
    write_report("/dev/hidg0", seq)


if sys.argv[1] == "RETURN":
    write_report("/dev/hidg0", K('\n') + K(''))
else:
    type_kbd(sys.argv[1])


#write_report("/dev/hidg0", K("LEFT", alt=True) + K(""))
#write_report("/dev/hidg0", K("TAB") + K(""))
#type_kbd("\n")
#alt_f2()
