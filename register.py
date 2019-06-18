# -- coding: utf-8 --
# 寄存器


class Reg:
    eax = ''
    ebx = ''
    ecx = ''
    edx = ''
    esi = ''
    edi = ''
    esp = ''
    ebp = ''
    flag = ''

    def reg_step(self, code):
        infos = code.info.split(", ")
        for info in infos:
            if info.strip() == '':
                continue
            info_parts=info.split("=")
            if len(info_parts) == 2:
                if info_parts[0] == 'ESP':
                    self.esp = info_parts[1]
                elif info_parts[0] == 'EAX':
                    self.eax = info_parts[1]
                elif info_parts[0] == 'EBX':
                    self.ebx = info_parts[1]
                elif info_parts[0] == 'ECX':
                    self.ecx = info_parts[1]
                elif info_parts[0] == 'EDX':
                    self.edx = info_parts[1]
                elif info_parts[0] == 'EDI':
                    self.edi = info_parts[1]
                elif info_parts[0] == 'ESI':
                    self.esi = info_parts[1]
                elif info_parts[0] == 'EBP':
                    self.ebp = info_parts[1]
                elif info_parts[0] == 'FL':
                    self.flag = info_parts[1]
                else:
                    print "error reg!----%s"%info
            else:
                print "error reg!----%s"%info



reg = Reg()