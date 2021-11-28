import json

result = []

with open('Queries_Labeled_Valeria.json') as f:
  data = json.load(f)


for each in data['TREC']['DOC']:
    labels = {}
    labels = each['label']
    print("label: ", labels)
    result.append(labels)

f = open("Labels_IE1_SKB_derigval.txt", "a")

# Eliminate duplicates
result = list(dict.fromkeys(result))
f.write(str(result))
f.close()

back_json = json.dumps(result)
print("back_json: ", back_json)
