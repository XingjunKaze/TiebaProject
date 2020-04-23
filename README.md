# 贴吧云签到Docker版

# [非docker版](https://github.com/ghosx/TiebaProject)

## 项目简介

独立开发的基于Django的贴吧云签到网站 

作者维护的地址：http://sign.heeeepin.com/

## 安装

### 1. 安装docker

`curl -sSL https://get.docker.com | sh`

### 2. 安装docker-compose

`curl -L https://get.daocloud.io/docker/compose/releases/download/1.25.5/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && chmod +x /usr/local/bin/docker-compose`

### 3. 下载本项目

`git clone https://gitee.com/ghosx/TiebaProject.git`

`cd TiebaProject`


### 4. 启动

`docker-compose up -d`

## 常见问题

- 日志在哪？

> 统一在 /home/tieba 下

- 如何配置邮件通知？

> 修改 web/Tiebaproject/setting.py 中 EMAIL 相关配置

## 讨论群

TG： https://t.me/tiebasign

qq群： 818794879

## LICENSE

[WTFPL – Do What the Fuck You Want to Public License](http://www.wtfpl.net/about/)
