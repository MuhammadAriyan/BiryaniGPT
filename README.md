## 🍛 BiryaniGPT  
### *Spicing Up Conversations,One Byte at a Time!*  

BiryaniGPT is a fun and interactive AI assistant designed to chat with users while adding a little kitchen magic!🧑‍🍳✨  

---

## 🚀 Features  
- 🤖 **AI-Powered Chat** using Mistral AI  
- 🎭 **Random Food Emojis** for user interactions  
- 🎨 **Styled UI** with a gradient title and custom design  
- 🍽️ **Easy Setup & Customization**  

---

## 🛠 Installation  

1️⃣ **Clone the Repository**  
```bash
git clone https://github.com/yourusername/BiryaniGPT.git
cd BiryaniGPT
```

2️⃣ **Install Dependencies**  
```bash
pip install -r requirements.txt
```
3️⃣ **Set Up Environment Variables**  
Create a `.env` file and add:  
```
agent_id=your_mistral_agent_id
api_key=your_mistral_api_key
```

4️⃣ **Run the App**  
```bash
streamlit run app.py
```

---

## 🎨 Customization  

🔹 **Change the Page Favicon**  
Modify this line in `app.py`:  
```python
st.set_page_config(page_icon='🍕')  # Change emoji/icon
```


🔹 **Add More Emojis**  
Update the `randomEmoji()` function:  
```python
ranEmojiList = ['🍔', '🍟', '🥑', '🍩', '🌮', '🍉']
```

---

## 📜 License  
This project is open-source. Feel free to modify and contribute!  

---

### **Enjoy Cooking & Chatting with BiryaniGPT!** 🍛🔥  

Let me know if you need any tweaks! 🚀💖
