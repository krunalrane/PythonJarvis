import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pygame
import random
import sys


engine = pyttsx3.init()
newVoiceRate = 155
engine.setProperty('rate',newVoiceRate)
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

MASTER = "Master!"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12:
        speak("Good Morning" + MASTER)
    
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + MASTER)

    else:
        speak("Good Evening" + MASTER)
    
    speak("what can i do for you?")

def takeCommand():
    #it takes microphone input form the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        print(e)
        print("say that again please....")
    return query
wishMe()
while True:
    query = takeCommand()


    if 'wikipedia' in query.lower():
        speak('Searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences =2)
        speak('According to wikipedia')
        print(results)
        speak(results)

    elif 'open youtube' in query.lower():
        #webbrowser.open("youtube.com")
        url = "youtube.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open google' in query.lower():
        #webbrowser.open("google.com")
        url = "google.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open facebook' in query.lower():
        #webbrowser.open("facebook.com")
        url = "facebook.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'weather in vadodara' in query.lower():
        #webbrowser.open("facebook.com")
        url = "https://www.google.com/search?q=weather+in+vadodara&oq=weather+in+vadodara&aqs=chrome..69i57j0l7.5309j1j7&sourceid=chrome&ie=UTF-8"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open amazon' in query.lower():
        #webbrowser.open("amazon.in")
        url = "amazon.in"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open flipkart' in query.lower():
        #webbrowser.open("flipkart.in")
        url = "flipkart.in"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'play music' in query.lower():
        songs_dir = "C:\\Users\\User\\Music\\english songs"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))
    elif 'open vs code' in query.lower():
        codePath = "D:\\users\\Microsoft VS Code\\code.exe"
        os.startfile(codePath)

    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime(":%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")
        print(strTime)

    elif 'quiz' in query.lower():
        

        question = [
            "Which is the longest river in the world, option A Amazon option B Nile option C Ganga",
            "Which is the biggest animal on the earth, option A Elephant option B Giraffe option c Blue Whale",
            "Who is the current president of India, option A Ramnath Kovind option B Pranab Mukhariji option c Narendra Modi",
            "Which is the fastest animal on the earth, option A Cheetah option B Horse option c dogs",
            "Which is the most popular programming language , option A C++ option B Python option c Java",
        ]
        speak(question[0])
        query = takeCommand()
        score = 0
        if 'b' in query.lower():
            score += 1
        speak(question[1])
        query = takeCommand()
        if 'option c' in query.lower():
            score += 1
        speak(question[2])
        query = takeCommand()
        if 'option a' in query.lower():
            score += 1
        speak(question[3])
        query = takeCommand()
        if 'option a' in query.lower():
            score += 1
        speak(question[4])
        query = takeCommand()
        if 'option c' in query.lower():
            score += 1
        speak(f"your score is: {score}")
        

    
    elif 'game' in query.lower():
        pygame.init()

        WIDTH = 800
        HEIGHT = 600

        RED = (255,0,0)
        BLUE = (0,0,255)
        YELLOW = (255,255,0)
        BACKGROUND_COLOR = (0,0,0)

        player_size = 50
        player_pos = [WIDTH/2, HEIGHT-2*player_size]

        enemy_size = 50
        enemy_pos = [random.randint(0,WIDTH-enemy_size), 0]
        enemy_list = [enemy_pos]

        SPEED = 10

        screen = pygame.display.set_mode((WIDTH, HEIGHT))

        game_over = False

        score = 0

        clock = pygame.time.Clock()

        myFont = pygame.font.SysFont("monospace", 35)

        def set_level(score, SPEED):
            if score < 20:
                SPEED = 5
            elif score < 40:
                SPEED = 8
            elif score < 60:
                SPEED = 12
            else:
                SPEED = 15
            return SPEED
            # SPEED = score/5 + 1


        def drop_enemies(enemy_list):
            delay = random.random()
            if len(enemy_list) < 10 and delay < 0.1:
                x_pos = random.randint(0,WIDTH-enemy_size)
                y_pos = 0
                enemy_list.append([x_pos, y_pos])

        def draw_enemies(enemy_list):
            for enemy_pos in enemy_list:
                pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

        def update_enemy_positions(enemy_list, score):
            for idx, enemy_pos in enumerate(enemy_list):
                if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
                    enemy_pos[1] += SPEED
                else:
                    enemy_list.pop(idx)
                    score += 1
            return score

        def collision_check(enemy_list, player_pos):
            for enemy_pos in enemy_list:
                if detect_collision(enemy_pos, player_pos):
                    return True
            return False

        def detect_collision(player_pos, enemy_pos):
            p_x = player_pos[0]
            p_y = player_pos[1]

            e_x = enemy_pos[0]
            e_y = enemy_pos[1]

            if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x+enemy_size)):
                if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y+enemy_size)):
                    return True
            return False

        while not game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:

                    x = player_pos[0]
                    y = player_pos[1]

                    if event.key == pygame.K_LEFT:
                        x -= player_size
                    elif event.key == pygame.K_RIGHT:
                        x += player_size

                    player_pos = [x,y]

            screen.fill(BACKGROUND_COLOR)

            drop_enemies(enemy_list)
            score = update_enemy_positions(enemy_list, score)
            SPEED = set_level(score, SPEED)

            text = "Score:" + str(score)
            label = myFont.render(text, 1, YELLOW)
            screen.blit(label, (WIDTH-200, HEIGHT-40))

            if collision_check(enemy_list, player_pos):
                game_over = True
                break

            draw_enemies(enemy_list)

            pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

            clock.tick(45)

            pygame.display.update()

    elif 'exit' in query.lower():
        break
                

    
