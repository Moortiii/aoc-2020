from arango import ArangoClient

def initialize_database(db):
    if db.has_collection('bags'):
        db.delete_collection('bags')
    db.create_collection('bags')

    if db.has_collection('contains'):
        db.delete_collection('contains')
    db.create_collection('contains', edge=True)

db = ArangoClient().db('_system')
initialize_database(db)

with open("example_input.txt", "r") as f:
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
    inner_bags = [" ".join((bag.strip().replace('.', '').split(" ")[1:-1])) for bag in inner_bags]

    if not bags.get(outer_bag):
        outer = db.insert_document('bags', {
            "name": outer_bag
        })

        bags[outer_bag] = outer['_id']

    for inner_bag in inner_bags:
        if not bags.get(inner_bag):
            inserted = db.insert_document('bags', {
                "name": inner_bag
            })

            bags[inner_bag] = inserted['_id']
        
        document = {
            "_from": bags[outer_bag],
            "_to": bags[inner_bag],
        }

        db.insert_document('contains', document)


cursor = db.aql.execute("""
    FOR gold_bag IN bags
    FILTER gold_bag.name == 'shiny gold'
    
    FOR vertex, edge IN 1..20 INBOUND gold_bag contains
        RETURN DISTINCT vertex.name
    """
)

results = cursor.batch()
print("There are", len(results), "bags which eventually lead to a shiny gold bag.")