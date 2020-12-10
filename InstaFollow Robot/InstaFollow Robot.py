# Import requiements
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

MyUserName = "MEU USERNAME AQUI"
MyPassword = "MINHA SENHA AQUI"

# Create our class
class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox(executable_path = 'geckodriver.exe')

    def login(self):
        bot = self.bot
        # Navigate to the Instagram login page
        bot.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)

        # Find the email and password boxes, enter our login credentials
        email = bot.find_element_by_name('username').send_keys(self.username)
        password = bot.find_element_by_name('password').send_keys(self.password)

        # Wait for 1 second then press ENTER
        time.sleep(1)
        bot.find_element_by_name('password').send_keys(Keys.RETURN)

        # Wait 3 second while the post-login page loads
        time.sleep(3)

    def findMyFollowers(self, number_of_followers):
        bot = self.bot
        bot.get('https://instagram.com/' + self.username)
        time.sleep(2)
        bot.find_element_by_xpath('//a[@href="/' + self.username + '/followers/"]').click()
        time.sleep(1)
        popup = bot.find_element_by_class_name('isgrP')
        followers_array = []
        i = 1
        print("findMyFollowers:", i)

        while len(followers_array) <= number_of_followers:
            bot.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', popup)
            time.sleep(0.4)
            followers = bot.find_elements_by_class_name('FPmhX')

            for follower in followers:
                if follower not in followers_array:
                    followers_array.append(follower.text)

                i+=1
                print(followers_array)
                print("While followers_array:", i)

                self.followers = followers_array

    def followTheirFollowers(self, number_to_follow):
        bot = self.bot
        FollowLimit = 0

        for follower in self.followers:
            bot.get('https://instagram.com/' + follower)
            time.sleep(2)

            if(len(bot.find_elements_by_xpath("//*[contains(text(), 'Esta conta é privada')]")) > 0):
                # If they're private, we can't see their follower list, so skip them
                continue

            bot.find_element_by_xpath('//a[@href="/' + follower + '/followers/"]').click()
            time.sleep(3)

            follow = bot.find_elements_by_xpath("//button[contains(text(), 'Seguir')]")

            i = 1
            print("FollowTheirFollowers", i)

            for follower in follow:
                if(i != 1):
                        bot.execute_script("arguments[0].click();", follower)

                if(25 < number_to_follow):
                    break

                i+=1
                print("Followers in Follow:", i)
                print("Number To Follow:", number_to_follow)

                FollowLimit += 1
                print("Follow Limit:", FollowLimit)

                if (FollowLimit == 29):
                    # 6 minutos de espera para seguir mais 29
                    print(">>> Você chegou ao limite!")
                    SleepTime = 60 * 6
                    time.sleep(SleepTime)
                    break

insta = InstagramBot(MyUserName, MyPassword)
insta.login()
insta.findMyFollowers(5)
insta.followTheirFollowers(10)
