#!/usr/bin/env python3

proto = ["ssh", "http", "https"]

print(proto)

print(proto[1])

proto.extend("dns")

print(proto)

proto2 = [22, 80, 443, 53]

proto.extend(proto2)

print(proto)

protoa.append(proto2)

print(protoa)
