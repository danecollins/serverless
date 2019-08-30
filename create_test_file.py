from ailog import log_install

param_list = dict(user="Josh Moore", build="9000", date="2019-08-28")

context = {}
context['queryStringParameters'] = param_list

print(log_install(context, None))

