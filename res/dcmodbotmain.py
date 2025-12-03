import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from collections import Counter
import time
import os
import sys
import pyotp
import requests
import traceback
import subprocess
import asyncio
import pyautogui
import emoji
import sqlite3

dir = os.path.dirname(os.path.realpath(__file__))+"/"
os.chdir(dir)

dcBotScript = dir+f"dcBot4SubProcess.py"

url = input("Enter Livestream Popup Url: ")

options = ChromeOptions()
options.add_argument("--headless=new")

driver = uc.Chrome(use_subprocess=True, enable_cdp_events=True)
#driver = uc.Chrome(options=options)

# Load credentials from environment variables
mail = os.getenv("GOOGLE_MAIL")
password = os.getenv("GOOGLE_PASSWORD") 
secret_key = os.getenv("GOOGLE_2FA_SECRET")
dcBotToken = os.getenv("DISCORD_BOT_TOKEN")
dcBanChannelID = os.getenv("DISCORD_CHANNEL_ID")

streamID = url.split("v=")[1]

if not os.path.exists(dir+f"data/"+streamID):
    os.makedirs(dir+f"data/"+streamID)
    print(f"Folder '{dir}'data/{streamID}created successfully.")


#* DC BOT SUBPROCESS

process = subprocess.Popen(["python", dcBotScript], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(process.stdout)

def sendMessage2Discord(banText, banImage, dcChannelID):
    discordMessageApi = f'https://discord.com/api/v10/channels/{dcChannelID}/messages'
    headers = {
        'Authorization': f'Bot {dcBotToken}',
    }

    if banImage == "" or banImage == None:
        banImage = "./placeholder.png"
    if banText == "":
        banText = "Yazı Hatası"
    
    if banImage != "yok":
        with open(banImage, 'rb') as file:
            payload = {
                'content': banText,
            }

            files = {
                'file': (banImage, file, 'image/png'),  
            }

            response = requests.post(discordMessageApi, headers=headers, data=payload, files=files)
    else:
            payload = {
                'content': banText,
            }
            response = requests.post(discordMessageApi, headers=headers, data=payload)
    if response.status_code == 200:
        return('Message sent successfully')
    else:
        return(f'Failed to send message. Status code: {response.status_code}, Response: {response.text}')





singInURL = 'https://accounts.google.com/signin'
maxTries = 5
signedIn = False
def login2Google():
    driver.get(singInURL)
    time.sleep(3)

    for attempt in range(1, maxTries + 1):
        try:
            # Attempt to find the password input element
            email_input = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, 'identifierId'))
            )

            # If found, enter the password and submit
            email_input.send_keys(mail)
            email_input.send_keys(Keys.RETURN)

            # Break out of the loop if successful
            break

        except NoSuchElementException:
            # Element not found, wait and then retry
            time.sleep(3)

        except Exception as e:
            # Handle other exceptions
            print("Error at Mail (Attempt {}): {}".format(attempt, e))
    else:
        # If all attempts are unsuccessful, print an error message
        return("Failed to find the mail input element after {} attempts.".format(maxTries))
        driver.quit()

    time.sleep(3)

    for attempt in range(1, maxTries + 1):
        try:
            # Attempt to find the password input element
            password_input = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.NAME, 'Passwd'))
            )

            # If found, enter the password and submit
            password_input.send_keys(password)
            password_input.send_keys(Keys.RETURN)

            # Break out of the loop if successful
            break

        except NoSuchElementException:
            # Element not found, wait and then retry
            time.sleep(3)

        except Exception as e:
            # Handle other exceptions
            print("Error at Password (Attempt {}): {}".format(attempt, e))

    else:
        # If all attempts are unsuccessful, print an error message
        return("Failed to find the password input element after {} attempts.".format(maxTries))
        driver.quit()

    time.sleep(3)

    for attempt in range(1, maxTries + 1):
        try:
            # Attempt to find the password input element
            pressYesAuth = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//img[@src="https://ssl.gstatic.com/accounts/embedded/signin_tapyes.gif"]'))
            )

            # If found, enter the password and submit
            tryAnotherWay = driver.find_element(By.CLASS_NAME, 'VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-dgl2Hf ksBjEc lKxP2d LQeN7 BqKGqe eR0mzb TrZEUc lw1w4b')
            ActionChains(driver).move_to_element(tryAnotherWay).click().perform()

            # Break out of the loop if successful
            break

        except NoSuchElementException:
            # Element not found, wait and then retry
            time.sleep(3)

        except Exception as e:
            # Handle other exceptions
            print("Error at Try Another Way (Attempt {}): {}".format(attempt, e))

    else:
        # If all attempts are unsuccessful, print an error message
        print("Failed to find the Try Another Way element after {} attempts.".format(maxTries))


    time.sleep(3)

    for attempt in range(1, maxTries + 1):
        try:
            # Attempt to find the password input element
            authUlElements = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//ul[@class="Dl08I"]'))
            )

            # If found, enter the password and submit
            googleAuth = driver.find_element(By.XPATH, '//div[@class="VV3oRb" and .//strong[text()="Google Authenticator"]]').find_element(By.XPATH, '..').find_element(By.XPATH, '..')
            ActionChains(driver).move_to_element(googleAuth).click().perform()

            # Break out of the loop if successful
            break

        except NoSuchElementException:
            # Element not found, wait and then retry
            time.sleep(3)

        except Exception as e:
            # Handle other exceptions
            print("Error at Select Google Auth (Attempt {}): {}".format(attempt, e))

    else:
        # If all attempts are unsuccessful, print an error message
        return("Failed to find the Select Google Auth element after {} attempts.".format(maxTries))
        driver.quit()


    time.sleep(3)

    for attempt in range(1, maxTries + 1):
        try:
            # Attempt to find the password input element
            GoogleAuthElement = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="PrDSKc" and .//strong[text()="Google Authenticator"]]'))
            )

            # If found, enter the password and submit
            totp = pyotp.TOTP(secret_key)
            one_time_code = totp.now()
            totp_input = driver.find_element(By.NAME, 'totpPin')
            totp_input.send_keys(one_time_code)
            totp_input.send_keys(Keys.RETURN)

            # Break out of the loop if successful
            break

        except NoSuchElementException:
            # Element not found, wait and then retry
            time.sleep(3)

        except Exception as e:
            # Handle other exceptions
            print("Error at Write Google Auth (Attempt {}): {}".format(attempt, e))

    else:
        # If all attempts are unsuccessful, print an error message
        return("Failed to find the Write Google Auth element after {} attempts.".format(maxTries))
        driver.quit()

    time.sleep(3)
    global signedIn 
    signedIn = True
    return("Login Successful.")

while signedIn == False:
    loginResult = login2Google()
    print(loginResult)



driver.get(url)


def createImage(items, modName, modTimestamp):
    try:
        # Open the main image
        main_image = Image.new("RGB", (1280, 720), (66, 75, 84))
        positionX = 30
        positionY = 15

        draw = ImageDraw.Draw(main_image)

        fontSize = 25

        # Choose a font and size
        font_path = dir + f"arial-unicode-ms.ttf"  # You may need to adjust the font path
        font = ImageFont.truetype(font_path, fontSize)

        def writeTextWithLines(text, font, adjustmentPixel, textPosition, color):
            result_text = ""
            messageBreakLineIndexes = []
            resultTextLength = 0

            words = text.split()
            for word in words:
                # Check the width of the current line plus the next word
                word_width = draw.textlength(word, font=font)
                if resultTextLength + word_width <= adjustmentPixel:
                    # If the line isn't too wide, add the word to the line
                    result_text += word + " "
                    resultTextLength += word_width + draw.textlength(" ", font=font)  # Add space width
                else:
                    # If the line is too wide, break the line
                    result_text = result_text.rstrip()
                    messageBreakLineIndexes.append(len(result_text))
                    result_text += word + " "
                    resultTextLength = word_width + draw.textlength(" ", font=font)  # Reset line width

            for i in range(len(messageBreakLineIndexes)):
                index = messageBreakLineIndexes[i]
                result_text = result_text[:index+i] + "\n" + result_text[index+i:]
            draw.text(textPosition, result_text, font=font, fill=color)

            text_bbox = draw.textbbox(textPosition, result_text, font=font)

            # Extract width and height from the bounding box
            textWidth = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]

            return textWidth


        for i in range(len(items)):

            name = f'{items[i][3]} {items[i][4]}: '
            message = items[i][5]
            modName

            overlay_image_url = items[i][6]

            response = requests.get(overlay_image_url, timeout= (10, 10))
            overlay_image = Image.open(BytesIO(response.content))
            overlay_image = overlay_image.convert("RGBA")
            overlay_image = overlay_image.resize((64, 64))

            mask = Image.new("L", overlay_image.size, 0)
            draw_mask = ImageDraw.Draw(mask)
            draw_mask.ellipse((0, 0, overlay_image.width, overlay_image.height), fill=255)

            rounded_img = Image.new("RGBA", overlay_image.size, (0, 0, 0, 0))
            rounded_img.paste(overlay_image, (0, 0), mask)

            position = (positionX, positionY)
            main_image.paste(overlay_image, position, rounded_img)
            
            name_start_x = (rounded_img.width) + 50
            name_adjustment = (name_start_x + 25)

            # Draw the name text in green
            name_width = writeTextWithLines(name, font, name_adjustment, (name_start_x, position[1]), (15, 206, 128))

            #print("name: ", name_width)
            message_start_x = name_start_x + name_width + 25
            #print(message_start_x)
            
            # Draw the message text in white
            writeTextWithLines(message, font, main_image.width - message_start_x - 40, (message_start_x, (fontSize / 2) + position[1]), (255, 255, 255))

            main_image.paste(overlay_image, position, rounded_img)
            positionY += 125

        print("Image Created Successfully!")

        roundedRectangle = draw.rounded_rectangle(((positionX + rounded_img.width) / 2, positionY, (positionX + rounded_img.width) / 2 + 20, positionY + 60), radius=20, fill=0)

        if items[0][10] != None:
            banText = f'{items[0][4]} - {items[0][10]}, {modName} tarafından {modTimestamp} saatinde gizlendi.'
        else:
            banText = f'{items[0][4]}, {modName} tarafından {modTimestamp} saatinde gizlendi.'

        # Draw the ban text in black
        writeTextWithLines(banText, font, main_image.width - 200, (positionX + 60, positionY), (0, 0, 0))

        # Save the result
        main_image.save(dir+f'data/{streamID}/ban_{items[0][4].replace(":", "_")}.png')
        outputImage = str(dir+f'data/{streamID}/ban_{items[0][4].replace(":", "_")}.png')
    except:
        outputImage = str(dir+f'placeholder.png')
        try:
            if items[0][10] != None:
                banText = f'{items[0][4]} - {items[0][10]}, {modName} tarafından {modTimestamp} saatinde gizlendi.'
            else:
                banText = f'{items[0][4]}, {modName} tarafından {modTimestamp} saatinde gizlendi.'
        except:
            banText = "Ban Mesajı Hatası"
    return banText, outputImage



def change2AllChat():
    #change chat to all chat
    for attempt in range(1, maxTries + 1):
        try:
            chatTypeMenu = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//div[@id="trigger" and @class="style-scope tp-yt-paper-menu-button"]'))
            )
            ActionChains(driver).move_to_element(chatTypeMenu).click().perform()

            time.sleep(1)

            chatTypes = driver.find_elements(By.XPATH, '//div[@id="item-with-badge" and @class="style-scope yt-dropdown-menu"]')

            if chatTypes:
                # Click the last menu item
                allChatType = chatTypes[1]
                ActionChains(driver).move_to_element(allChatType).click().perform()

            # Break out of the loop if successful
            break

        except NoSuchElementException:
            # Element not found, wait and then retry
            time.sleep(5)

        except Exception as e:
            # Handle other exceptions
            print("Error at Changing Chat To All Chat (Attempt {}): {}".format(attempt, e))
    else:
        # If all attempts are unsuccessful, print an error message
        print("Failed to Change Chat To All Chat element after {} attempts.".format(maxTries))
        sys.exit()

def closePoll(tries):
    #close poll
    for attempt in range(1, tries + 1):
        try:
            pollMenu= WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//yt-live-chat-banner-manager[@id="live-chat-banner"]'))
            )
            driver.execute_script('arguments[0].style.display = "none";', pollMenu)
            break
        except:
            pass



db = sqlite3.connect(dir+f"data/chatData.sqlite3")
cursor = db.cursor()
cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS "{streamID}" (
    msgOrder INTEGER,
    msgType INTEGER,
    msgID TEXT PRIMARY KEY,
    timeStamp TEXT,
    name TEXT,
    message TEXT,
    img TEXT,
    chipBadgesSvg TEXT,
    chatBadgesSvg TEXT,
    memberBadge TEXT,
    memberTime TEXT,
    isDeleted INTEGER,
    moderator TEXT,
    banTime TEXT,
    banType TEXT);''')
db.commit()

change2AllChat()
time.sleep(3)

async def getMostCommonImg(bannedMessages):
    getMostCommonImg = Counter([item[6] for item in bannedMessages]).most_common(1)[0][0] 
    return getMostCommonImg

async def scrapeModMessage(div, lastID):
    #print("MOD MESSAGE")
    timeStamp = div.find("span", {"id":"timestamp"})
    timeStamp = timeStamp.text.strip()
    banMessage = div.find("yt-formatted-string", {"id":"message"}).find_all("span")
    bannedUser = banMessage[0].text.strip()
    bannedUser = emoji.demojize(bannedUser)
    moderator = banMessage[2].text.strip()
    moderator = emoji.demojize(moderator)
    banType = banMessage[-1].text.strip()
    banTime = None

    #print(bannedUser, " by ", moderator, " as ", banType)
    if banType == "tarafından gizlendi.":
        banType = "perma"
        banTime = "perma"
    elif banType == "saniye süreyle engellendi.":
        banType = "timeout"
        banTime = banMessage[-2].text.strip()
    elif banType == "tarafından kaldırıldı.":
        banType = "unban"

    cursor.execute(f'SELECT * FROM "{streamID}" WHERE msgID = ?', (lastID,))
    modMsgExists = cursor.fetchall()
    if len(modMsgExists) == 0:
        cursor.execute(f'SELECT COUNT(*) FROM "{streamID}"')
        tableLen = (cursor.fetchone())[0]
        messageOrder = tableLen + 1
        cursor.execute(f'INSERT INTO "{streamID}" (msgOrder, msgType, msgID, timeStamp, name, moderator, banTime, banType) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (messageOrder, 2, lastID, timeStamp, bannedUser, moderator, banTime, banType))
        db.commit()
        if banType == "perma":
            cursor.execute(f'SELECT * FROM ( SELECT * FROM "{streamID}" WHERE name = ? AND isDeleted = 1 AND msgOrder < ? ORDER BY msgOrder DESC LIMIT 5) AS reversed_results ORDER BY msgOrder ASC;', (bannedUser, messageOrder))
            bannedMessages = cursor.fetchall()

            mostCommonImg = await getMostCommonImg(bannedMessages)
            cursor.execute(f'SELECT * FROM ( SELECT * FROM "{streamID}" WHERE name = ? AND img = ? AND msgOrder < ? ORDER BY msgOrder DESC LIMIT 5) AS reversed_results ORDER BY msgOrder ASC;', (bannedUser, mostCommonImg, messageOrder))
            bannedMessages = cursor.fetchall()
            
            banText, banImage = createImage(bannedMessages, moderator, timeStamp)
            if banText == "Ban Mesajı Hatası":
                messageInput = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//div[@id="input" and @class="style-scope yt-live-chat-text-input-field-renderer"]'))
                )
                botMsg = 'Hello I am ModBot. I am sendıng thıs message because there ıs a error at Ban Text whıch ı send ıt to Moderator Dıscord Server!'
                messageInput.send_keys(botMsg)
                messageInput.send_keys(Keys.RETURN)
            
            if banImage.split("/")[-1] == "placeholder.png":
                messageInput = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//div[@id="input" and @class="style-scope yt-live-chat-text-input-field-renderer"]'))
                )
                botMsg = "Hello I am ModBot. I am sendıng thıs message because there ıs a error at Image whıch ı send ıt to Moderator Dıscord Server!"
                messageInput.send_keys(botMsg)
                messageInput.send_keys(Keys.RETURN)
            dcMessageResponse = sendMessage2Discord(banText, banImage, dcBanChannelID)
            print(dcMessageResponse)
        elif banType == "unban":
            dcMessageResponse = sendMessage2Discord(f'{bannedUser} kullanıcısının gizliliği, {moderator} tarafından {timeStamp} saatinde kaldırıldı.', "yok", dcBanChannelID)


async def scrapeMessage(div, lastID, isDeleted):
    name = div.find("span", {"id":"author-name"})
    name = name.text.strip()
    name = emoji.demojize(name)

    img = div.find(id="author-photo").find("img", {"id":"img"})
    img = img['src'].strip()
    timeStamp = div.find("span", {"id":"timestamp"})
    timeStamp = timeStamp.text.strip()
    chipBadgesSvg = None
    chatBadgesSvg = None
    membership = None
    chipBadgesSvg = div.find("span", {"id":"chip-badges"}).find("svg") #tik
    chatBadgesSvg = div.find("span", {"id":"chat-badges"}).find("svg") #mod ingiliz anahtarı
    if chipBadgesSvg:
        chipBadgesSvg = '`' + str(chipBadgesSvg).strip() + '`'
    else:
        chipBadgesSvg = None
    if chatBadgesSvg:
        chatBadgesSvg = '`' + str(chatBadgesSvg).strip() + '`'
    else:
        chatBadgesSvg = None
    messageDiv = div.find("span", {"id":"message"})

    msgImgContentDivs = messageDiv.find_all('img')
    message = str(messageDiv)

    for msgImgContent in msgImgContentDivs:
        msgEmoji = msgImgContent.get('alt', '')
        msgEmoji = emoji.demojize(msgEmoji)
        if msgEmoji[0] == ":":
            msgEmoji = msgEmoji[1:]
        if msgEmoji[-1] == ":":
            msgEmoji = msgEmoji[:-1]
        alt_attribute = ":"+msgEmoji+":"
        message = message.replace(str(msgImgContent), alt_attribute)
    messageSoup = BeautifulSoup(message, 'html.parser')
    message = messageSoup.find("span", {"id": "message"}).text

    membership = div.find("img", {"class":"yt-live-chat-author-badge-renderer"})
    if membership != None:
        memberBadge = membership['src']
        memberTime = membership['alt']
    else:
        memberBadge = None
        memberTime = None

    cursor.execute(f'SELECT * FROM "{streamID}" WHERE msgID = ?', (lastID,))
    msgExists = cursor.fetchall()

    if len(msgExists) == 0:
        cursor.execute(f'SELECT COUNT(*) FROM "{streamID}"')
        tableLen = cursor.fetchone()[0]
        messageOrder = tableLen + 1
        cursor.execute(f'INSERT INTO "{streamID}" (msgOrder, msgType, msgID, img, timeStamp, name, chipBadgesSvg, chatBadgesSvg, message, memberBadge, memberTime, isDeleted) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (messageOrder, 1, lastID, img, timeStamp, name, chipBadgesSvg, chatBadgesSvg, message, memberBadge, memberTime, isDeleted))
        db.commit()

closePoll(5)
async def scrape():
    try:
        closePoll(1)

        divs = driver.find_element(By.XPATH, "//div[@id='items' and @class='style-scope yt-live-chat-item-list-renderer']")
        divs = BeautifulSoup(divs.get_attribute("outerHTML"), "html5lib")
        divs = divs.find_all(attrs={"class":"style-scope yt-live-chat-item-list-renderer"})
        lastDiv = divs[-1]
        #print(lastDiv['id'])
        cursor.execute(f'SELECT * FROM "{streamID}" WHERE msgID = ?', (lastDiv['id'],))
        msgIDExists = cursor.fetchall()
        for div in divs:
            lastID = div['id']
            try:
                isDeleted = div.has_attr('is-deleted')
                if isDeleted:
                    isDeleted = 1
                else:
                    isDeleted = 0
            except:
                isDeleted = 1
            if isDeleted == 1:
                cursor.execute(f'UPDATE "{streamID}" SET isDeleted = 1 WHERE msgID = ?', (lastID,))
                db.commit()
            if len(msgIDExists) == 0:
                if div.name == "yt-live-chat-text-message-renderer":
                    await scrapeMessage(div, lastID, isDeleted)
                elif div.name == "yt-live-chat-moderation-message-renderer":
                    #* mod message fonksiyonunu çağır
                    await scrapeModMessage(div, lastID)
            
            try:
                isDeleted = div.has_attr('is-deleted')
                if isDeleted:
                    isDeleted = 1
                else:
                    isDeleted = 0
            except:
                isDeleted = 0
            if isDeleted == 1:
                cursor.execute(f'UPDATE "{streamID}" SET isDeleted = 1 WHERE msgID = ?', (lastID,))
        #print("waiting 5 sec")
        #time.sleep(5)
    except Exception as e:
            traceback.print_exc()
            time.sleep(2)

async def main():
    sendMessage2Discord(f'Çalışmak Beni Özgürleştirir...', dir + f'active.png', "1151847706654941246")
    while True:
        try:
            await scrape()
            #pyautogui.moveRel(1, 0, duration=0.1)
            #pyautogui.moveRel(-1, 0, duration=0.1)
        except KeyboardInterrupt:
            print("Script interrupted by user.")
            driver.quit()
            break

# Assuming you have an event loop, you can run the main coroutine like this:
asyncio.run(main())
