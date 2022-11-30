class President:
    __instance = None
    def __new__(cls, val = None):
        if President.__instance is None:
            President.__instance = object.__new__(cls)
        President.__instance.val = val
        return President.__instance

v = President()
print(v.val)
v.val = 'SBY'
print(v.val)
w = President()
w.val = 'JKW'
print(w.val)
print(v.val)

z = President("HBB")
print(v.val)
print(w.val)
print(z.val)


print(President(), President(), President())