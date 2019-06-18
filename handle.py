# -- coding: utf-8 --
import handles
import tool
from register import reg

neat = {
    'name': 'UNKNOWN',
    'param': [],
}

def run(handle):
    for handle_info in handles.handles:
        if rule_check(handle_info, handle):
            neat['name']=handle_info['name']
            return neat
    return neat


def rule_check(handle_info, handle):
    for rule in handle_info['regex']:
        if not code_step(rule, handle, handle_info.get('register',None)):
            return False
    return True


def reg_get(code, register):
    if register is None:
        return
    for k, v in register.items():
        if tool.compare(k, code.asm):
            for the_reg in v:
                neat['param'].append(reg.__dict__.get(the_reg))


def code_step(rule, handle, register):
    neat['name'] = 'UNKNOWN'
    neat['param'] = []
    for code in handle:
        reg_get(code, register)
        reg.reg_step(code)
        if tool.compare(rule, code.asm):
            return True
    return False

