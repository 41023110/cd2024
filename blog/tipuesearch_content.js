var tipuesearch = {"pages":[{"title":"About","text":"cmsimde 內容管理系統 倉儲: https://github.com/mdecycu/cmsimde_site 網站: https://mde.tw/cmsimde_site/ 簡報: https://mde.tw/cmsimde_site/reveal 網誌: https://mde.tw/cmsimde_site/blog","tags":"misc","url":"./pages/about/"},{"title":"2a-midag8 2024 Spring 課程","text":"2024 Spring 網際內容管理與協同產品設計實習課程教學導引. w12-1 W12 任務一 使用Siwmens NX Journal設計專案，在其中可使用NXOpen程式執行儲存格式 。在使用軟體時建議使用英文介面，因為中文翻譯的介面並不明確。 在設定選擇用語時，選擇Python方便後續網際上延伸編輯後續。 組別分配網球平衡台零件繪製，並用NXOpen Python執行。之後試著把每個零件組合起來，並且做出啟動一個程式時全部的零組件可以在一程式域內快速組合起來。 w12-2 W12 任務二 將分組倉儲設為評分子模組，直接在Repilt進行git clear、import跟git push過了。 直接在倉儲做git submodule add+分組倉儲+組別，其為做子模組的方式。後續acp確認是否有丟上成功。 後續試著子模組能否整合。 w12-3 W12 任務三 進行足球機器人網際場景模擬，在cd2024 blog上下載去年的倉儲資料，並安裝跟改過的CoppeliaSim ipv6。 要確認軟體內modules之connectivity的三個visualization stream、ws remote api server、zmq remote api server分別都是running的狀態。visualization stream是在瀏覽器上輸入埠號為23020的localhost可看到目前的模擬場景。 開啟下載到的模擬場景，有兩個程式可以執行，分別judge.py與player.py。","tags":"w12","url":"./2024-Spring-w12-blog-tutorial.html"},{"title":"2024 協同課程a-w9","text":"2024 Spring 網際內容管理與協同產品設計實習課程教學導引 w4-1 教學影片分組整理 w9協同帳號資料處理，根據老師給的範例去作出一個新的網站連結，連結內的 Ace 編輯器執行後可以正常列出班級協同相關網站。 網球平衡台PID控制與模擬。根據老師給的7z檔中6個PDF檔，閱讀後並每篇解讀寫一個文中的摘要與弊端報告。 用NX與Solvespace繪製網球台零件。並用ZMQ RemoteAPI Python 控制程式模擬鋼球平衡台場景","tags":"a-w9-41023110","url":"./2024-協同課程a-w9-41023110.html"},{"title":"2024 協同課程a-w4","text":"2024 Spring 網際內容管理與協同產品設計實習課程教學導引 w4-1 教學影片分組整理 w4 2a 分組任務 負責w3 a.b的影片 使用capcut編輯字幕與影片剪輯，把翻譯好的影片上傳到youtube並嵌入在txt，在記事本依檔照程序碼排版。上傳到組與個人downloads。","tags":"a-w4-41023110","url":"./2024-協同課程a-w4-41023110.html"},{"title":"2024 協同課程a-w1","text":"2024 Spring 網際內容管理與協同產品設計實習課程教學導引. 網站內容管理系統 使用者可以自行利用 cmsimde_site 倉儲作為 Template, 建立自己的網站內容管理系統. 引用網站網址連結的方法: cmsimde_site - 在文章中多次引用同一個網站連結時, 可以使用此種方法. https://github.com/mdecycu/cmsimde_site - 假如想要快速將網址套用 html 網站連結, 可以使用此種方法. cmsimde_site - 也可以使用 Markdown 的標準網站連結使用格式. # 引用 Python 程式的方法 for i in range(10): print(i, \"列出字串\") 也可以直接在 .md 檔案中使用 html 標註, 或加入 Javascript 或 Brython 程式碼. 從 1 累加到 100: 1 add to 100 將 iterable 與 iterator 相關說明 , 利用 Brython 與 Ace Editor 整理在這個頁面. Filename: .py Run Output 清除輸出區 清除繪圖區 Reload 從 1 累加到 100 part2: 1 add to 100 cango_three_gears BSnake AI Tetris Rotating Block Filename: .py Run Output 清除輸出區 清除繪圖區 Reload","tags":"a-w1-41023110","url":"./2024-協同課程a-w1-41023110.html"},{"title":"2024 協同課程a-w2","text":"2024 Spring 網際內容管理與協同產品設計實習課程教學導引. -1 說明甲班第一組組長如何建立 midag1 Team, 並利用 Codespaces 維護 2a-midag1 分組倉儲 終端機每個人每月都有120code小時。要push倉儲要新增終端機後，進行git add->git commit\"網頁標題\"，執行後就會直接推上不需要在轉檔。啟動靜態要在新增終端機，有python3內建模組了就可以直接http.server直接啟動埠號，8000會自動開啟瀏覽器連結，就可以直接進入到靜態。用完codespaces要在關閉code讓計時暫停。 利用 Codespaces 維護 : 一.在 GitHub Classroom 中建立組別倉儲： a.組長在 \"or create a new team\" 處以 \"midag X\" 命名組別，然後點擊 \"+create team\" 創建。 b.組員各自加入組別。 二.完成倉儲建立後： a.前往倉儲的 settings 選取 pages 進入主分支，啟動 GitHub Pages。 b.使用 Codespaces 維護內容。 三.在 Codespaces 中： a.不需要使用公用的 443 埠號，有許多終端機和埠號資源可用。 b.啟動終端機並安裝模組：執行 chmod u+x init_replit，安裝完成後會有 2GB 記憶體。 c.使用 python3 main.py 執行動態應用，並使用 8080 埠號開啟瀏覽器。 d.連結埠號會顯示亂碼，保證安全性。 e.登入後可以更改內容。 -2 說明如何利用Replit管理從 Classroom 取得的分組倉儲 一.在 Replit 中建立網站： a.使用 from url 導入資料，改成 Python 模式並 import 到分組倉儲，但在 Replit 上無法直接維護分組倉儲。 二.生成 SSH 密鑰： a.在 shell 中執行 ssh-keygen，跟 s.cycu 相同。 b.執行 pwd 確認倉儲位置在 home/runner 下。 c.使用 cd ../ 切換到 runner 目錄，執行 ls -l 查看 pub 鍵。 三.建立個人 ID： a.確認有 putty，新增 SSH 並複製 import 資料。 b.打開 puttygen.exe，生成亂數，複製內容到組長倉儲的 settings。 c.將 ID 存在 settings 和 .ssh 目錄中。 這樣就可以載入並顯示 pub key。 -3 如何利用近端可攜環境與外部 IPv4 開啟動態網站。 一.使用 SSH 啟動並克隆倉儲： a.使用 PuTTY 進入 Replit，沒有任何 settings。 b.在系統中用 regedit 使三個倉儲同步。 c.設置外擴 IPv4，使遠端可通過防火牆設置進入。 二.使用 PuTTY 設置連接： a.在 PuTTY Configuration 中輸入 github.com 作為 IP。 b.在 Sessions 和 SSH 中設置 ppk 文件。 c.將倉儲設在常用資料位置，以便隨時啟動。 三.設定 SSH 資料夾： a.在 SSH 的 credentials 中設置 ppk 文件的位置。 b.保存後 open，會給予一把 key，連線時無法取得。 四.存取 GitHub 檔案： a.匯出檔案到可攜環境，若有對應 key 且已 open，則可用 SSH 抓取並推回倉儲。 b.在近端自由啟動動態： 小組成員可以獨立編輯，不受他人干擾。 連接組員： 改密碼後查詢 IP，並複製到 init.py 中修改，設置外部 IP 儲存，使電腦變成主機。 這樣可以使組員在 CMS 中一次完成動作。","tags":"協同課程a-w2-41023110","url":"./2024-協同課程a-w2-41023110.html"}]};