# -- coding: utf-8 --

handles = [
    {
        'name': 'vPopReg4',
        'regex': [
            'mov     ecx, dword ptr [ebp]',
            'add     ebp, 0x4',
            'mov     dword ptr [esp+eax], ecx'
        ],
        'register':
            {
                'mov     dword ptr [esp+eax], ecx': ['eax', 'ecx']
            }
    },
    {
        'name': 'vPopReg4',
        'regex': [
            'mov     ecx, dword ptr [ebp]',
            'lea     ebp, dword ptr [ebp+0x4]',
            'mov     dword ptr [esp+eax], ecx'
        ],
        'register':{
            'mov     dword ptr [esp+eax], ecx': ['eax', 'ecx']
        }
    },
    {
        'name': 'vPopReg2',
        'regex': [
            'mov     cx, word ptr [ebp]',
            'mov     word ptr [esp+eax], cx'
        ],
        'register':{
            'mov     word ptr [esp+eax], cx': ['eax', 'ecx']
        },
        'remark':
            '''弹出2字节寄存器
        从指令中取出1字节立即数作为寄存器索引，把栈顶2字节弹出到寄存器'''
    },
    {
        'name': 'vPopReg1',
        'regex': [
            'mov     cx, word ptr [ebp]',
            'mov     byte ptr [esp+eax], cl '
        ],
        'register':{
            'mov     byte ptr [esp+eax], cl ': ['eax', 'ecx']
        },
        'remark':
            '''弹出1字节寄存器
从指令中取出1字节立即数作为寄存器索引，把栈顶2字节作为1字节弹出到寄存器'''
    },
    {
        'name': 'vPushReg4',
        'regex': [
            'mov     eax, dword ptr [esp+eax]',
            'lea     ebp, dword ptr [ebp-0x4]',
            'mov     dword ptr [ebp], eax'
        ],
        'register':{
            'mov     eax, dword ptr [esp+eax]': ['eax'],
            'mov     dword ptr [ebp], eax': ['eax'],
        }
    },
    {
        'name': 'vPushReg4',
        'regex': [
            'mov     eax, dword ptr [esp+eax]',
            'sub     ebp, 0x4',
            'mov     dword ptr [ebp], eax'
        ],
        'register':{
            'mov     eax, dword ptr [esp+eax]': ['eax'],
            'mov     dword ptr [ebp], eax': ['eax']
        }
    },
    {
        'name': 'vReadMem4',
        'regex': [
            'mov     ecx, dword ptr [ebp]',
            'mov     eax, dword ptr ss:[ecx]',
            'mov     dword ptr [ebp], eax'
        ],
        'remark':
            '''读取段4字节内存
        以栈顶4字节为地址读取4字节内容保存到栈顶'''
    },
    {
        'name': 'vWriteMemSs4',
        'regex': [
            'mov     ecx, dword ptr [ebp]',
            'mov     eax, dword ptr [ebp+0x4]',
            'mov     dword ptr ss:[ecx], eax'
        ],
        'register':{
            'mov     dword ptr ss:[ecx], eax':['ecx','eax']
        },
        'remark':
            '''写入SS段4字节内存
以栈顶4字节为地址，栈顶+4 4字节为内容写入SS段内存，弹出8字节'''
    },
    {
        'name': 'vAdd4',
        'regex': [
            'mov     eax, dword ptr [ebp]',
            'mov     ecx, dword ptr [ebp+0x4]',
            'add     eax, ecx',
            'mov     dword ptr [ebp+0x4], eax',
            'pushfd',
        ],
        'register':{
            'add     eax, ecx': ['eax', 'ecx'],
            'mov     dword ptr [ebp+0x4], eax':['eax']
        },
        'remark':
            '''4字节加法
栈顶4字节和栈顶+4 4字节相加，结果保存到栈顶+4，标志4字节保存到栈顶'''
    },
    {
        'name': 'vAdd2',
        'regex': [
            'mov     ax, word ptr [ebp]',
            'mov     cx, word ptr [ebp+0x2]',
            'add     ax, cx',
            'mov     word ptr [ebp+0x4], ax',
            'pushfd',
        ],
        'register':{
            'add     ax, cx': ['eax', 'ecx'],
            'mov     word ptr [ebp+0x4], eax':['eax']
        },
        'remark':
            '''2字节加法
栈顶2字节和栈顶+2 2字节相加，压入2字节后把结果保存到栈顶+4，标志4字节保存到栈顶'''
    },
    {
        'name': 'vPopVEsp',
        'regex': [
            'mov     ebp, dword ptr [ebp]',
        ],
        'remark':
            '''弹出vESP
把栈顶4字节弹出到vESP（栈顶指针）'''
    },
    {
        'name': 'vPushImm4',
        'regex': [
            'sub     ebp, 0x4',
            'mov     dword ptr [ebp], eax',
        ],
        'register':{
            'mov     dword ptr [ebp], eax': ['eax']
        },
        'remark':
            '''4字节立即数压栈
从指令中取出4字节立即数压入栈顶'''
    },
    {
        'name': 'vPushImm4',
        'regex': [
            'lea     ebp, dword ptr [ebp-0x4]',
            'mov     dword ptr [ebp], eax',
        ],
        'register':{
            'mov     dword ptr [ebp], eax': ['eax']
        },
        'remark':
            '''4字节立即数压栈
从指令中取出4字节立即数压入栈顶'''
    },
    {
        'name': 'vNand4',
        'regex': [
            'not eax',
            'not ecx',
            'and     eax, ecx',
            'mov     dword ptr [ebp+0x4], eax',
            'pushfd'
        ],
        'register':{
            'not eax': ['eax'],
            'not ecx': ['ecx'],
            'mov     dword ptr [ebp+0x4], eax':['eax']
        },
        'remark':
            '''4字节与非
栈顶4字节和栈顶+4 4字节做与非运算，结果保存到栈顶+4，标志4字节保存到栈顶'''
    },
    {
        'name': 'vNand2',
        'regex': [
            'not ax',
            'not cx',
            'and     ax, cx',
            'mov     word ptr [ebp+0x4], ax',
            'pushfd'
        ],
        'register':{
            'not ax': ['eax'],
            'not cx': ['ecx'],
            'mov     word ptr [ebp+0x4], ax':['eax']
        },
        'remark':
            '''2字节与非
栈顶2字节和栈顶+2 2字节做与非运算，压入2字节后把结果保存到栈顶+4，标志4字节保存到栈顶'''
    },
    {
        'name': 'vJmp',
        'regex': [
            'mov     esi, dword ptr [ebp]'
        ],
        'remark':
            '''弹出栈顶4字节转移目标到vEIP,然后解密后跳转'''
    },
    {
        'name': 'vPushImm2',
        'regex': [
            'mov     word ptr [ebp], ax ',
        ],
        'register':{
            'mov     word ptr [ebp], ax ': ['eax']
        },
        'remark':
            '''2字节立即数压栈
从指令中取出2字节立即数压入栈顶'''
    },
    {
        'name': 'vShl4',
        'regex': [
            'SHL EAX,CL',
            'MOV DWORD PTR [EBP+0x4],EAX',
            'PUSHFD',
        ],
        'register':{
            'SHL EAX,CL': ['eax', 'ecx'],
            'MOV DWORD PTR [EBP+0x4],EAX':['eax']
        },
        'remark':
            '''4字节逻辑左移
栈顶4字节内容，栈顶+4 2字节作为1字节移位数做逻辑左移，压入2字节后把结果保存到栈顶+4，标志4字节保存到栈顶'''
    },
    {
        'name': 'vShl1',
        'regex': [
            'SHl al,CL',
            'MOV WORD PTR [EBP+0x4],ax',
            'PUSHFD',
        ],
        'register':{
            'SHl al,CL': ['eax', 'ecx'],
            'MOV WORD PTR [EBP+0x4],ax':['eax']
        },
        'remark':
            '''1字节逻辑左移
栈顶2字节作为1字节内容，栈顶+2 2字节作为1字节移位数做逻辑左移，压入2字节后把结果作为2字节保存到栈顶+4，标志4字节保存到栈顶'''
    },
    {
        'name': 'vShl2',
        'regex': [
            'SHl ax,CL',
            'MOV WORD PTR [EBP+0x4],ax',
            'PUSHFD',
        ],
        'register':{
            'SHl ax,CL': ['eax', 'ecx'],
            'MOV WORD PTR [EBP+0x4],ax':['eax']
        },
        'remark':
            '''2字节逻辑左移
栈顶2字节内容，栈顶+2 2字节作为1字节移位数做逻辑左移，压入2字节后把结果保存到栈顶+4，标志4字节保存到栈顶'''
    },
    {
        'name': 'vShr4',
        'regex': [
            'SHr EAX,CL',
            'MOV DWORD PTR [EBP+0x4],EAX',
            'PUSHFD',
        ],
        'register':{
            'SHr EAX,CL': ['eax', 'ecx'],
            'MOV DWORD PTR [EBP+0x4],EAX':['eax']
        },
        'remark':
            '''4字节逻辑右移
栈顶4字节内容，栈顶+4 2字节作为1字节移位数做逻辑右移，压入2字节后把结果保存到栈顶+4，标志4字节保存到栈顶'''
    },
    {
        'name': 'vShr1',
        'regex': [
            'SHr al,CL',
            'MOV WORD PTR [EBP+0x4],ax',
            'PUSHFD',
        ],
        'register':{
            'SHr al,CL': ['eax', 'ecx'],
            'MOV WORD PTR [EBP+0x4],ax':['eax']
        },
        'remark':
            '''1字节逻辑右移
栈顶2字节作为1字节内容，栈顶+2 2字节作为1字节移位数做逻辑右移，压入2字节后把结果作为2字节保存到栈顶+4，标志4字节保存到栈顶'''
    },
    {
        'name': 'vShr2',
        'regex': [
            'SHr ax,CL',
            'MOV WORD PTR [EBP+0x4],ax',
            'PUSHFD',
        ],
        'register':{
            'SHr ax,CL': ['eax', 'ecx'],
            'MOV WORD PTR [EBP+0x4],ax':['eax']
        },
        'remark':
            '''2字节逻辑右移
栈顶2字节内容，栈顶+2 2字节作为1字节移位数做逻辑右移，压入2字节后把结果保存到栈顶+4，标志4字节保存到栈顶'''
    },
]