# 基于Python alpine
FROM python:alpine

# 设置工作目录
WORKDIR /usr/src/app

# 将镜像中的文件复制到容器内
COPY ./app .

# 安装
RUN pip3 install -r ./requirements.txt

# 运行应用程序
CMD ["python", "app.py"]