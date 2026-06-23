data = {
    "毕": {
        "pinyin": "Bi",
        "meaning": "Chinese surname"
    },
    "王": {
        "pinyin": "Wang",
        "meaning": "Chinese surname"
    },
    "李": {
        "pinyin": "Li",
        "meaning": "Chinese surname"
    }
}

name = input("请输入姓氏：")

if name in data:
    print("姓氏:", name)
    print("拼音:", data[name]["pinyin"])
else:
    print("未找到该姓氏")
"张": {"pinyin": "Zhang", "meaning": "Chinese surname"},
"刘": {"pinyin": "Liu", "meaning": "Chinese surname"},
"陈": {"pinyin": "Chen", "meaning": "Chinese surname"},
"杨": {"pinyin": "Yang", "meaning": "Chinese surname"},
"赵": {"pinyin": "Zhao", "meaning": "Chinese surname"}
