import re
from collections import Counter

import jieba
from sanic import Sanic
from sanic.response import json

app = Sanic("jieba")

split = r'[\n\r]'
replace = r"[A-Za-z0-9]"


# 词频分析
@app.post("/")
async def word_frequency(request):
    c = Counter()
    lines = re.split(split, request.body.decode("utf-8"))
    for line in lines:
        # line = re.sub(replace, "", line)
        seg_list = jieba.cut(line)
        for word in seg_list:
            if len(word) > 1:
                c[word] += 1

    return json(c.most_common())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9988, access_log=False)
