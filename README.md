## Common Voice 句子收集

- 粵語版首頁：[commonvoice.mozilla.org/yue](https://commonvoice.mozilla.org/yue)
- 句子收集器統計：[STATISTICS](https://commonvoice.mozilla.org/sentence-collector/#/yue/stats)
- 所有通過審核嘅句子：[common-voice/server/data/yue/sentence-collector.txt](https://github.com/common-voice/common-voice/blob/main/server/data/yue/sentence-collector.txt)

目前抌落去 common voice 嘅句子都要符合以下規範：

1. 字形上無需統一，並唔需要 OpenCC 字形
2. 用字符合標準粵文用字，語氣詞用字參考 https://jyutping.org/blog/particles/
   - 例如 _on9 仔唔好亂 up 嘢_ 應該改成 _戇鳩仔唔好亂噏嘢_
3. 句子唔應該太長，儘量保持 30 個字以內
4. 儘量以標準粵語（廣州話）為語體，可以加入少量其他片區嘅粵語，但係要保證用字一致。
5. 儘量少用中英夾雜嘅句子，例如：
   - 可以接受嘅中英夾雜嘅句子：我喺 Facebook 上面開個咗新帖講嘢
   - 唔可以接受嘅中英夾雜嘅誒句子：我喺 Facebook 上面 send 咗個新 post 講嘢

我哋暫時需要保證 common voice 嘅語料係冇混合語言嘅，之後再考慮加入中英夾雜語料嘅問題。

## 清理規範

[How-to](https://commonvoice.mozilla.org/sentence-collector/#/how-to)

加入 Common Voice 嘅句子要排除版權問題，而且要做下面嘅規範化清洗：

1. 冇數字：句子入面唔可以有「2049」，要轉成「二零四九」或者「兩千零四十九」
2. 冇縮寫：一啲英文縮寫譬如「ICE」既可以讀成 /ai si i/ 又可以讀成 /ais/，會造成唔一致
3. 冇標點：多餘標點符號同埋 emoji 都應該刪除
4. 外國文字：呢點需要另外討論，因爲香港粵語有大量英文詞，所以可能無法避免
5. 長度：mozilla 要求唔可以超過 14 個詞，呢個有待討論
6. 句子必須冇語病、冇錯別字而且可讀。

## 清理步驟

簡單嚟講，所有嘅句子必須係「可讀嘅」。呢個「可讀」包含咗幾個層面嘅意思，首先係通順清晰冇語病，然後係適合做 ASR 語料。具體有下面幾個要求。

#### 1 意義清晰冇語病

呢個係必需條件，句子一定要係清晰流暢且意義清晰。如果一句話九唔搭八，或者因為缺少上下文所以唔知喺度講咩嘅話，可以將佢改寫成通順易明嘅句子，或者直接清走。例如下面呢啲句子：

| 例句                   | 説明                                     | 操作                    |
| ---------------------- | ---------------------------------------- | ----------------------- |
| _貿字到底算侯仲係豪啊_ | 意義不明                                 | 刪                      |
| _焗佢過台灣發為囉_     | 唔知講乜                                 | 刪                      |
| _但係基本唔用咗_       | 病句，似乎係普通話母語者學粵語嘅錯誤用法 | 改寫成 _但係基本唔用嘞_ |

#### 2 唔可以有官話成分或者官粵夾雜

我哋嘅句子必須係純粵語句子，**唔可以有粵語普通話/國語混雜或者書面語混雜嘅文本**，否則會影響個語料庫數據質量。

| 例句           | 説明                       | 操作                                    |
| -------------- | -------------------------- | --------------------------------------- |
| _好像挺嚴重嘅_ | 「好像」同「挺」都係普通話 | 改寫成 _好似幾嚴重嘅_                   |
| _又不關我事_   | 「不」係普通話             | 改成 _又唔關我事_                       |
| _似乎還夠用？_ | 「還」係普通話             | 改成 _似乎都夠用？_ 或者 _似乎仲夠用？_ |
| _不覺得好看啊_ | 成句話係普通話             | 改成 _我又唔覺得好睇噃_ 或者刪          |

#### 3 句子必須【讀出後可理解】而唔係【文字交流型】句子

ASR 語料係為咗訓練模型學識「語音」到「文字」嘅轉換，呢度隱含咗一個前提，就係段語音係可以被人理解而轉換成文字嘅。而有一啲句子屬於「文字交流型」句子，佢哋承載嘅信息同文字符號本身相關，而呢啲信息係唔可能從語音中分辨出嚟嘅。例如下面呢幾個句子：

| 例句                 | 説明                                                                        | 操作 |
| -------------------- | --------------------------------------------------------------------------- | ---- |
| 祇祗二字相通         | 句話讀出嚟係「zi2 zi2 二字相通」，正常人冇可能聽得出「zi2 zi2」係乜嘢嚟嘅   | 刪   |
| 你哋寫為字定爲字多？ | 句話讀出嚟係「你哋寫 wai4 字定 wai4 字多」，冇人會聽得明個「wai4」係邊隻字  | 刪   |
| 支整定係姿整？       | 句話讀出嚟係「zi1 整定係 zi1 整」，雖然明個意思但係冇可能判斷得出佢係邊隻字 | 刪   |

呢啲句子都有個共同點，就係「睇文字都睇得明，但係如果冇文字，齋讀出嚟畀你聽，你就估唔到佢講緊乜」。呢啲就係「文字交流型」句子，佢哋都係唔適合做 ASR 語料嘅句子，應該改寫或者鏟走。

#### 4 檢查錯別字同用字錯誤

語音識別用嘅句子唔可以有錯別字或者用錯字，我哋都唔想語音輸入法會打一柞錯別字出嚟。粵文中常見嘅錯別字可以可以參考呢個表：[粵文常見錯別字](https://jyutping.org/blog/typo/)。下面係啲有錯別字嘅例句，都係應該留意同清洗嘅：

| 例句                   | 説明                        | 操作                          |
| ---------------------- | --------------------------- | ----------------------------- |
| 我覺得唔駛理佢嘅       | 「駛」係錯別字              | 改成 _我覺得唔使理佢嘅_       |
| 唔翻學嘅時候你都無上堂 | 「翻」「無」都唔啱用字標準  | 改成 _唔返學嘅時候你都冇上堂_ |
| 我屋企唔係果度         | 「係」同「果」都係錯別字    | 改成 _我屋企唔喺嗰度_         |
| 揾佢揾到我僕街         | 「僕」讀 buk6，應該係「仆」 | 改成 _揾佢揾到我仆街_         |

#### 5 唔可以有多餘標點符號同特殊符號

| 例句                    | 説明           | 操作                          |
| ----------------------- | -------------- | ----------------------------- |
| 我估得啩。。。。。      | 連續幾個句號   | 改成 _我估得啩_               |
| 《集韻》本書            | 唔可以有書名號 | 改成 _集韻本書_               |
| 因為我學廣州話 先得兩日 | 唔可以有空格   | 改成 _因為我學廣州話先得兩日_ |

#### 6 留意句子內容

| 例句                   | 説明           | 操作 |
| ---------------------- | -------------- | ---- |
| 啲非洲黑鬼都係廢青嚟嘅 | 敏感、冒犯言論 | 刪   |
| 信閪基督咩             | 敏感、冒犯言論 | 刪   |

ASR 語料庫允許有少量粗口出現，所以唔需要刪走所有含有「屌閪鳩撚𨳍」嘅句子。
