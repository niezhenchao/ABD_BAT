# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/19 21:47
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：实战
@Installer：pip install requests
"""
import requests
import json
import warnings
warnings.filterwarnings("ignore", category=Warning)

session = requests.session()
# 访问接口
result = session.get(
    'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?'
    'query=175.10.74.133&co=&resource_id=5809&t=1603115352195'
    '&ie=utf8&oe=gbk&cb=op_aladdin_callback&format=json&tn=baidu'
    '&cb=jQuery110205915984965331551_1603115328149&_=1603115328154')
# 获得unicode解码后的返回值
res = result.content.decode('unicode_escape')
print(res)

# 截取：find,rfind

# 取location这个键的值
