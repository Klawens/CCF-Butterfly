import json

f = open('./results.bbox.json', 'r')
dic = json.load(f)
res = {}
for key in range(94):
    res[str(key)] = []
for i, ann in enumerate(dic):
    print(i)
    img_id = ann['image_id']
    score = ann['score']
    bbox = ann['bbox']
    bbox[3] = bbox[3] + bbox[1]
    bbox[2] = bbox[2] + bbox[0]
    category_id = ann['category_id'] - 1
    obj = [img_id, score] + bbox
    res[str(category_id)].append(obj)
f1 = open("submission.json", "w")
json.dump(res, f1)
