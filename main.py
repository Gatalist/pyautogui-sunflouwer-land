import pyautogui, keyboard, os
from settings import SeedsHarvest, Captcha


class Garden(SeedsHarvest, Captcha):
    def __init__(self, name):
        self.obj_seed_harvest = self.get_seed_harvest(name)
        self.seed = self.obj_seed_harvest['seed']
        self.harvest = self.obj_seed_harvest['harvest']
        self.basket: str = os.path.join('image', 'basket.png')
        self.close_basket: str = os.path.join('image', 'close_x.png')
        self.close_long_btn: str = os.path.join('image', 'close_long_btn.png')
        self.garden_free_land: str = os.path.join('image', 'land', 'garden_free_land.png')

    # садить урожай 
    def plant_garden_seeds(self):
        free_land = pyautogui.locateOnScreen(self.garden_free_land, confidence=0.9)
        if free_land:
            pyautogui.click(free_land)
            print("Сажаем урожай")

    # собрать урожай
    def reap_harvest(self):
        found_harvest = pyautogui.locateOnScreen(self.harvest, confidence=0.65)
        if found_harvest:
            # pyautogui.moveTo(0, 20)
            print(pyautogui.position())
            pyautogui.click(found_harvest)
            pyautogui.sleep(0.1)

    # выбрать семена
    def take_seeds(self):
        basket = pyautogui.locateOnScreen(self.basket, confidence=0.7)
        pyautogui.click(basket)
        pyautogui.sleep(0.5)
        seed = pyautogui.locateOnScreen(self.seed, confidence=0.7)
        pyautogui.click(seed)
        close = pyautogui.locateOnScreen(self.close_basket, confidence=0.7)
        pyautogui.click(close)
        pyautogui.sleep(0.3)

    # закрываем окно
    def close_popap(self: str):
        close = pyautogui.locateOnScreen(self.close_long_btn, confidence=0.7)
        if close:
            pyautogui.click(close)
            pyautogui.sleep(0.3)

    # проверяем нет ли капчи на экране
    def check_captcha(self):
        stop_image = self.get_image_in_folder('stop')
        for image in stop_image:
            print(image)
            check = pyautogui.locateOnScreen(image, confidence=0.7)
            if check:
                if image.find("goblin") != -1:
                    print("search - goblin")
                    goblin_image = self.get_image_in_folder('goblin')
                    self.searche_image(goblin_image)
                if image.find("seekers") != -1:
                    print("search - seeker")
                    seekers_image = self.get_image_in_folder('seekers')
                    self.searche_image(seekers_image)
                if image.find("box") != -1:
                    print("search - box")
                    box_image = self.get_image_in_folder('box')
                    self.searche_image(box_image)

    # перебираем выбранные изображения
    def searche_image(self, captcha_image):
        for image in captcha_image:
            print(image)
            click_image = pyautogui.locateOnScreen(image, confidence=0.7)
            if click_image:
                pyautogui.click(click_image)
                pyautogui.sleep(0.2)
            self.close_popap()


# выбираем какаой урожай нужно собирать
garden = Garden(name='potato')

def start():
    garden.take_seeds()
    while keyboard.is_pressed("esc")==False:
        garden.reap_harvest()
        garden.check_captcha()
        garden.plant_garden_seeds()

start()