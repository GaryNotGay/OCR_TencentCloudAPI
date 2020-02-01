# @Author  :  lijishi
# @Contact :  lijishi@emails.bjut.edu.cn
# @Software:  Pycharm & Python 3.7
# @EditTime:  Jan 23, 2020
# @Version :  1.0
# @describe:  Sort The Tdentification Results
# @LICENSE :  GNU GENERAL PUBLIC LICENSE Version 3

'''
11:通用印刷体识别 12:通用印刷体识别（高速版）13:通用印刷体识别（高精度版） 14:通用手写体识别 15:英文识别
21:身份证识别 22:营业执照识别 23:银行卡识别 24:名片识别
31:增值税发票识别 32:运单识别
41:驾驶证识别 42:车牌识别 43:车辆VIN码识别 44:行驶证识别
51:算式识别 52:表格识别
'''

def Text_Arrange_Summary(text, mode):
    if mode == '11':  # 11:通用印刷体识别
        return Text_Arrange_General(text)
    elif mode == '12':  # 12:通用印刷体识别（高速版）
        return Text_Arrange_General(text)
    elif mode == '13':  # 13:通用印刷体识别（高精度版）
        return Text_Arrange_General(text)
    elif mode == '14':  # 14:通用手写体识别
        return Text_Arrange_General(text)
    elif mode == '15':  # 15:英文识别
        return Text_Arrange_General(text)
    elif mode == '21':  # 21:身份证识别
        return Text_Arrange_IDCard(text)
    elif mode == '22':  # 22:营业执照识别
        return Text_Arrange_BizLicense(text)
    elif mode == '23':  # 23:银行卡识别
        return Text_Arrange_BankCard(text)
    elif mode == '24':  # 24:名片识别
        return Text_Arrange_BusinessCard(text)
    elif mode == '31':  # 31:增值税发票识别
        return Text_Arrange_VatInvoice(text)
    elif mode == '32':  # 32:运单识别
        return Text_Arrange_Waybill(text)
    elif mode == '41':  # 41:驾驶证识别
        return Text_Arrange_DriverLicense(text)
    elif mode == '42':  # 42:车牌识别
        return Text_Arrange_LicensePlate(text)
    elif mode == '43':  # 43:车辆VIN码识别
        return Text_Arrange_Vin(text)
    elif mode == '44':  # 44:行驶证识别
        return Text_Arrange_VehicleLicense(text)
    elif mode == '51':  # 51:算式识别
        return Text_Arrange_Arithmetic(text)
    elif mode == '52':  # 52:表格识别
        return Text_Arrange_Table(text)
    else:
        return Text_Arrange_General(text)

#11:通用印刷体识别 12:通用印刷体识别（高速版）13:通用印刷体识别（高精度版） 14:通用手写体识别 15:英文识别
def Text_Arrange_General(text):
    return_text = ''
    for index in range(len(text)):
        if text[index:index+12] == "DetectedText":
            end = End_Query_General(text, index+16)
            return_text += text[index+16:end]
            return_text += '\n'
    return return_text

#21:身份证识别
def Text_Arrange_IDCard(text):
    return_text = ''
    for index in range(len(text)):
        if text[index:index+6] == "\"Name\"":
            return_text += '姓名：'
            end = End_Query_General(text, index+10)
            return_text += text[index+10:end]
            return_text += '\n'
        elif text[index:index+5] == "\"Sex\"":
            return_text += '性别：'
            end = End_Query_General(text, index+9)
            return_text += text[index+9:end]
            return_text += '\n'
        elif text[index:index+8] == "\"Nation\"":
            return_text += '民族：'
            end = End_Query_General(text, index+12)
            return_text += text[index+12:end]
            return_text += '\n'
        elif text[index:index+7] == "\"Birth\"":
            return_text += '出生日期：'
            end = End_Query_General(text, index+11)
            return_text += text[index+11:end]
            return_text += '\n'
        elif text[index:index+9] == "\"Address\"":
            return_text += '地址：'
            end = End_Query_General(text, index+13)
            return_text += text[index+13:end]
            return_text += '\n'
        elif text[index:index+7] == "\"IdNum\"":
            return_text += '身份证号：'
            end = End_Query_General(text, index+11)
            return_text += text[index+11:end]
            return_text += '\n'
        elif text[index:index+11] == "\"Authority\"":
            return_text += '发证机关：'
            end = End_Query_General(text, index+15)
            return_text += text[index+15:end]
            return_text += '\n'
        elif text[index:index+11] == "\"ValidDate\"":
            return_text += '证件有效期：'
            end = End_Query_General(text, index+15)
            return_text += text[index+15:end]
            return_text += '\n'
    return return_text

def Text_Arrange_IDCard_Warning(text):
    return_text = ''
    for index in range(len(text)):
        if text[index:index + 5] == "-9100":
            return_text += text[index:index+5]
            return_text += " 身份证有效日期不合法告警\n"
        elif text[index:index + 5] == "-9101":
            return_text += text[index:index+5]
            return_text += " 身份证边框不完整告警\n"
        elif text[index:index + 5] == "-9102":
            return_text += text[index:index+5]
            return_text += " 身份证复印件告警\n"
        elif text[index:index + 5] == "-9103":
            return_text += text[index:index+5]
            return_text += " 身份证翻拍告警\n"
        elif text[index:index + 5] == "-9105":
            return_text += text[index:index+5]
            return_text += " 身份证框内遮挡告警\n"
        elif text[index:index + 5] == "-9104":
            return_text += text[index:index+5]
            return_text += " 临时身份证告警\n"
        elif text[index:index + 5] == "-9106":
            return_text += text[index:index+5]
            return_text += " 身份证 PS 告警\n"
    if len(return_text) < 10:
        return_text = 'null'
    return return_text

def Text_Arrange_IDCard_IDCardCut(text):
    return_text = ''
    for index in range(len(text)):
        if text[index:index + 10] == r"\"IdCard\"":
            end = End_Query_General(text, index + 12)
            return_text = text[index + 12:end]
            break
    return return_text

def Text_Arrange_IDCard_PortraitCut(text):
    return_text = ''
    for index in range(len(text)):
        if text[index:index + 12] == r"\"Portrait\"":
            end = End_Query_General(text, index + 14)
            return_text = text[index + 14:end]
            break
    return return_text

#22:营业执照识别
def Text_Arrange_BizLicense(text):
    return_text = ''
    for index in range(len(text)):
        if text[index:index+6] == "RegNum":
            return_text += '注册号：'
            end = End_Query_General(text, index+10)
            return_text += text[index+10:end]
            return_text += '\n'
        elif text[index:index+6] == "Person":
            return_text += '法定代表人：'
            end = End_Query_General(text, index+10)
            return_text += text[index+10:end]
            return_text += '\n'
        elif text[index:index+7] == "Capital":
            return_text += '注册资本：'
            end = End_Query_General(text, index+11)
            return_text += text[index+11:end]
            return_text += '\n'
        elif text[index:index+4] == "Name":
            return_text += '公司名称：'
            end = End_Query_General(text, index+8)
            return_text += text[index+8:end]
            return_text += '\n'
        elif text[index:index+7] == "Address":
            return_text += '地址：'
            end = End_Query_General(text, index+11)
            return_text += text[index+11:end]
            return_text += '\n'
        elif text[index:index+6] == "Period":
            return_text += '营业期限：'
            end = End_Query_General(text, index+10)
            return_text += text[index+10:end]
            return_text += '\n'
        elif text[index:index+8] == "Business":
            return_text += '经营范围：'
            end = End_Query_General(text, index+12)
            return_text += text[index+12:end]
            return_text += '\n'
        elif text[index:index+4] == "Type":
            return_text += '主体类型：'
            end = End_Query_General(text, index+8)
            return_text += text[index+8:end]
            return_text += '\n'
        elif text[index:index+13] == "ComposingForm":
            return_text += '组成形式：'
            end = End_Query_General(text, index+17)
            return_text += text[index+17:end]
            return_text += '\n'
    return return_text

#23:银行卡识别
def Text_Arrange_BankCard(text):
    return_text = ''
    for index in range(len(text)):
        if text[index:index+6] == "CardNo":
            return_text += '卡号：'
            end = End_Query_General(text, index+10)
            return_text += text[index+10:end]
            return_text += '\n'
        elif text[index:index+8] == "BankInfo":
            return_text += '银行信息：'
            end = End_Query_General(text, index+12)
            return_text += text[index+12:end]
            return_text += '\n'
        elif text[index:index+9] == "ValidDate":
            return_text += '有效期：'
            end = End_Query_General(text, index+12)
            return_text += text[index+12:end]
            return_text += '\n'
    return return_text

#24:名片识别
def Text_Arrange_BusinessCard(text):
    return_text = ''
    for index in range(len(text)):
        if text[index:index + 6] == "\"Name\"":
            end = End_Query_General(text, index + 10)
            return_text += text[index + 10:end]
            return_text += '：'
        elif text[index:index + 7] == "\"Value\"":
            end = End_Query_General(text, index + 11)
            return_text += text[index + 11:end]
            return_text += '\n'
    return return_text

def Text_Arrange_BusinessCard_Picture(text):
    return_text = ''
    for index in range(len(text)):
        if text[index:index + 14] == "RetImageBase64":
            end = End_Query_General(text, index + 18)
            return_text = text[index + 18:end]
            break
    return return_text

#31:增值税发票识别
def Text_Arrange_VatInvoice(text):
    return_text = ''
    for index in range(len(text)):
        if text[index:index + 4] == "Name":
            end = End_Query_General(text, index + 8)
            return_text += text[index + 8:end]
            return_text += '：'
        elif text[index:index + 5] == "Value":
            end = End_Query_General(text, index + 9)
            return_text += text[index + 9:end]
            return_text += '\n'
    return return_text

#32:运单识别
def Text_Arrange_Waybill(text):
    return_text = ''
    for index in range(len(text)):
        if text[index:index + 5] == "Text\"":
            end = End_Query_General(text, index + 10)
            return_text += text[index + 10:end]
            return_text += '\n'
        elif text[index:index + 7] == "RecName":
            return_text += '收件人姓名'
            return_text += '：'
        elif text[index:index + 7] == "RecAddr":
            return_text += '收件人地址'
            return_text += '：'
        elif text[index:index + 6] == "RecNum":
            return_text += '收件人手机号'
            return_text += '：'
        elif text[index:index + 10] == "SenderName":
            return_text += '寄件人姓名'
            return_text += '：'
        elif text[index:index + 9] == "SenderNum":
            return_text += '寄件人手机号'
            return_text += '：'
        elif text[index:index + 10] == "SenderAddr":
            return_text += '寄件人地址'
            return_text += '：'
        elif text[index:index + 10] == "WaybillNum":
            return_text += '运单号'
            return_text += '：'
    return return_text

#41:驾驶证识别
def Text_Arrange_DriverLicense(text):
    return_text = ''
    for index in range(len(text)):
        if text[index:index + 4] == "Name":
            end = End_Query_General(text, index + 8)
            return_text += '姓名'
            return_text += '：'
            return_text += text[index + 8:end]
            return_text += '\n'
        elif text[index:index + 3] == "Sex":
            end = End_Query_General(text, index + 7)
            return_text += '性别'
            return_text += '：'
            return_text += text[index + 7:end]
            return_text += '\n'
        elif text[index:index + 11] == "Nationality":
            end = End_Query_General(text, index + 15)
            return_text += '国籍'
            return_text += '：'
            return_text += text[index + 15:end]
            return_text += '\n'
        elif text[index:index + 7] == "Address":
            end = End_Query_General(text, index + 11)
            return_text += '住址'
            return_text += '：'
            return_text += text[index + 11:end]
            return_text += '\n'
        elif text[index:index + 11] == "DateOfBirth":
            end = End_Query_General(text, index + 15)
            return_text += '出生日期'
            return_text += '：'
            return_text += text[index + 15:end]
            return_text += '\n'
        elif text[index:index + 16] == "DateOfFirstIssue":
            end = End_Query_General(text, index + 20)
            return_text += '初次领证日期'
            return_text += '：'
            return_text += text[index + 20:end]
            return_text += '\n'
        elif text[index:index + 5] == "Class":
            end = End_Query_General(text, index + 9)
            return_text += '准驾车型'
            return_text += '：'
            return_text += text[index + 9:end]
            return_text += '\n'
        elif text[index:index + 9] == "StartDate":
            end = End_Query_General(text, index + 13)
            return_text += '有效期开始时间'
            return_text += '：'
            return_text += text[index + 13:end]
            return_text += '\n'
        elif text[index:index + 7] == "EndDate":
            end = End_Query_General(text, index + 11)
            return_text += '有效期截止时间'
            return_text += '：'
            return_text += text[index + 11:end]
            return_text += '\n'
        elif text[index:index + 8] == "CardCode":
            end = End_Query_General(text, index + 12)
            return_text += '证号'
            return_text += '：'
            return_text += text[index + 12:end]
            return_text += '\n'
    return return_text

def Text_Arrange_DriverLicense_Warning(text):
    return_text = ''
    for index in range(len(text)):
        if text[index:index + 16] == "RecognizeWarnMsg":
            index_temp = index + 21
            while True:
                if index_temp > len(text)-60:
                    break
                end = End_Query_General(text, index_temp)
                return_text += text[index_temp:end]
                return_text += ' '
                if text[index_temp:end] == "WARN_DRIVER_LICENSE_COPY_CARD":
                    return_text += '复印件告警'
                elif text[index_temp:end] == "WARN_DRIVER_LICENSE_SCREENED_CARD":
                    return_text += '翻拍件告警'
                elif text[index_temp:end] == "WARN_DRIVER_LICENSE_PS_CARD":
                    return_text += 'PS告警'
                return_text += '\n'
                index_temp += len(text[index_temp:end])
                index_temp += 4
    if len(return_text) < 10:
        return_text = 'null'
    return return_text

#42:车牌识别
def Text_Arrange_LicensePlate(text):
    return_text = ''
    for index in range(len(text)):
        if text[index:index + 6] == "Number":
            end = End_Query_General(text, index + 10)
            return_text += '车牌号码：'
            return_text += text[index + 10:end]
            return_text += '\n'
    return return_text

#43:车辆VIN码识别
def Text_Arrange_Vin(text):
    return_text = ''
    for index in range(len(text)):
        if text[index:index + 3] == "Vin":
            end = End_Query_General(text, index + 7)
            return_text += 'Vin码：'
            return_text += text[index + 7:end]
            return_text += '\n'
    return return_text

#44:行驶证识别
def Text_Arrange_VehicleLicense(text):
    return_text = ''
    for index in range(len(text)):
        if text[index:index + 7] == "PlateNo":
            end = End_Query_General(text, index + 11)
            return_text += '号牌号码'
            return_text += '：'
            return_text += text[index + 11:end]
            return_text += '\n'
        elif text[index:index + 11] == "VehicleType":
            end = End_Query_General(text, index + 15)
            return_text += '车辆类型'
            return_text += '：'
            return_text += text[index + 15:end]
            return_text += '\n'
        elif text[index:index + 5] == "Owner":
            end = End_Query_General(text, index + 9)
            return_text += '所有人'
            return_text += '：'
            return_text += text[index + 9:end]
            return_text += '\n'
        elif text[index:index + 7] == "Address":
            end = End_Query_General(text, index + 11)
            return_text += '住址'
            return_text += '：'
            return_text += text[index + 11:end]
            return_text += '\n'
        elif text[index:index + 12] == "UseCharacter":
            end = End_Query_General(text, index + 16)
            return_text += '使用性质'
            return_text += '：'
            return_text += text[index + 16:end]
            return_text += '\n'
        elif text[index:index + 5] == "Model":
            end = End_Query_General(text, index + 9)
            return_text += '品牌型号'
            return_text += '：'
            return_text += text[index + 9:end]
            return_text += '\n'
        elif text[index:index + 3] == "Vin":
            end = End_Query_General(text, index + 7)
            return_text += '车辆识别代号'
            return_text += '：'
            return_text += text[index + 7:end]
            return_text += '\n'
        elif text[index:index + 8] == "EngineNo":
            end = End_Query_General(text, index + 12)
            return_text += '发动机号码'
            return_text += '：'
            return_text += text[index + 12:end]
            return_text += '\n'
        elif text[index:index + 12] == "RegisterDate":
            end = End_Query_General(text, index + 16)
            return_text += '注册日期码'
            return_text += '：'
            return_text += text[index + 16:end]
            return_text += '\n'
        elif text[index:index + 9] == "IssueDate":
            end = End_Query_General(text, index + 13)
            return_text += '发证日期'
            return_text += '：'
            return_text += text[index + 13:end]
            return_text += '\n'
        elif text[index:index + 4] == "Seal":
            end = End_Query_General(text, index + 8)
            return_text += '印章'
            return_text += '：'
            return_text += text[index + 8:end]
            return_text += '\n'
        elif text[index:index + 6] == "FileNo":
            end = End_Query_General(text, index + 10)
            return_text += '档案编号'
            return_text += '：'
            return_text += text[index + 10:end]
            return_text += '\n'
        elif text[index:index + 8] == "AllowNum":
            end = End_Query_General(text, index + 12)
            return_text += '核定人数'
            return_text += '：'
            return_text += text[index + 12:end]
            return_text += '\n'
        elif text[index:index + 9] == "TotalMass":
            end = End_Query_General(text, index + 13)
            return_text += '总质量'
            return_text += '：'
            return_text += text[index + 13:end]
            return_text += '\n'
        elif text[index:index + 10] == "CurbWeight":
            end = End_Query_General(text, index + 14)
            return_text += '整备质量'
            return_text += '：'
            return_text += text[index + 14:end]
            return_text += '\n'
        elif text[index:index + 11] == "LoadQuality":
            end = End_Query_General(text, index + 15)
            return_text += '核定载质量'
            return_text += '：'
            return_text += text[index + 15:end]
            return_text += '\n'
        elif text[index:index + 12] == "ExternalSize":
            end = End_Query_General(text, index + 16)
            return_text += '外廓尺寸'
            return_text += '：'
            return_text += text[index + 16:end]
            return_text += '\n'
        elif text[index:index + 5] == "Marks":
            end = End_Query_General(text, index + 9)
            return_text += '备注'
            return_text += '：'
            return_text += text[index + 9:end]
            return_text += '\n'
        elif text[index:index + 6] == "Record":
            end = End_Query_General(text, index + 10)
            return_text += '检验记录'
            return_text += '：'
            return_text += text[index + 10:end]
            return_text += '\n'
        elif text[index:index + 14] == "TotalQuasiMass":
            end = End_Query_General(text, index + 18)
            return_text += '准牵引总质量'
            return_text += '：'
            return_text += text[index + 18:end]
            return_text += '\n'
    return return_text

def Text_Arrange_VehicleLicense_Warning(text):
    return_text = ''
    for index in range(len(text)):
        if text[index:index + 16] == "RecognizeWarnMsg":
            index_temp = index + 21
            while True:
                if index_temp > len(text)-60:
                    break
                end = End_Query_General(text, index_temp)
                return_text += text[index_temp:end]
                return_text += ' '
                if text[index_temp:end] == "WARN_DRIVER_LICENSE_COPY_CARD":
                    return_text += '复印件告警'
                elif text[index_temp:end] == "WARN_DRIVER_LICENSE_SCREENED_CARD":
                    return_text += '翻拍件告警'
                elif text[index_temp:end] == "WARN_DRIVER_LICENSE_PS_CARD":
                    return_text += 'PS告警'
                return_text += '\n'
                index_temp += len(text[index_temp:end])
                index_temp += 4
    if len(return_text) < 10:
        return_text = 'null'
    return return_text

#51:算式识别
def Text_Arrange_Arithmetic(text):
    return_text = ''
    for index in range(len(text)):
        if text[index:index + 12] == "DetectedText":
            end = End_Query_General(text, index + 16)
            return_text += '文本内容：'
            return_text += text[index + 16:end]
            return_text += '\n'
        elif text[index:index + 6] == "Result":
            end = End_Query_General(text, index + 9)
            return_text += '运算结果：'
            return_text += text[index + 9:end-2]
            return_text += '\n'
        elif text[index:index + 14] == "ExpressionType":
            end = End_Query_General(text, index + 18)
            return_text += '算式类型：'
            if text[index + 18:end] == '1':
                return_text += '加减乘除四则'
            elif text[index + 18:end] == '2':
                return_text += '加减乘除已知结果求运算因子'
            elif text[index + 18:end] == '3':
                return_text += '判断大小'
            elif text[index + 18:end] == '4':
                return_text += '约等于估算'
            elif text[index + 18:end] == '5':
                return_text += '带余数除法'
            elif text[index + 18:end] == '6':
                return_text += '分数四则运算'
            elif text[index + 18:end] == '7':
                return_text += '单位换算'
            elif text[index + 18:end] == '8':
                return_text += '竖式加减法'
            elif text[index + 18:end] == '9':
                return_text += '竖式乘除法'
            elif text[index + 18:end] == '10':
                return_text += '脱式计算'
            elif text[index + 18:end] == '11':
                return_text += '解方程'
            else:
                return_text += '位置类型'
            return_text += '\n'
            return_text += '\n'
    return return_text

# 52:表格识别
def Text_Arrange_Table(text):
    return_text = ''
    for index in range(len(text)):
        if text[index:index + 4] == "Data":
            end = End_Query_General(text, index + 8)
            return_text += text[index + 8:end]
    return return_text


def End_Query_General(text, index):
    i = index
    while True:
        if text[i] == '\"' and text[i-1] != '\\':
            break
        else:
            i += 1
    return i
