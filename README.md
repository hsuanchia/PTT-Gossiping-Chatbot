# PTT-Gossiping-Chatbot
A Chat bot that use training data from PTT Gossiping

**課堂上的專題，自己做來玩的小玩具，有緣人想看我醜醜的code就拿去用吧!**

## Dataset
2021 5月份 PTT-gossiping版上的問卦文章
## Data Preprocessing
* 有效文章: 有至少1則推文、回應、噓文且標題為問卦的文章
* 推文: 最多每篇文章只取前100推文
* 將文章及其推文整理成QA型態 -> 文章標題為問題，取最佳推文為回答
  * 取最佳推文方法
    1. 統計該文章下每一則推文出現的詞
    2. 將所有出現過的詞賦予權重(出現次數即該詞彙的權重)，出現次數越多的權重越高
    3. 計算每一則推文出現的詞彙的權重和
    4. 取權重和最高的推文，權重一樣時取越早推文的
  * 最終處理完之後總計有48560筆問答
* 斷詞: CKIP
* Tokenize
  * Character based: 總共有4764個字(Q+A)
  * Word based: 總共有31565個詞(Q+A)
  * Special token: unk sos end pad
* Padding
  * Word-based
    * Question pad 到 30 個詞(最長問題有30個詞)
    * Answer   pad 到 60 個詞(最長回答有59個詞)
  * Character-based
    * Question pad 到 42 個詞(最長問題有42個詞)
    * Answer   pad 到 70 個詞(最長回答有70個詞)
## Architecture
* Word-based
![Chatbot_arch](https://user-images.githubusercontent.com/59002617/155270992-9f70092e-021a-4061-b861-cefa35093082.png)
* Character-based
![Chatbot_arch_char](https://user-images.githubusercontent.com/59002617/155271004-d1bfb20d-df8d-45e0-a777-f3d19e1a6ff4.png)
## Implementation result
* Word-based
 
![Word_based ex1](https://user-images.githubusercontent.com/59002617/155271277-72b4e6e9-759d-42e6-86c3-2a1fe1d9c019.png)
 
![Word_based ex2](https://user-images.githubusercontent.com/59002617/155271289-88ad5ff6-701b-4be9-bb2d-9d72596624d6.png)
* Character-based
 
![not HTML](https://user-images.githubusercontent.com/59002617/155271344-763c5084-ca31-4942-98ac-f1ed2ec6c0ec.jpg)
 
![train_char_example2](https://user-images.githubusercontent.com/59002617/155271398-9e2cbe09-2fee-4d08-bd8f-55e03d540610.jpg)

## Future work
* 改善取最佳推文的方法
* 資加有效資料量(現在只有用1個月)
* parameter fine-tune
* Architecture: BERT
  
  
