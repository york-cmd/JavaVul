from vul import requests_config

requests_list = [
    {
        'api': name,
        'name': details['name'],
        'method': details['method'],
        'url': details['url'],
        'type': '攻击' if details['type'] == 'attack' else ('正常' if details['type'] == 'normal' else '修复')
    }
    for name, details in requests_config.items()
]

# Sorting the list based on 'type'
requests_list_sorted = sorted(requests_list, key=lambda x: x['type'])

# Creating Markdown table with 'name' field included
markdown_table_with_name = "| 接口 | 漏洞名字 | 请求方法 | url | 接口类型 |\n"
markdown_table_with_name += "| :----------------------------------------: | :---------------------------------------------------------: | -------- | :----------------------------------------------------------: | :------: |\n"
for item in requests_list_sorted:
    markdown_table_with_name += "| {api} | {name} | {method} | {url} | {type} |\n".format(**item)

print(markdown_table_with_name)