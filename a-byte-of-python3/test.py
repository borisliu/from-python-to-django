import pickle

# 这是我们将存储对象的文件名
shoplistfile = 'shoplist.data'
# 购物的清单
shoplist = ['苹果', '芒果', '胡萝卜']

# 写入文件
f = open(shoplistfile, 'wb')
# 将对象存储到文件
pickle.dump(shoplist, f)
f.close()

# 销毁 shoplist 变量
del shoplist

# 从存储中读回
f = open(shoplistfile, 'rb')
# 从文件加载对象
storedlist = pickle.load(f)
print(storedlist)
f.close()
