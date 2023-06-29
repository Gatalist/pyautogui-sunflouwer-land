import os


class SeedsHarvest:
    this_directory = os.getcwd()

    sunflower: dict = {
        "seed": 'sunflower.png',
        "harvest": 'sunflower.png'}
    potato: dict = {
        "seed": 'potato.png',
        "harvest": 'potato.png'}
    pumkin: dict = {
        "seed": 'pumkin.png',
        "harvest": 'pumkin.png'}
    carrot: dict = {
        "seed": 'carrot.png',
        "harvest": 'carrot.png'}
    cabbage: dict = {
        "seed": 'cabbage.png',
        "harvest": 'cabbage.png'}
    beetroot: dict = {
        "seed": 'beetroot.png',
        "harvest": 'beetroot.png'}
    cauliflower: dict = {
        "seed": 'cauliflower.png',
        "harvest": 'cauliflower.png'}
    parsnip: dict = {
        "seed": 'parsnip.png',
        "harvest": 'parsnip.png'}
    eggplant: dict = {
        "seed": 'eggplant.png',
        "harvest": 'eggplant.png'}
    radish: dict = {
        "seed": 'radish.png',
        "harvest": 'radish.png'}
    wheat: dict = {
        "seed": 'wheat.png',
        "harvest": 'wheat.png'}
    kale: dict = {
        "seed": 'kale.png',
        "harvest": 'kale.png'}
    blueberry: dict = {
        "seed": 'blueberry.png',
        "harvest": 'blueberry.png'}
    orange: dict = {
        "seed": 'orange.png',
        "harvest": 'orange.png'}
    apple: dict = {
        "seed": 'apple.png',
        "harvest": 'apple.png',}

    def get_seed_harvest(self, name):
        attr = getattr(self, name, None)
        attr['seed'] = os.path.join('image', 'seeds', attr['seed'])
        attr['harvest'] = os.path.join('image', 'harvest', name, attr['harvest'])
        return attr


class Captcha:
    this_directory = os.getcwd()
    path_folder = os.path.join(this_directory, 'image')
   
    def get_image_in_folder(self, name):
        path = os.path.join(self.path_folder, name)
        return [os.path.join('image', name, image) for image in os.listdir(path)] 
    
    