inputhex = "620D7B005DF2549DF6D51466E599E2BF1F60016A3F980293FFC16E802B325332544017CC951E3801A19A3C98A7FF5141004A48627F21A400C0C9344EBA4D9345D987A8393D43D000172329802F3F5DE753D56AB76009080350CE3B44810076274468946009E002AD2D9936CF8C4E2C472400732699E531EDDE0A4401F9CB9D7802F339DE253B00CCE77894EC084027D4EFFD006C00D50001098B708A340803118E0CC5C200A1E691E691E78EA719A642D400A913120098216D80292B08104DE598803A3B00465E7B8738812F3DC39C46965F82E60087802335CF4BFE219BA34CEC56C002EB9695BDAE573C1C87F2B49A3380273709D5327A1498C4F6968004EC3007E1844289240086C4D8D5174C01B8271CA2A880473F19F5024A5F1892EF4AA279007332980CA0090252919DEFA52978ED80804CA100622D463860200FC608FB0BC401888B09E2A1005B725FA25580213C392D69F9A1401891CD617EAF4A65F27BC5E6008580233405340D2BBD7B66A60094A2FE004D93F99B0CF5A52FF3994630086609A75B271DA457080307B005A68A6665F3F92E7A17010011966A350C92AA1CBD52A4E996293BEF5CBFC3480085994095007009A6A76DF136194E27CE34980212B0E6B3940B004C0010A8631E20D0803F0F21AC2020085B401694DA4491840D201237C0130004222BC3F8C2200DC7686B14A67432E0063801AC05C3080146005101362E0071010EC403E19801000340A801A002A118012C0200B006AC4015088018000B398019399C2FC432013E3003551006E304108AA000844718B51165F35FA89802F22D3801374CE3C3B2B8B5B7DDC11CC011C0090A6E92BF5226E92BF5327F3FD48750036898CC7DD9A14238DD373C6E70FBCA0096536673DC9C7770D98EE19A67308154B7BB799FC8CE61EE017CFDE2933FBE954C69864D1E5A1BCEC38C0179E5E98280"
inputbin = ""

for hexchar in inputhex:
    binvalue = bin(int("0x" + hexchar,16))[2:]

    while len(binvalue) < 4:
        binvalue = "0" + binvalue

    inputbin += binvalue

versions = []

def Operator(subpacketvalues, typeid):
    if typeid == 0:
        return sum(subpacketvalues)

    elif typeid == 1:
        returnval = 1
        for val in subpacketvalues:
            returnval *= val

        return returnval

    elif typeid == 2:
        return min(subpacketvalues)

    elif typeid == 3:
        return max(subpacketvalues)

    elif typeid == 5:
        return int(subpacketvalues[0] > subpacketvalues[1])

    elif typeid == 6:
        return int(subpacketvalues[0] < subpacketvalues[1])

    elif typeid == 7:
        return int(subpacketvalues[0] == subpacketvalues[1])

def DecodePacket(packet):
    version = int(packet[0:3],2)
    typeid = int(packet[3:6],2)

    versions.append(version)
    strippedpacket = packet[6:]

    if typeid == 4: #Literal
        i = 0
        prefix = strippedpacket[i]

        binnumber = ""
        while prefix == "1":
            binnumber += strippedpacket[i+1:i+5]
            i += 5

            prefix = strippedpacket[i]

        binnumber += strippedpacket[i + 1:i + 5]

        while len(binnumber) % 4 != 0:
            binnumber = binnumber[:-1]

        return strippedpacket[i + 5:], int(binnumber,2)

    else: #Operator
        subpacketvalues = []

        lentypeid = strippedpacket[0]

        if lentypeid == "0":
            lenbits = int(strippedpacket[1:16],2)
            subpackets = strippedpacket[16:]

            bitsused = 0

            while bitsused < lenbits:
                newpackets,val = DecodePacket(subpackets)
                subpacketvalues.append(val)

                bitsused += len(subpackets) - len(newpackets)

                subpackets = newpackets

            return subpackets, Operator(subpacketvalues,typeid)

        else:
            numsubpackets = int(strippedpacket[1:12],2)
            subpackets = strippedpacket[12:]

            while numsubpackets != 0:
                subpackets, val = DecodePacket(subpackets)
                subpacketvalues.append(val)
                numsubpackets -= 1

            return subpackets, Operator(subpacketvalues,typeid)

if __name__ == "__main__":
    print("Part 1")
    value = DecodePacket(inputbin)[1]
    print("Answer:", sum(versions))

    print("\nPart 2")
    print("Answer:", value)