# Android-Intelligence
A combination of programs that allows GPT to be your Assistant for your everyday life. GPT has context and will answer any of your questions.
# Example of usage
**[Video](https://youtu.be/lFpIeRj4TjQ?si=ef5WEwang4Nyw1Qh)**
# Requirements
### [Macrodroid](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://play.google.com/store/apps/details%3Fid%3Dcom.arlosoft.macrodroid%26hl%3Den_US%26referrer%3Dutm_source%253Dgoogle%2526utm_medium%253Dorganic%2526utm_term%253Dmacrodroid%2Bplay%26pcampaignid%3DAPPU_1_vKOPZqqqBbSO7NYPsKComA4&ved=2ahUKEwiq-JKh1J6HAxU0B9sEHTAQCuMQ5YQBegQIDhAC&usg=AOvVaw0gkSlTgAaCdI1qfWfuKLI9) (free or paid version)
### [Termux](https://github.com/termux)
### [OpenAI api key](https://platform.openai.com/docs/quickstart#:~:text=First%2C%20create%20an%20OpenAI%20account,not%20share%20it%20with%20anyone.)
# Instructions 
# Termux
After installing termux give it all necessary permissions and let's continue:
1. ```pkg install python```
2. ```apt install git```
3. IMPORTANT COMMAND, NOT OPTIONAL fixes bug when installing openai python library [source](https://github.com/termux/termux-packages/issues/20039)
```
_file="$(find $PREFIX/lib/python3.11 -name "_sysconfigdata*.py")"
rm -rf $PREFIX/lib/python3.11/__pycache__
cp $_file "$_file".backup
sed -i 's|-fno-openmp-implicit-rpath||g' "$_file"
```
- Change current directory to
- ```cd /storage/emulated/0/```
- Clone github repository
```
git clone https://github.com/Sal0ID/Android-Intelligence
```
- Install requests library
- ```pip install requests```
- Install OpenAI python library.
- **THIS MAY TAKE UP TO 30 MINUTES**
- ```pip install openai```
- Then ```cd Android-Intelligence```
- ```nano main.py```
- Put in your OpenAI api key here ```openai.api_key = ""```
- After completing macrodroid instructions insert link to second trigger here
- ```trigger = "" # Link to macrodroid trigger```
- ![IMG_20240718_191906](https://github.com/user-attachments/assets/d41917f9-823b-46a5-b426-98700f4fa266)

- Congratulations, to launch program:
- ```python main.py```
# Macrodroid
After installing macrodroid you should go to templates page and search for Android-Intelligence without the whitespace at the end, or else it would not find it.
![IMG_20240712_132633](https://github.com/user-attachments/assets/591c59fb-58d8-4042-8da8-989f71fd7234)
After finding macro, click on it and add it to your library in the right bottom corner. Then go to home page and find quick tile settings. 
![IMG_20240712_134224](https://github.com/user-attachments/assets/e9b9979e-7543-4053-870f-4d0a83460a66)
Enable ANY button on the list, NAME IT and choose button setting
![IMG_20240712_134604](https://github.com/user-attachments/assets/888254fd-120e-4820-92e5-9889c660f30f)
Add your button to the menu
![IMG_20240712_135045](https://github.com/user-attachments/assets/a57210e7-9593-4c35-90e5-25314d8f86ca)
![IMG_20240712_135409](https://github.com/user-attachments/assets/46a2356b-ed6d-4b81-85d3-649d696b8fc3)
Go to macros menu -> click on Android-Intelligence macros -> tap on first trigger -> configure 
![IMG_20240715_074408](https://github.com/user-attachments/assets/e1d6c630-5da9-40f4-858a-bec35c78b8d3)
### Select your named tile
![IMG_20240715_074502](https://github.com/user-attachments/assets/3ba56136-e95a-428a-ada1-91ab276b6435)
### Choose first option
![IMG_20240715_074549](https://github.com/user-attachments/assets/c2403605-1bba-4a88-85f0-d6d361e13828)
Then open configuration for the second trigger -> Generate new device id
![IMG_20240716_092157](https://github.com/user-attachments/assets/ee43a3ba-614c-4965-92d4-e3cbcfed6def)

If python program in termux is still working then you are ready to go 😄
