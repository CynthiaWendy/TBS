from collections import OrderedDict

CONGIF = {
    "creds":
        {
            "endpoint": "https://XXXX.us-east-1.fc.aliyuncs.com",
            "aliyun_id": "XXXX",
            "aliyun_key": "XXXX"
        },
    "func":
        {
            "name_prefix": "mytest",
            "region": "cn-east-1",
            "role_1": "acs:ram::XXXXX:role/XXXX"
        }
}


# The default path for function code

# CODE_PATH = {
#     'python2.7': './code/python',
#     'python3.6': './code/python',
#     'nodejs6.10': './code/nodejs',
#     'nodejs4.3': './code/nodejs',
#     'java8': './code/java',
# }
CODE_PATH = {
    'python3': './code',
}

"""
The template request
sleep: set a value X here. The function will sleep for X seconds before return
stat: if let the measurement function will run the basic_stat subroutine
run: pass a cmd to the measurement function. if set the measurement function
	will run the specified string as an external command.
io: pass the parameters for the IO tests
net: pass the parameters for the network throughput tests
cpu: pass the parameters for the CPU tests
cpuu: pass the parameters for the CPU utilization tests
"""
PARA_TEMP = OrderedDict()
PARA_TEMP["sleep"] = 0		# change it to 0 for quick tests
PARA_TEMP["stat"] = dict(argv=1)
PARA_TEMP["run"] = dict(cmd=str) # {'cmd': str}
PARA_TEMP["io"] = dict(rd=int, size=str, cnt=int)
PARA_TEMP["net"] = dict(port_offset=int, server_ip=str)
PARA_TEMP["cpu"] = dict(n=int)
PARA_TEMP["cpuu"] = dict(n=int)
