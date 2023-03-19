[English](https://github.com/cycleapple/StoryGenerator/blob/main/README.md) | 繁體中文

# 小故事產生器

這是一個簡單的 Flask 應用程式，根據使用者提供的主題產生小故事。這個應用程式使用 OpenAI GPT-3 API 來生成小說，讓使用者可以選擇英文或繁體中文語言。

## 安裝

為了在電腦上使用這個應用程式，你必須先安裝 Python 3 和需要的依賴套件。你可以透過以下指令安裝依賴套件：

```
pip install -r requirements.txt
```


除此之外，你也需要在這個專案的根目錄建立一個 `.env` 檔案，並在這個檔案中加入你的 OpenAI API 金鑰，格式如下：


````
OPENAI_API_KEY=<your-api-key>
````


請把 `<你的 API 金鑰>` 改為你真實的金鑰，你可以在 OpenAI 網站上申請 API 金鑰。

當你完成以上步驟之後，你可以透過以下指令來啟動這個應用程式：


````
python app.py
````


接著，你可以在網頁瀏覽器中輸入 `http://localhost:5000` 來使用這個應用程式。

## 用法

你可以在輸入欄中輸入一個主題，然後選擇語言選項（英文或繁體中文）來產生一篇小故事。當你按下「產生」按鈕後，這個應用程式會顯示載入動畫並等待小說生成。當小說產生完畢之後，它會顯示在網頁上。

## 貢獻者

這個應用程式由 [MingTu](https://github.com/cycleapple) 創建。它使用了 [OpenAI GPT-3 API](https://openai.com/api/) 來產生小說，並使用 [Flask](https://flask.palletsprojects.com/en/2.1.x/) 和 [Bootstrap](https://getbootstrap.com/) 來開發。

## 授權

這個應用程式是根據 [MIT 授權](LICENSE) 發布。你可以在遵守授權條款的情況下自由使用和修改這個應用程式，
