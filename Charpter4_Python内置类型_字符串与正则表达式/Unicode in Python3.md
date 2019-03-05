## Unicode and UTF-8

1. 所有东西（file， network）在计算机中都是以 byte 存储的。但是 byte
本身没有含义，为了使 byte 表示文本，我们需要一套相应的编码方案（比如 ASCII）。

2. 但是事实是世界上的文字很多，而 ASCII
只能表示西方字符，要表示其他字符（比如中文）就无力了。因此每个国家都有一套自己的编码方案来编码自己国家的字符。但这样就产生了混乱（一个byte在不同的编码方案下产生的字符不同）。
为了解决这个问题，产生了 Unicode，每种字符只有一个相应的 coding point
表示。而将 Unicode 字符的 coding point map 到 bytes 的就是 UTF-8，
UFT-16。 因此可以这么认为 **Unicode 是一套字符集，而 UFT-8 等是编码方案 **

## Unicode in Python3
1. 在 Python3 中，有 str, bytes, bytearray。str type 存储的是 Unicode
字符的coding point，而 bytes type 存储的是 bytes。而且在 Python3 中不会有
bytes 和 str 的隐形转换。（在 Python2 中有，这也往往是bug的来源）

![](https://gitee.com/qytanggit/Python_Basic/raw/master/image/Charpter4/unicode0.jpg)

![](https://gitee.com/qytanggit/Python_Basic/raw/master/image/Charpter4/unicode1.jpg)

![](https://gitee.com/qytanggit/Python_Basic/raw/master/image/Charpter4/unicode2.jpg)

### 查看系统编码方式：
\>>> import sys  
\>>> sys.getfilesystemencoding()  
\>>> 'utf-8'

### 编码测试：
\>>> test1 = '亁颐堂'  
\>>> test1.encode()  
b'\xe4\xba\x81\xe9\xa2\x90\xe5\xa0\x82'  
\>>> test1.encode('gbk')  
b'\x81x\xd2\xc3\xcc\xc3'  
\>>> test1.encode('gb18030')  
b'\x81x\xd2\xc3\xcc\xc3'

### 解码测试(尾部添加了\x01)：
\>>> octets1 = b'\xe4\xba\x81\xe9\xa2\x90\xe5\xa0\x82\x01'  
\>>> octets1.decode()  
'亁颐堂\x01'  
\>>> octets1.decode('gbk')  
解码错误  
\>>> octets1.decode('gb18030')  
解码错误

ASCII字符会自动转码:  
\>>> print(b'\x73\x70\x01\x61\x6d')  
b'sp\x01am'  
\>>> b'sp\x01am' == b'\x73\x70\x01\x61\x6d'  
True
