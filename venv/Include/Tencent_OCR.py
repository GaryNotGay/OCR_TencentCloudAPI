# @Author  :  lijishi
# @Contact :  lijishi@emails.bjut.edu.cn
# @Software:  Pycharm & Python 3.7
# @EditTime:  Jan 23, 2020
# @Version :  1.0
# @describe:  Use TencentCloud API Realize OCR
# @LICENSE :  GNU GENERAL PUBLIC LICENSE Version 3

# References
# https://cloud.tencent.com/document/product/866/33515

'''
11:通用印刷体识别 12:通用印刷体识别（高速版）13:通用印刷体识别（高精度版） 14:通用手写体识别 15:英文识别
21:身份证识别 22:营业执照识别 23:银行卡识别 24:名片识别
31:增值税发票识别 32:运单识别
41:驾驶证识别 42:车牌识别 43:车辆VIN码识别 44:行驶证识别
51:算式识别 52:表格识别
'''

#身份证识别暂缓，需要添加额外按钮以及接口完善

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models

def Tencent_OCR_Summary(pic_str, mode):
    try:
        cred = credential.Credential("Your ID", "Your Secret")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "ocr.tencentcloudapi.com"
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = ocr_client.OcrClient(cred, "ap-beijing", clientProfile)

        if mode == '11': #11:通用印刷体识别
           return Tencent_OCR_Basic_Print(pic_str, client)
        elif mode == '12': #12:通用印刷体识别（高速版）
            return Tencent_OCR_Basic_Print_Fast(pic_str, client)
        elif mode == '13': #13:通用印刷体识别（高精度版）
            return Tencent_OCR_Basic_Print_HighAccurate(pic_str, client)
        elif mode == '14': #14:通用手写体识别
            return Tencent_OCR_Handwriting(pic_str, client)
        elif mode == '15': #15:英文识别
            return Tencent_OCR_English(pic_str, client)
        elif mode == '21': #21:身份证识别
            return # 废弃
        elif mode == '22': #22:营业执照识别
            return Tencent_OCR_BizLicense(pic_str, client)
        elif mode == '23': #23:银行卡识别
            return Tencent_OCR_BankCard(pic_str, client)
        elif mode == '24': #24:名片识别
            return # 废弃
        elif mode == '31': #31:增值税发票识别
            return Tencent_OCR_VatInvoice(pic_str, client)
        elif mode == '32': #32：运单识别
            return Tencent_OCR_Waybill(pic_str, client)
        elif mode == '41': #41:驾驶证识别
            return Tencent_OCR_DriverLicense(pic_str, client)
        elif mode == '42': #42：车牌识别
            return Tencent_OCR_LicensePlate(pic_str, client)
        elif mode == '43': #43：车辆VIN码识别
            return Tencent_OCR_Vin(pic_str, client)
        elif mode == '44': #44：行驶证识别
            return # 废弃
        elif mode == '51': #51:算式识别
            return Tencent_OCR_Arithmetic(pic_str, client)
        elif mode == '52': #52：表格识别
            return Tencent_OCR_Table(pic_str, client)
        else:
            return Tencent_OCR_Basic_Print(pic_str, client)

    except TencentCloudSDKException as err:
        print(err)

#11:通用印刷体识别
def Tencent_OCR_Basic_Print(pic_str, client):
    req = models.GeneralBasicOCRRequest()
    params_1 = r'{"ImageBase64":"'
    params_2 = r'","LanguageType":"auto"}'
    params = params_1 + pic_str + params_2
    # params = '{"ImageBase64":"pic_str","LanguageType":"auto"}'
    req.from_json_string(params)
    resp = client.GeneralBasicOCR(req)
    text = resp.to_json_string()
    return text

#12:通用印刷体识别（高速版）
def Tencent_OCR_Basic_Print_Fast(pic_str, client):
    req = models.GeneralFastOCRRequest()
    params_1 = r'{"ImageBase64":"'
    params_2 = r'"}'
    params = params_1 + pic_str + params_2
    # params = '{"ImageBase64":"pic_str"}'
    req.from_json_string(params)
    resp = client.GeneralFastOCR(req)
    text = resp.to_json_string()
    return text

#13:通用印刷体识别（高精度版）
def Tencent_OCR_Basic_Print_HighAccurate(pic_str, client):
    req = models.GeneralAccurateOCRRequest()
    params_1 = r'{"ImageBase64":"'
    params_2 = r'"}'
    params = params_1 + pic_str + params_2
    #params = '{"ImageBase64":"pic_str"}'
    req.from_json_string(params)
    resp = client.GeneralAccurateOCR(req)
    text = resp.to_json_string()
    return text

#14:通用手写体识别
def Tencent_OCR_Handwriting(pic_str, client):
    req = models.GeneralHandwritingOCRRequest()
    params_1 = r'{"ImageBase64":"'
    params_2 = r'"}'
    params = params_1 + pic_str + params_2
    #params = '{"ImageBase64":"pic_str"}'
    req.from_json_string(params)
    resp = client.GeneralHandwritingOCR(req)
    text = resp.to_json_string()
    return text

#15:英文识别
def Tencent_OCR_English(pic_str, client):
    req = models.EnglishOCRRequest()
    params_1 = r'{"ImageBase64":"'
    params_2 = r'"}'
    params = params_1 + pic_str + params_2
    #params = '{"ImageBase64":"pic_str"}'
    req.from_json_string(params)
    resp = client.EnglishOCR(req)
    text = resp.to_json_string()
    return text

#22:营业执照识别
def Tencent_OCR_BizLicense(pic_str, client):
    req = models.BizLicenseOCRRequest()
    params_1 = r'{"ImageBase64":"'
    params_2 = r'"}'
    params = params_1 + pic_str + params_2
    #params = '{"ImageBase64":"pic_str"}'
    req.from_json_string(params)
    resp = client.BizLicenseOCR(req)
    text = resp.to_json_string()
    return text

#23:银行卡识别
def Tencent_OCR_BankCard(pic_str, client):
    req = models.BankCardOCRRequest()
    params_1 = r'{"ImageBase64":"'
    params_2 = r'"}'
    params = params_1 + pic_str + params_2
    #params = '{"ImageBase64":"pic_str"}'
    req.from_json_string(params)
    resp = client.BankCardOCR(req)
    text = resp.to_json_string()
    return text

#31:增值税发票识别
def Tencent_OCR_VatInvoice(pic_str, client):
    req = models.VatInvoiceOCRRequest()
    params_1 = r'{"ImageBase64":"'
    params_2 = r'"}'
    params = params_1 + pic_str + params_2
    #params = '{"ImageBase64":"pic_str"}'
    req.from_json_string(params)
    resp = client.VatInvoiceOCR(req)
    text = resp.to_json_string()
    return text

#32：运单识别
def Tencent_OCR_Waybill(pic_str, client):
    req = models.WaybillOCRRequest()
    params_1 = r'{"ImageBase64":"'
    params_2 = r'"}'
    params = params_1 + pic_str + params_2
    #params = '{"ImageBase64":"pic_str"}'
    req.from_json_string(params)
    resp = client.WaybillOCR(req)
    text = resp.to_json_string()
    return text

#41:驾驶证识别
def Tencent_OCR_DriverLicense(pic_str, client):
    req = models.DriverLicenseOCRRequest()
    params_1 = r'{"ImageBase64":"'
    params_2 = r'"}'
    params = params_1 + pic_str + params_2
    #params = '{"ImageBase64":"pic_str"}'
    req.from_json_string(params)
    resp = client.DriverLicenseOCR(req)
    text = resp.to_json_string()
    return text

#42：车牌识别
def Tencent_OCR_LicensePlate(pic_str, client):
    req = models.LicensePlateOCRRequest()
    params_1 = r'{"ImageBase64":"'
    params_2 = r'"}'
    params = params_1 + pic_str + params_2
    #params = '{"ImageBase64":"pic_str"}'
    req.from_json_string(params)
    resp = client.LicensePlateOCR(req)
    text = resp.to_json_string()
    return text

#43:车辆VIN码识别
def Tencent_OCR_Vin(pic_str, client):
    req = models.VinOCRRequest()
    params_1 = r'{"ImageBase64":"'
    params_2 = r'"}'
    params = params_1 + pic_str + params_2
    #params = '{"ImageBase64":"pic_str"}'
    req.from_json_string(params)
    resp = client.VinOCR(req)
    text = resp.to_json_string()
    return text

#51:算式识别
def Tencent_OCR_Arithmetic(pic_str, client):
    req = models.ArithmeticOCRRequest()
    params_1 = r'{"ImageBase64":"'
    params_2 = r'"}'
    params = params_1 + pic_str + params_2
    #params = '{"ImageBase64":"pic_str"}'
    req.from_json_string(params)
    resp = client.ArithmeticOCR(req)
    text = resp.to_json_string()
    return text

#52：表格识别
def Tencent_OCR_Table(pic_str, client):
    req = models.TableOCRRequest()
    params_1 = r'{"ImageBase64":"'
    params_2 = r'"}'
    params = params_1 + pic_str + params_2
    #params = '{"ImageBase64":"pic_str"}'
    req.from_json_string(params)
    resp = client.TableOCR(req)
    text = resp.to_json_string()
    return text



#21:身份证识别
def Tencent_OCR_IDCard(pic_str, flag_side, flag_piccut, flag_porcut):
        cred = credential.Credential("AKIDX6Yr0xFNsFUhjdBxQjvUxJVaVCfu4bbL", "3rQXP1NUPfjX6QVLukOnwrSouqbBWfcL")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "ocr.tencentcloudapi.com"
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = ocr_client.OcrClient(cred, "ap-beijing", clientProfile)

        req = models.IDCardOCRRequest()
        params_1 = r'{"ImageBase64":"'
        if flag_side:
            params_2 = r'","CardSide":"BACK","Config":"{\"CropIdCard\":'
        else:
            params_2 = r'","CardSide":"FRONT","Config":"{\"CropIdCard\":'
        if flag_piccut:
            params_3 = r'false,\"CropPortrait\":'
        else:
            params_3 = r'true,\"CropPortrait\":'
        if flag_porcut:
            params_4 = r'false}"}'
        else:
            params_4 = r'true}"}'
        params = params_1 + pic_str + params_2 + params_3 + params_4
        #params = '{"ImageBase64":"pic_str","CardSide":"FRONT","Config":"{\\"CropIdCard\\":true,\\"CropPortrait\\":true}"}'
        req.from_json_string(params)
        resp = client.IDCardOCR(req)
        text = resp.to_json_string()
        return text

#24:名片识别
def Tencent_OCR_BusinessCard(pic_str, flag):
        cred = credential.Credential("AKIDX6Yr0xFNsFUhjdBxQjvUxJVaVCfu4bbL", "3rQXP1NUPfjX6QVLukOnwrSouqbBWfcL")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "ocr.tencentcloudapi.com"
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = ocr_client.OcrClient(cred, "ap-beijing", clientProfile)

        req = models.BusinessCardOCRRequest()
        params_1 = r'{"ImageBase64":"'
        if flag:
            params_2 = r'","Config":"{\"RetImageType\":\"PROPROCESS\"}"}'
        else:
            params_2 = r'"}'
        params = params_1 + pic_str + params_2
        #params = '{"ImageBase64":"pic_str","Config":"{\\"RetImageType\\":\\"PROPROCESS\\"}"}'
        req.from_json_string(params)
        resp = client.BusinessCardOCR(req)
        text = resp.to_json_string()
        return text

# 44：行驶证识别
def Tencent_OCR_VehicleLicense(pic_str, flag):
    cred = credential.Credential("AKIDX6Yr0xFNsFUhjdBxQjvUxJVaVCfu4bbL", "3rQXP1NUPfjX6QVLukOnwrSouqbBWfcL")
    httpProfile = HttpProfile()
    httpProfile.endpoint = "ocr.tencentcloudapi.com"
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = ocr_client.OcrClient(cred, "ap-beijing", clientProfile)

    req = models.VehicleLicenseOCRRequest()
    params_1 = r'{"ImageBase64":"'
    if flag:
        params_2 = r'","CardSide":"BACK"}'
    else:
        params_2 = r'","CardSide":"FRONT"}'
    params = params_1 + pic_str + params_2
    #  params = '{"ImageBase64":"pic_str","CardSide":"FRONT"}'
    req.from_json_string(params)
    resp = client.VehicleLicenseOCR(req)
    text = resp.to_json_string()
    return text


