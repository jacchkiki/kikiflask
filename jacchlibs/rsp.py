import random,json

#命名一個類別 class
class rsp:
    #定義 MEMBER
    result="rock","scissior","paper"

    #RSP 被產生時__init__ : init=initial 初始化
    def __init__(self): 
        pass

    #產生隨機結果
    def random_result(self):
        #n = 亂數.亂數整數（0,2）
        n=random.randint(0,2)
        #回傳 n
        return n
    
    #取出上面的結果
    def random_result_show(self):
        
        #self=>物件自己，使用裡面的方法 random_result
        n=self.random_result()

        #從結果取出 成員結果
        print (self.result[n])

    #取結果，然後串成JSON
    def random_result_json(self):
        #產生結果
        n=self.random_result() 
        
        #放到json status 結果
        res={"status":"0","data":self.result[n]} 
        #轉成JSON
        return json.dumps(res) 
 
