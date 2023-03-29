# Python3 Jieba分词+词频分析 http服务镜像

## 使用 9988 端口

## 支持内容

单行、多行文本

### 使用

```python
import requests

res = requests.post(url="http://localhost:9988/", data="“结巴”中文分词：做最好的 Python 中文分词组件")
```

### 返回标准的JSON格式数组(已按词频次数由多到少排序)

```js
[["中文", 2], ["分词", 2], ["结巴", 1,], ["最好", 1,], ["Python", 1,], ["组件", 1,]]
```

### Docker-compose
```yaml
version: "3"

service:
  jieba:
    image: gzlock/http_jieba_frequency_service:latest
    restart: always
    expose: 
      - 9988
    ports:
      - "9988:9988"
```

### [Docker hub](https://hub.docker.com/r/gzlock/http_jieba_frequency_service)