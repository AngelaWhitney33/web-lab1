# WEB信息处理实验一
## 运行环境
使用python作为编程语言，主要调用的库有nltk和email.parser
下载nltk推荐直接下载 https://github.com/nltk/nltk_data/tree/gh-pages/packages 并解压子文件夹下的压缩文件，具体教程可见 https://www.cnblogs.com/eksnew/p/12909814.html .
## 文件结构
* src 代码文件
    * bool_search.py: 对于原始邮件进行分词、词根化、去停用词等操作，结果写入output/dataset
    * pre.py: 对于bool_search.py得到的结果进行进一步处理，统计每个人的词频并写入output/count/{people}.csv中，然后再对于所有人的词频统计得到总的词频sorted_count.csv，从中取前1000个作为查询词。
    * my_stopwords: 由于原始的stopwords不能够特别的针对数据集，故排序后手动去除了部分词语作为停用词，可根据实际需要再次修改（但是修改后需要重新运行pre.py来获得最新的词频统计表）
* output 输出文件夹
    * /count 包含了每个人的词频统计
    * sorted_count.csv 所有人合并在一起的词频统计，前1000个作为查询词
