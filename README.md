# MyFileListener
一个基于MD5的文件监控系统 A file monitoring system based on MD5


# 需求说明
  需要实现对一个文件夹下的文件的增加、修改和删除的监控， 一旦发生上述操作，则进行提示。可以选择过滤掉文件名中的特定字符和只监听文件名中含有特定字符的文件。

# 简述
  1. 关于文件的增加、修改、删除的反馈，可以想到利用MD5等类似的加密算法，因为文件本身可以生成哈希值，只要文件内容或者文件名被修改过，就会生成和修改之前的哈希值不同的值，因此可以利用dict来存储，一个文件名对应一个哈希值来存储。其中增加和删除就对应一个新增加的键值对和一个减少的键值对，而修改则可以理解为删除了旧的文件、增加了一个新的文件。   
  MD5算法可以直接利用第三方的 hashlib 库来实现
  
  2. 关于滤掉文件名中的特定字符和只监听文件名中含有特定字符的文件的功能，这个其实非常简单，只需要用 list 分别对需要过滤和必须存在字符串进行存储， 然后利用标志位和字符串的子串包含性进行判断就可以了，只有满足条件的文件可以产生哈希值，产生哈希值也就意味着被监听了。   
　判断字符串中是否含有字串最常用的方法是 in 和 string 中的 find 方法，这里就不再赘述，可以直接看下面的代码

  3. 因为要同时监控多个文件夹，所以必须要利用到线程来处理，创建一个线程池来存储线程， 线程利用了 threading 库，并且实现一个线程类来处理线程的操作
  
# 文件说明
  createConfigFile 为分别初始化json和toml格式的配置文件   
  myToml 为基于toml格式数据传递的监控程序   
  myJson 为基于Json格式数据传递的监控程序   
  jsonConfig 为json格式的配置文件   
  tomlConfig 为toml格式的配置文件   
