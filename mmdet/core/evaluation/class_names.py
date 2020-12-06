import mmcv


def wider_face_classes():
    return ['face']


def voc_classes():
    return [
        'aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat',
        'chair', 'cow', 'diningtable', 'dog', 'horse', 'motorbike', 'person',
        'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor'
    ]


def imagenet_det_classes():
    return [
        'accordion', 'airplane', 'ant', 'antelope', 'apple', 'armadillo',
        'artichoke', 'axe', 'baby_bed', 'backpack', 'bagel', 'balance_beam',
        'banana', 'band_aid', 'banjo', 'baseball', 'basketball', 'bathing_cap',
        'beaker', 'bear', 'bee', 'bell_pepper', 'bench', 'bicycle', 'binder',
        'bird', 'bookshelf', 'bow_tie', 'bow', 'bowl', 'brassiere', 'burrito',
        'bus', 'butterfly', 'camel', 'can_opener', 'car', 'cart', 'cattle',
        'cello', 'centipede', 'chain_saw', 'chair', 'chime', 'cocktail_shaker',
        'coffee_maker', 'computer_keyboard', 'computer_mouse', 'corkscrew',
        'cream', 'croquet_ball', 'crutch', 'cucumber', 'cup_or_mug', 'diaper',
        'digital_clock', 'dishwasher', 'dog', 'domestic_cat', 'dragonfly',
        'drum', 'dumbbell', 'electric_fan', 'elephant', 'face_powder', 'fig',
        'filing_cabinet', 'flower_pot', 'flute', 'fox', 'french_horn', 'frog',
        'frying_pan', 'giant_panda', 'goldfish', 'golf_ball', 'golfcart',
        'guacamole', 'guitar', 'hair_dryer', 'hair_spray', 'hamburger',
        'hammer', 'hamster', 'harmonica', 'harp', 'hat_with_a_wide_brim',
        'head_cabbage', 'helmet', 'hippopotamus', 'horizontal_bar', 'horse',
        'hotdog', 'iPod', 'isopod', 'jellyfish', 'koala_bear', 'ladle',
        'ladybug', 'lamp', 'laptop', 'lemon', 'lion', 'lipstick', 'lizard',
        'lobster', 'maillot', 'maraca', 'microphone', 'microwave', 'milk_can',
        'miniskirt', 'monkey', 'motorcycle', 'mushroom', 'nail', 'neck_brace',
        'oboe', 'orange', 'otter', 'pencil_box', 'pencil_sharpener', 'perfume',
        'person', 'piano', 'pineapple', 'ping-pong_ball', 'pitcher', 'pizza',
        'plastic_bag', 'plate_rack', 'pomegranate', 'popsicle', 'porcupine',
        'power_drill', 'pretzel', 'printer', 'puck', 'punching_bag', 'purse',
        'rabbit', 'racket', 'ray', 'red_panda', 'refrigerator',
        'remote_control', 'rubber_eraser', 'rugby_ball', 'ruler',
        'salt_or_pepper_shaker', 'saxophone', 'scorpion', 'screwdriver',
        'seal', 'sheep', 'ski', 'skunk', 'snail', 'snake', 'snowmobile',
        'snowplow', 'soap_dispenser', 'soccer_ball', 'sofa', 'spatula',
        'squirrel', 'starfish', 'stethoscope', 'stove', 'strainer',
        'strawberry', 'stretcher', 'sunglasses', 'swimming_trunks', 'swine',
        'syringe', 'table', 'tape_player', 'tennis_ball', 'tick', 'tie',
        'tiger', 'toaster', 'traffic_light', 'train', 'trombone', 'trumpet',
        'turtle', 'tv_or_monitor', 'unicycle', 'vacuum', 'violin',
        'volleyball', 'waffle_iron', 'washer', 'water_bottle', 'watercraft',
        'whale', 'wine_bottle', 'zebra'
    ]


def imagenet_vid_classes():
    return [
        'airplane', 'antelope', 'bear', 'bicycle', 'bird', 'bus', 'car',
        'cattle', 'dog', 'domestic_cat', 'elephant', 'fox', 'giant_panda',
        'hamster', 'horse', 'lion', 'lizard', 'monkey', 'motorcycle', 'rabbit',
        'red_panda', 'sheep', 'snake', 'squirrel', 'tiger', 'train', 'turtle',
        'watercraft', 'whale', 'zebra'
    ]


def coco_classes():
    return [
        '巴黎翠凤蝶', '柑橘凤蝶', '玉带凤蝶', '碧凤蝶', '红基美凤蝶', '蓝凤蝶', '金裳凤蝶', '青凤蝶', 
        '朴喙蝶', '密纹飒弄蝶', '小黄斑弄蝶', '无斑珂弄蝶', '直纹稻弄蝶', '花弄蝶', '隐纹谷弄蝶', 
        '绢斑蝶', '虎斑蝶', '亮灰蝶', '咖灰蝶', '大紫琉璃灰蝶', '婀灰蝶', '曲纹紫灰蝶', '波太玄灰蝶', 
        '玄灰蝶', '红灰蝶', '线灰蝶', '维纳斯眼灰蝶', '艳灰蝶', '蓝灰蝶', '青海红珠灰蝶', '古北拟酒眼蝶', 
        '阿芬眼蝶', '拟稻眉眼蝶', '牧女珍眼蝶', '白眼蝶', '菩萨酒眼蝶', '西门珍眼蝶', '边纹黛眼蝶', 
        '云粉蝶', '侏粉蝶', '大卫粉蝶', '大翅绢粉蝶', '宽边黄粉蝶', '山豆粉蝶', '橙黄豆粉蝶', '突角小粉蝶', 
        '箭纹云粉蝶', '箭纹绢粉蝶', '红襟粉蝶', '绢粉蝶', '菜粉蝶', '镉黄迁粉蝶', '黎明豆粉蝶', '依帕绢蝶', 
        '四川绢蝶', '珍珠绢蝶', '蛇目褐蚬蝶', '中环蛱蝶', '云豹蛱蝶', '伊诺小豹蛱蝶', '小红蛱蝶', 
        '扬眉线蛱蝶', '斐豹蛱蝶', '曲斑珠蛱蝶', '柱菲蛱蝶', '柳紫闪蛱蝶', '灿福蛱蝶', '玄珠带蛱蝶', 
        '珍蛱蝶', '琉璃蛱蝶', '白钩蛱蝶', '秀蛱蝶', '绢蛱蝶', '绿豹蛱蝶', '网蛱蝶', '美眼蛱蝶', 
        '翠蓝眼蛱蝶', '老豹蛱蝶', '荨麻蛱蝶', '虬眉带蛱蝶', '蟾福蛱蝶', '钩翅眼蛱蝶', '银斑豹蛱蝶', 
        '银豹蛱蝶', '链环蛱蝶', '锦瑟蛱蝶', '黄环蛱蝶', '黄钩蛱蝶', '黑网蛱蝶', '尖翅翠蛱蝶', '素弄蝶', 
        '翠袖锯眼蝶', '蓝点紫斑蝶', '雅弄蝶'
    ]


def cityscapes_classes():
    return [
        'person', 'rider', 'car', 'truck', 'bus', 'train', 'motorcycle',
        'bicycle'
    ]


dataset_aliases = {
    'voc': ['voc', 'pascal_voc', 'voc07', 'voc12'],
    'imagenet_det': ['det', 'imagenet_det', 'ilsvrc_det'],
    'imagenet_vid': ['vid', 'imagenet_vid', 'ilsvrc_vid'],
    'coco': ['coco', 'mscoco', 'ms_coco'],
    'wider_face': ['WIDERFaceDataset', 'wider_face', 'WDIERFace'],
    'cityscapes': ['cityscapes']
}


def get_classes(dataset):
    """Get class names of a dataset."""
    alias2name = {}
    for name, aliases in dataset_aliases.items():
        for alias in aliases:
            alias2name[alias] = name

    if mmcv.is_str(dataset):
        if dataset in alias2name:
            labels = eval(alias2name[dataset] + '_classes()')
        else:
            raise ValueError(f'Unrecognized dataset: {dataset}')
    else:
        raise TypeError(f'dataset must a str, but got {type(dataset)}')
    return labels
