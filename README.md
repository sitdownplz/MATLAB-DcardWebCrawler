# MATLAB 狄卡文章爬蟲 (Dcard Web Crawler)

此程式碼使用 Dcard API 做文章資料撈取以及使用開源中文斷詞模組 jieba
將撈取的文章內容做簡單視覺化

![script snapshot](https://i.imgur.com/zt8XE0P.png)

---
版本號 Version Dev.0 (測試版本 R2021a)
---
  
### MATLAB工具箱需求 (MATLAB Toolbox Requirement)
* [文本分析工具箱 Text Analytics Toolbox](https://www.mathworks.com/help/textanalytics/)
### Python 模組需求 (Python Module Requirement)
* [結巴中文斷詞模組 jieba](https://github.com/fxsjy/jieba)
 

#### 參數說明 :
    - forumsList: 抓取Dcard看板列表
    - forum: 目標抓取看板
    - isPopular: 是否抓取看板熱門文章
    - limit: 單次抓取文章數量限制
    - iter: 抓取次數
#### MATLAB 支援版本
    - R2020b
    - R2021a
    - R2021b
#### Python 版本
    Python 3.7
### 其他 (Ref.)
 狄卡 Dcard API: 
 https://www.dcard.tw/service/api/v2/
 
 在MATLAB中使用自訂義Python模組 Call User-Defined Python Module:
 https://www.mathworks.com/help/matlab/matlab_external/call-user-defined-custom-module.html
