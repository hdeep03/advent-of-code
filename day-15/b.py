import sys

def main():
    data = sys.stdin.read()
    s = 0
    boxes = [[] for _ in range(256)]
    label_to_boxes = {}
    for x in data.split(","):
        if "=" in x:
            box, fl, label = parse_equal(x)
            if box in label_to_boxes.get(label, []):
                for i in range(len(boxes[box])):
                    if boxes[box][i][0] == label:
                        boxes[box][i] = (label, fl)
                        break
            else:
                boxes[box].append((label, fl))
                label_to_boxes[label] = label_to_boxes.get(label, []) + [box]
        else:
            label = x[:-1]
            for box in label_to_boxes.get(label, []):
                boxes[box] = list(filter(lambda x: x[0] != label, boxes[box]))
            
            label_to_boxes[label] = []


    for i, box in enumerate(boxes, 1):
        for j, (label, fl) in enumerate(box, 1):
            s+=i*j*fl
    print(s)


def parse_equal(text):
    left, right = text.split("=")
    return chash(left), int(right), left

def chash(text):
    val = 0
    for x in text:
        val+=ord(x)
        val*=17
        val = val % 256
    return val


main()