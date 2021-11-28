import json

result = []

with open('Queries_Labeled_Claudio.json') as f:
  data = json.load(f)


for each in data['documents']:
    labels = {}
    labels = each['labels']
    result.append(labels)

# Convert list of lists to flat list
flat_result = []
for i in result:
    for j in i:
        flat_result.append(j)

f = open("Labels_IE1_SKB_ansalcla.txt", "a")

# Eliminate duplicates
flat_result = list(dict.fromkeys(flat_result))

f.write(str(flat_result))
f.close()

back_json = json.dumps(flat_result)
print(back_json)
