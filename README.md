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

## Common Voice 句子收集器輸入要求

[How-to](https://commonvoice.mozilla.org/sentence-collector/#/how-to)

加入 Common Voice 嘅句子要排除版權問題，而且要做下面嘅規範化清洗：

1. 冇數字：句子入面唔可以有「2049」，要轉成「二零四九」或者「兩千零四十九」
2. 冇縮寫：一啲英文縮寫譬如「ICE」既可以讀成 /ai si i/ 又可以讀成 /ais/，會造成唔一致
3. 冇標點：多餘標點符號同埋 emoji 都應該刪除
4. 外國文字：呢點需要另外討論，因爲香港粵語有大量英文詞，所以可能無法避免
5. 長度：mozilla 要求唔可以超過 14 個詞，呢個有待討論
6. 句子必須冇語病、冇錯別字而且可讀。
