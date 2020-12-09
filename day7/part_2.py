from arango import ArangoClient
import json

def initialize_database(db):
    if db.has_collection('bags'):
        db.delete_collection('bags')
    db.create_collection('bags')

    if db.has_collection('contains'):
        db.delete_collection('contains')
    db.create_collection('contains', edge=True)

db = ArangoClient().db('_system')
initialize_database(db)

with open("input.txt", "r") as f:
    data = f.readlines()

data = [line.strip() for line in data]

bags = {}

for line in data:
    if "contain no other bags" in line:
        continue

    split = line.split(" ")
    outer_bag = " ".join(split[:2])
    inner_bags = split[4:]
    inner_bags = " ".join(inner_bags).split(',')
    inner_bags = [" ".join((bag.strip().replace('.', '').split(" ")[:-1])) for bag in inner_bags]

    if not bags.get(outer_bag):
        outer = db.insert_document('bags', {
            "name": outer_bag
        })

        bags[outer_bag] = outer['_id']

    for inner_bag in inner_bags:
        amount = inner_bag.split(" ")[0]
        bag_name = " ".join(inner_bag.split(" ")[1:])

        if not bags.get(bag_name):
            inserted = db.insert_document('bags', {
                "name": bag_name,
            })

            bags[bag_name] = inserted['_id']
        
        document = {
            "_from": bags[outer_bag],
            "_to": bags[bag_name],
            "amount": amount
        }

        db.insert_document('contains', document)


cursor = db.aql.execute("""
    FOR gold_bag IN bags
    FILTER gold_bag.name == 'shiny gold'
    
    FOR vertex, edge IN 1..20 OUTBOUND gold_bag contains
        RETURN {
            "amount": vertex.amount,
            "name": vertex.name,
            "other_amount": edge.amount
        }
    """
)

results = list(cursor.batch())
print(json.dumps(results, indent=2))