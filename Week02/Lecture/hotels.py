ids_to_hotelnames = dict()

f1 = open("hotels.txt")

for line in f1:
    line = line.strip()
    info = line.split("\t")
    id = info[0]
    hotel_name = info[1]
    ids_to_hotelnames[id] = hotel_name

f1.close()

ids_to_ratings = dict()
f2 =open("reviews.txt")
for line in f2:
    line = line.strip()
    info = line.split("\t")
    id = info[1]
    rating = int(info[-1])
    if id not in ids_to_ratings:
        ids_to_ratings[id] = [rating]
    else:
        ids_to_ratings[id].append(rating)
f2.close()

for k, v in ids_to_ratings.items():
    avg = sum(v) / len(v)
    ids_to_ratings[k] = avg


while len(ids_to_ratings) > 0:
    maxValue = max(ids_to_ratings.values())
    for id, rating in ids_to_ratings.items():
        if rating == maxValue:
            print(ids_to_hotelnames[id], rating)
            maxKey = id
            break
    ids_to_ratings.pop(maxKey)