# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/Blog-With-GitHub-Boilerplate/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": False,
    "repo": ""
}

# 站点设置
site_name = "Minhua Li"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-18T16:51+08:00"
author = "MINHUA LI"
email = "LEEMMMHHHH@GMAIL.COM"
author_homepage = "https://www.imalan.cn"
description = "Here is an individual version of the truth"
key_words = ['anthropology', 'photography', 'health', 'blog']
language = 'zh-CN'
nav = [
    {
        "name": "Home",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "Bio",
        "url": "${site_prefix}bio/",
        "target": "_self"
    },
    {
        "name": "Writings",
        "url": "${site_prefix}writings/",
        "target": "_self"
    },
    {
     "name": "Photography",
        "url": "${site_prefix}photography/",
        "target": "_self"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
