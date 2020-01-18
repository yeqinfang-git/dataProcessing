# from __future__ import print_function
# import json

def dict_generator(indict, pre=None):
    pre = pre[:] if pre else [] # 如果pre有数据，返回pre所有元素，否则返回空列表
    if isinstance(indict, dict) :# 判断 indict 是否为 dict
        for key, value in indict.items() : # 以列表返回可遍历的(键, 值) 元组数组
            if isinstance(value, dict): # 判断 值 是否为 字典
                if len(value) == 0:
                    # yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，
                    # Python 解释器会将其视为一个 generator，
                    # 调用 dict_generator（） 不会执行该函数，而是返回一个 iterable 对象！
                    yield pre+[key, '{}'] #  返回一个可迭代对象 iterable, 为列表
                else:
                    for d in dict_generator(value, pre + [key]): # 字典还有值，继续迭代
                        yield d
            elif isinstance(value, list): # 如果不是字典，判断是否为列表
                if len(value) == 0:
                    yield pre+[key, '[]']
                else:
                    for v in value:
                        for d in dict_generator(v, pre + [key]):
                            yield d
            elif isinstance(value, tuple): # 如果不是列表， 元组
                if len(value) == 0:
                    yield pre+[key, '()']
                else:
                    for v in value:
                        for d in dict_generator(v, pre + [key]):
                            yield d
            else:
                yield pre + [key, value]
    else: # 如果都不是以上的类型，直接返回值
        yield indict

jsonData = {
    "base_config":{
        "enforce":{
            "value":"0",
            "inherit":"0",
            "global":"0"
        },
        "modify":{
            "value":"0",
            "inherit":"0",
            "global":"0"
        }
    },
    "safe_control_list":{
        "list":[
            {
                "gid":"0",
                "gname":"全网计算机",
                "isactive":"1",
                "rule_id":"0",
                "rule_name":"请选择规则",
                "time_range":"所有时间",
                "time_range_id":"1",
                "policy_tpl":"33",
                "policy_tpl_id":"17",
                "isonline":"3",
                "priority":"1"
            }
        ]
    }
}

jsonData1 = {
    "detail":{
        "baseline":{
            "cancel_scheduled_task":"1",
            "comeonstage":"topwin",
            "conf_ver":2635792175,
            "conf_ver_s":"f7f8ac46##",
            "mission_id":0,
            "rules":{

            },
            "scheduled_task":"1",
            "scheduled_task_rule":{
                "autoexec_on_coundown":"1",
                "exec_countdown":"0",
                "exec_interval":"0",
                "exec_mode":"4",
                "exec_time":"*|00|*|*|*",
                "extra":{
                    "countdown_type":"3600",
                    "cycle_type":"1",
                    "every_type":"1"
                },
                "gid":0,
                "is_notice":"1",
                "is_reportback":"0",
                "module_id":3,
                "name":"",
                "notice_msg":"",
                "status":1,
                "tpl_id":420,
                "type":1
            }
        }
    },
    "id":1,
    "type":2100
}

jsonData2 = {
	"appid": "1",
	"methodname": "queryCompilerTool",
	"param": {
		"name": "ff",
		"product_category_id": "",
		"operatorId": "117"
	},
	"token": "793281F0D68342A68C73FAF7EC330811"
}

jsonData3 = {
	"persons": [{
		"id": 1,
		"name": "Number1",
		"age": 11
	}, {
		"id": "2",
		"name": "Number2",
		"age": 22
	}, {
		"id": 3,
		"name": "Number3",
		"age": 33
	}]
}

jsonData4 = {
	"code": 200,
	"persons": [{
		"id": 1,
		"name": "Number1",
		"age": 11
	}, {
		"id": 1,
		"name": "Number2",
		"age": 22
	}, {
		"id": 3,
		"name": "Number3",
		"age": 33
	}]
}

jsonData5 = {"a":1}

if __name__ == "__main__":
    # print(type(jsonData))
    # sJOSN =  str(jsonData)
    # sValue = json.loads(sJOSN)
    sValue = jsonData
    sValue1 = jsonData1
    sValue2 = jsonData2
    sValue3 = jsonData3
    sValue4 = jsonData4
    sValue5 = jsonData5
    # for i in dict_generator(sValue):
    #     print('.'.join(i[0:-1]), ':', i[-1]) # 每次都返回最后的值，格式为 a.b.c : value
    # for i in dict_generator(sValue1):
    #     print('.'.join(i[0:-1]), ':', i[-1])
    for i in dict_generator(sValue2):
        print('.'.join(i[0:-1]), ':', i[-1])
        print(i[0],":",i[-1]) # 只能显示第一层级i[0]
    print(i[::]) # 因为是迭代器，所以只显示最后一个取值
    # for i in dict_generator(sValue3):
    #     print('.'.join(i[0:-1]), ':', i[-1])
    # for i in dict_generator(sValue4):
    #     print('.'.join(i[0:-1]), ':', i[-1])
    # for i in dict_generator(sValue5):
    #     print('.'.join(i[0:-1]), ':', i[-1])
