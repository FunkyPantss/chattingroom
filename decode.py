import base64

with open('c:/Users/Administrator/Desktop/decode.txt', 'r') as f:
    with open('result.txt', 'w') as fw:
        while True:
            line = f.readline()
            if not line:
                break
            print(base64.b64decode(line))
            fw.write(base64.b64decode(line).decode('utf-8'))