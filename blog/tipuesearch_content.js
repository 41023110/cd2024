var tipuesearch = {"pages":[{"title":"About","text":"cmsimde 內容管理系統 倉儲: https://github.com/mdecycu/cmsimde_site 網站: https://mde.tw/cmsimde_site/ 簡報: https://mde.tw/cmsimde_site/reveal 網誌: https://mde.tw/cmsimde_site/blog","tags":"misc","url":"./pages/about/"},{"title":"2024 Spring 課程","text":"2024 Spring 網際內容管理與協同產品設計實習課程教學導引. w3-1 LaTeX 格式分工完成下列文章的英文與中文翻譯並列資料。 負責第三段 43-65page 由41023110 (introduction_orig.txt, 使用了chatgpt與劍橋辭翻譯，並用word編排翻譯段落。","tags":"w3.2","url":"./2024-Spring-w3.2-blog-tutorial.html"},{"title":"2024 Spring 課程","text":"2024 Spring 網際內容管理與協同產品設計實習課程教學導引. w2-2 如何利用近端可攜環境與外部 IPv4 開啟動態網站。 用ssh來啟動它，要克隆它去到靜態拉出putty，近端中沒有任何settings。建立之後會存在系統登錄閘，在黑窗用regedit機制跑可以使三個倉儲同步，就不怕code用完。並且有外擴ipv4等同有一個伺服器，就算在遠端去到防火牆設置ip就能進入。 用PuTTY Configuration輸入ip定github.com，在sessions也是輸入github.com，並到ssh把剛設立的ppk給予它。倉儲要在常用資料位置，讓他可以隨時啟動，啟動近端時目錄可以方便鎖定。 在ssh的credentials中的機制設置對應的資料夾中的ppk位置，在任何一台開起可攜環境後續就不會出現跑掉的問題。 save後open後會給予一把key，此key連線時是無法取得的。存取github.com的檔案要匯出在可攜環境。 若有對應的key並有open過了兩條件，那是可以有權限用ssh抓取下來。改版後就可以推回倉儲。在近端就自由了，可以啟動動態進入。之後小組可以各自獨立編輯，不會受他人干擾。 若要讓組員連接過來，要先改密碼之後查詢ip，並複製到槽中的init.py去修改，丟入外部ip儲存，使其電腦變成一台主機。在cms一次組員就可以動作了 w2-1如何用Github Codespaces維護網站內容 每一個倉儲都有 ，在完成建立組倉儲後有code就可以改版。 任何一個倉儲中都有配置code，codespaces是一個線上整合環境與replit相似，只是介面是另一個配置。在倉儲下可以建一個在主分之來建codespaces。 先啟動動態在功能表還原終端系統，並新增一個終端系統，有兩意思給指令分別啟動動態與靜態。 在開始run後要執行python3 main.py，遇到執行時沒有flask模組。就要去chmod u+x init-replit讓程式可以執行，讓他幫其安裝對應模組。最後在./init-replit。網站就會給一個阜可以開啟動態。 要在python3 mhttp.senver 啟動一個模組，因系統帶有一個動態一個靜態，靜態還有一個index，更且有一個index可以啟動，帶進編輯器。index阻礙小輸送快速，約0秒就跳進content跟index，只要用這指令啟用靜態就可以看到更改了，改版會力馬有反應。每一次阜號都是不一樣安全性高。 code每月給定數量相同，編輯可以在介面外，在上傳時開啟就好，使用完後要記得關閉，每月用量平均好就可以一直免費使用。 網站內容管理系統 使用者可以自行利用 cmsimde_site 倉儲作為 Template, 建立自己的網站內容管理系統. 引用網站網址連結的方法: cmsimde_site - 在文章中多次引用同一個網站連結時, 可以使用此種方法. https://github.com/mdecycu/cmsimde_site - 假如想要快速將網址套用 html 網站連結, 可以使用此種方法. cmsimde_site - 也可以使用 Markdown 的標準網站連結使用格式. # 引用 Python 程式的方法 for i in range(10): print(i, \"列出字串\") 也可以直接在 .md 檔案中使用 html 標註, 或加入 Javascript 或 Brython 程式碼. 從 1 累加到 100: 1 add to 100 將 iterable 與 iterator 相關說明 , 利用 Brython 與 Ace Editor 整理在這個頁面. Filename: .py Run Output 清除輸出區 清除繪圖區 Reload 從 1 累加到 100 part2: 1 add to 100 cango_three_gears BSnake AI Tetris Rotating Block Filename: .py Run Output 清除輸出區 清除繪圖區 Reload","tags":"w3","url":"./2024-Spring-w3-blog-tutorial.html"},{"title":"2024 Spring 課程","text":"2024 Spring 網際內容管理與協同產品設計實習課程教學導引. 如何用Github Codespaces維護網站內容 每一個倉儲都有 ，在完成建立組倉儲後有code就可以改版。 任何一個倉儲中都有配置code，codespaces是一個線上整合環境與replit相似，只是介面是另一個配置。在倉儲下可以建一個在主分之來建codespaces。 先啟動動態在功能表還原終端系統，並新增一個終端系統，有兩意思給指令分別啟動動態與靜態。 在開始run後要執行python3 main.py，遇到執行時沒有flask模組。就要去chmod u+x init-replit讓程式可以執行，讓他幫其安裝對應模組。最後在./init-replit。網站就會給一個阜可以開啟動態。 要在python3 mhttp.senver 啟動一個模組，因系統帶有一個動態一個靜態，靜態還有一個index，更且有一個index可以啟動，帶進編輯器。index阻礙小輸送快速，約0秒就跳進content跟index，只要用這指令啟用靜態就可以看到更改了，改版會力馬有反應。每一次阜號都是不一樣安全性高。 code每月給定數量相同，編輯可以在介面外，在上傳時開啟就好，使用完後要記得關閉，每月用量平均好就可以一直免費使用。 網站內容管理系統 使用者可以自行利用 cmsimde_site 倉儲作為 Template, 建立自己的網站內容管理系統. 引用網站網址連結的方法: cmsimde_site - 在文章中多次引用同一個網站連結時, 可以使用此種方法. https://github.com/mdecycu/cmsimde_site - 假如想要快速將網址套用 html 網站連結, 可以使用此種方法. cmsimde_site - 也可以使用 Markdown 的標準網站連結使用格式. # 引用 Python 程式的方法 for i in range(10): print(i, \"列出字串\") 也可以直接在 .md 檔案中使用 html 標註, 或加入 Javascript 或 Brython 程式碼. 從 1 累加到 100: 1 add to 100 將 iterable 與 iterator 相關說明 , 利用 Brython 與 Ace Editor 整理在這個頁面. Filename: .py Run Output 清除輸出區 清除繪圖區 Reload 從 1 累加到 100 part2: 1 add to 100 cango_three_gears BSnake AI Tetris Rotating Block Filename: .py Run Output 清除輸出區 清除繪圖區 Reload","tags":"w2","url":"./2024-Spring-w2-blog-tutorial.html"}]};