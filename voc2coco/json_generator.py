import xml.etree.ElementTree as ET
import os
import json
import collections

coco = dict()
coco['images'] = []
coco['type'] = 'instances'
coco['annotations'] = []
coco['categories'] = []

# category_set = dict()
image_set = set()
image_id = 0  # train:2018xxx; val:2019xxx; test:2020xxx
category_item_id = 1
annotation_id = 1
category_set = ['巴黎翠凤蝶', '柑橘凤蝶', '玉带凤蝶', '碧凤蝶', '红基美凤蝶', '蓝凤蝶', '金裳凤蝶', '青凤蝶', '朴喙蝶', '密纹飒弄蝶', '小黄斑弄蝶', '无斑珂弄蝶',
                '直纹稻弄蝶', '花弄蝶', '隐纹谷弄蝶', '绢斑蝶', '虎斑蝶', '亮灰蝶', '咖灰蝶', '大紫琉璃灰蝶', '婀灰蝶', '曲纹紫灰蝶', '波太玄灰蝶', '玄灰蝶',
                '红灰蝶', '线灰蝶', '维纳斯眼灰蝶', '艳灰蝶', '蓝灰蝶', '青海红珠灰蝶', '古北拟酒眼蝶', '阿芬眼蝶', '拟稻眉眼蝶', '牧女珍眼蝶', '白眼蝶', '菩萨酒眼蝶',
                '西门珍眼蝶', '边纹黛眼蝶', '云粉蝶', '侏粉蝶', '大卫粉蝶', '大翅绢粉蝶', '宽边黄粉蝶', '山豆粉蝶', '橙黄豆粉蝶', '突角小粉蝶', '箭纹云粉蝶', '箭纹绢粉蝶',
                '红襟粉蝶', '绢粉蝶', '菜粉蝶', '镉黄迁粉蝶', '黎明豆粉蝶', '依帕绢蝶', '四川绢蝶', '珍珠绢蝶', '蛇目褐蚬蝶', '中环蛱蝶', '云豹蛱蝶', '伊诺小豹蛱蝶',
                '小红蛱蝶', '扬眉线蛱蝶', '斐豹蛱蝶', '曲斑珠蛱蝶', '柱菲蛱蝶', '柳紫闪蛱蝶', '灿福蛱蝶', '玄珠带蛱蝶', '珍蛱蝶', '琉璃蛱蝶', '白钩蛱蝶', '秀蛱蝶', '绢蛱蝶',
                '绿豹蛱蝶', '网蛱蝶', '美眼蛱蝶', '翠蓝眼蛱蝶', '老豹蛱蝶', '荨麻蛱蝶', '虬眉带蛱蝶', '蟾福蛱蝶', '钩翅眼蛱蝶', '银斑豹蛱蝶', '银豹蛱蝶', '链环蛱蝶',
                '锦瑟蛱蝶', '黄环蛱蝶', '黄钩蛱蝶', '黑网蛱蝶', '尖翅翠蛱蝶', '素弄蝶', '翠袖锯眼蝶', '蓝点紫斑蝶', '雅弄蝶',
                ]
'''
def addCatItem(name):
    global category_item_id
    category_item = dict()
    category_item['supercategory'] = 'none'
    category_item_id += 1
    category_item['id'] = category_item_id
    category_item['name'] = name
    coco['categories'].append(category_item)
    category_set[name] = category_item_id
    return category_item_id
'''


def addCatItem(name):
    '''
    增加json格式中的categories部分
    '''
    global category_item_id
    category_item = collections.OrderedDict()
    category_item['supercategory'] = 'none'
    category_item['id'] = category_item_id
    category_item['name'] = name
    coco['categories'].append(category_item)
    category_item_id += 1


def addImgItem(file_name, size):
    global image_id
    if file_name is None:
        raise Exception('Could not find filename tag in xml file.')
    if size['width'] is None:
        raise Exception('Could not find width tag in xml file.')
    if size['height'] is None:
        raise Exception('Could not find height tag in xml file.')
    # image_item = dict()    #按照一定的顺序，这里采用collections.OrderedDict()
    image_item = collections.OrderedDict()
    jpg_name = os.path.splitext(file_name)[0] + '.jpg'
    image_item['file_name'] = jpg_name
    image_item['width'] = size['width']
    image_item['height'] = size['height']
    image_item['id'] = image_id
    coco['images'].append(image_item)
    image_set.add(jpg_name)
    image_id = image_id + 1
    return image_id


def addAnnoItem(object_name, image_id, category_id, bbox):
    global annotation_id
    # annotation_item = dict()
    annotation_item = collections.OrderedDict()
    annotation_item['segmentation'] = []
    seg = []
    # bbox[] is x,y,w,h
    # left_top
    seg.append(bbox[0])
    seg.append(bbox[1])
    # left_bottom
    seg.append(bbox[0])
    seg.append(bbox[1] + bbox[3])
    # right_bottom
    seg.append(bbox[0] + bbox[2])
    seg.append(bbox[1] + bbox[3])
    # right_top
    seg.append(bbox[0] + bbox[2])
    seg.append(bbox[1])
    annotation_item['segmentation'].append(seg)
    annotation_item['area'] = bbox[2] * bbox[3]
    annotation_item['iscrowd'] = 0
    annotation_item['image_id'] = image_id
    annotation_item['bbox'] = bbox
    annotation_item['category_id'] = category_id
    annotation_item['id'] = annotation_id
    annotation_item['ignore'] = 0
    annotation_id += 1
    coco['annotations'].append(annotation_item)


def parseXmlFiles(xml_path):
    xmllist = os.listdir(xml_path)
    xmllist.sort()
    for f in xmllist:
        if not f.endswith('.xml'):
            continue

        bndbox = dict()
        size = dict()
        current_image_id = None
        current_category_id = None
        file_name = None
        size['width'] = None
        size['height'] = None
        size['depth'] = None

        xml_file = os.path.join(xml_path, f)
        print(xml_file)

        tree = ET.parse(xml_file)
        root = tree.getroot()  # 抓根结点元素

        if root.tag != 'annotation':  # 根节点标签
            raise Exception('pascal voc xml root element should be annotation, rather than {}'.format(root.tag))

        # elem is <folder>, <filename>, <size>, <object>
        for elem in root:
            current_parent = elem.tag
            current_sub = None
            object_name = None

            # elem.tag, elem.attrib，elem.text
            if elem.tag == 'folder':
                continue

            if elem.tag == 'filename':
                file_name = elem.text
                if file_name in category_set:
                    raise Exception('file_name duplicated')

            # add img item only after parse <size> tag
            elif current_image_id is None and file_name is not None and size['width'] is not None:
                if file_name not in image_set:
                    current_image_id = addImgItem(file_name, size)  # 图片信息
                    print('add image with {} and {}'.format(file_name, size))
                else:
                    raise Exception('duplicated image: {}'.format(file_name))
                    # subelem is <width>, <height>, <depth>, <name>, <bndbox>
            for subelem in elem:
                bndbox['xmin'] = None
                bndbox['xmax'] = None
                bndbox['ymin'] = None
                bndbox['ymax'] = None

                current_sub = subelem.tag
                if current_parent == 'object' and subelem.tag == 'name':
                    object_name = subelem.text
                    # if object_name not in category_set:
                    #    current_category_id = addCatItem(object_name)
                    # else:
                    # current_category_id = category_set[object_name]
                    current_category_id = category_set.index(object_name) + 1  # index默认从0开始,但是json文件是从1开始，所以+1
                elif current_parent == 'size':
                    if size[subelem.tag] is not None:
                        raise Exception('xml structure broken at size tag.')
                    size[subelem.tag] = int(subelem.text)

                # option is <xmin>, <ymin>, <xmax>, <ymax>, when subelem is <bndbox>
                for option in subelem:
                    if current_sub == 'bndbox':
                        if bndbox[option.tag] is not None:
                            raise Exception('xml structure corrupted at bndbox tag.')
                        bndbox[option.tag] = int(option.text)

                # only after parse the <object> tag
                if bndbox['xmin'] is not None:
                    if object_name is None:
                        raise Exception('xml structure broken at bndbox tag')
                    if current_image_id is None:
                        raise Exception('xml structure broken at bndbox tag')
                    if current_category_id is None:
                        raise Exception('xml structure broken at bndbox tag')
                    bbox = []
                    # x
                    bbox.append(bndbox['xmin'])
                    # y
                    bbox.append(bndbox['ymin'])
                    # w
                    bbox.append(bndbox['xmax'] - bndbox['xmin'])
                    # h
                    bbox.append(bndbox['ymax'] - bndbox['ymin'])
                    print(
                        'add annotation with {},{},{},{}'.format(object_name, current_image_id - 1, current_category_id,
                                                                 bbox))
                    addAnnoItem(object_name, current_image_id - 1, current_category_id, bbox)
    # categories部分
    for categoryname in category_set:
        addCatItem(categoryname)


if __name__ == '__main__':
    xml_path = '/home/lsc/datasets/butterfly/Annotations'
    json_file = '/home/lsc/datasets/butterfly/Annotations_/train.json'
    parseXmlFiles(xml_path)
json.dump(coco, open(json_file, 'w'))
