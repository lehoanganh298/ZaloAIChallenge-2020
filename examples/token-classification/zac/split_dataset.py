from sklearn.model_selection import train_test_split
import json, codecs

with open('train/train.jsonl',encoding="utf-8") as f:
    train = [json.loads(jline) for jline in f.read().splitlines()]

X_train, X_test = train_test_split(train, test_size=0.2, random_state=1)

with codecs.open('train/train_split.jsonl', 'w', "utf-8") as f:
    for item in X_train:
        json.dump(item, f,ensure_ascii=False)
        f.write('\n')
with codecs.open('train/test_split.jsonl', 'w', "utf-8") as f:
    for item in X_test:
        json.dump(item, f,ensure_ascii=False)
        f.write('\n')

print(len(X_train),len(X_test))