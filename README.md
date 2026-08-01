<img width="735" height="1280" alt="1" src="https://github.com/user-attachments/assets/1a00a893-4c94-482e-8ff1-7fabaefd564c" /><img width="735" height="1280" alt="image" src="https://github.com/user-attachments/assets/26a241bc-8c74-4983-b813-1e0d11874e81" /><h1 align="center">🧠 Stress Check Bot</h1> <p align="center">A Telegram bot for psychological stress self-assessment among students</p> <p align="center"> <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/aiogram-3.x-2CA5E0?style=flat"/> <img src="https://img.shields.io/badge/DB-SQLite-003B57?style=flat&logo=sqlite&logoColor=white"/> </p>           

**🖼️ Screenshots**            
<table> <tr> <td align="center"><b>Bot header</b><br/><!-- ![Bot header]            
<img width="735" height="1280" alt="1" src="https://github.com/user-attachments/assets/9666fb5d-499c-4fc5-9d5b-6580ff80eeb8" /> --></td> <td align="center"><b>Start message</b><br/><!-- ![Start message]               
<img width="855" height="1280" alt="2" src="https://github.com/user-attachments/assets/9910d769-a623-4a5d-b3d8-f00f834d34b0" />
--></td> </tr> <tr> <td align="center"><b>SOS button</b><br/><!-- ![SOS button]              
<img width="1170" height="478" alt="3" src="https://github.com/user-attachments/assets/0649337e-63a4-443f-ac9d-93eb229a4e79" />
<img width="972" height="1280" alt="4" src="https://github.com/user-attachments/assets/386af106-df92-42a3-8a23-5db094aa2a84" />
--></td> <td align="center"><b>Answering a question</b><br/><!-- ![Answering a question]                 
<img width="1169" height="1121" alt="5" src="https://github.com/user-attachments/assets/f6930390-b446-4ffb-8f3c-ffb9238e21d8" />
<img width="625" height="1280" alt="6" src="https://github.com/user-attachments/assets/198a0444-fbd5-4b6f-ae36-0d255358a36a" />
--></td> </tr> <tr> <td align="center" colspan="2"><b>Final result</b><br/><!-- ![Final result]                 
<img width="622" height="1280" alt="7" src="https://github.com/user-attachments/assets/80de4c8e-934b-4825-b10c-b12824e4026c" />
<img width="620" height="1280" alt="8" src="https://github.com/user-attachments/assets/5c5c73ba-8b85-4abc-a540-67afc7936060" />
--></td> </tr> </table>

**📖 About the project**               

The bot walks the user through a short 15-question survey to help them reflect on their current emotional state, then gives personalized recommendations based on the total score.               

This is a from-scratch Python backend rebuild of a psychological questionnaire originally prototyped in a no-code flow builder, now with real data persistence.           

⚠️ The bot is not a medical diagnostic tool and does not replace a consultation with a specialist — this is stated honestly inside the bot itself.         

**✨ Features**            
• 📋 A step-by-step survey of 15 questions with 5 answer options (Yes / Leaning yes / Not sure / Leaning no / No), each carrying its own point weight           
• 📊 Automatic scoring (0–60) and matching to one of three results with personalized recommendations              
• 🆘 A persistent emergency-help button — works at any point in the conversation and immediately shows a crisis hotline, without waiting for the survey to finish         
• 🔒 A disclaimer about confidentiality and the nature of the bot shown upfront            
• 💾 Test results saved to SQLite for later analysis (only the final score is stored — not the individual answers)               

**🛠️ Tech stack**        
**Component**  |	**Technology**       
Language	| Python 3.11+          
Telegram framework	| aiogram 3.x          
Data storage	| SQLite         
Configuration |	python-dotenv           

**📁 Project structure**            
margaritazhogolantistressbot/                 
├── bot.py              # entry point, handlers and dialogue logic                   
├── questions.py        # questions, answer weights and result texts                 
├── database.py         # SQLite storage                   
├── requirements.txt                    
├── .env.example        # template for the bot token (and optional proxy)                 
└── .gitignore                  
 
**▶️ Running locally**          
bash             
git clone https://github.com/margaritazhogol/margaritazhogolantistressbot.git           
cd margaritazhogolantistressbot              

python -m venv .venv           
source .venv/bin/activate   # Windows: .venv\Scripts\activate           

pip install -r requirements.txt          

cp .env.example .env            
# add your bot token from @BotFather to .env           

python bot.py           

**☁️ Deploying on PythonAnywhere (free tier)**           
1. Sign up at pythonanywhere.com (free Beginner account)              
2. Clone the repository through a **Bash console:**           
bash              
   git clone https://github.com/margaritazhogol/margaritazhogolantistressbot.git             
   cd margaritazhogolantistressbot              
3. Install dependencies (needed for proxy support on the free tier too):            
bash              
   pip install --user -r requirements.txt            
4. Create .env with your real bot token, **plus** a proxy setting — free PythonAnywhere accounts only reach the internet through their own HTTP proxy:            
   BOT_TOKEN=your_token_here               
   PROXY_URL=http://proxy.server:3128            
5. Run the bot:            
bash           
   python3 bot.py         

**Free-tier limitation, to be transparent:** PythonAnywhere's free plan does not include a true "Always-on task" (that's a paid feature, from $5/month on the Hacker plan). On the free tier the bot only stays online for as long as the console stays open — PythonAnywhere doesn't guarantee console uptime and may recycle it after a few hours to a couple of days. For a portfolio demo, that's fine — just reopen the console and run python3 bot.py again before showing it to someone. For real 24/7 uptime, an Always-on task on a paid plan is the reliable option.                 

**🧪 Testing**            

Verified during development:          

• correct scoring across all answer combinations         
• transitions between all three result ranges         
• the 🆘 button working at any point in the test, including mid-survey          
• protection against re-answering an already-answered question         
<p align="center">Python • aiogram • 2026</p>            
