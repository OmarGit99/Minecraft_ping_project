# -*- coding: utf-8 -*-


from mcstatus import MinecraftServer


server = MinecraftServer.lookup("tacobyte.xyz")


status = server.status()
print("The server has {0} players and replied in {1} ms".format(status.players.online, status.latency))
