from lshash import LSHash

lsh = LSHash(6, 8)            # 8 是特征,  6是lsh算法内部2进制编码长度.当然越长越好,可以避免重复.
lsh.index([1,2,3,4,5,6,7,8])
lsh.index([2,3,4,5,6,7,8,9])
lsh.index([10,12,99,1,5,31,2,3])
lsh.query([1,2,3,4,5,6,7,7])
print(1)
