from itertools import combinations
from collections import defaultdict


def scan_database(dataset, candidates, min_support_count):
    itemset_count = defaultdict(int)
    

    for transaction in dataset:
        for candidate in candidates:
            if candidate.issubset(transaction):
                itemset_count[candidate] += 1
    

    frequent_itemsets = {}
    for itemset, count in itemset_count.items():
        if count >= min_support_count:
            frequent_itemsets[itemset] = count
    
    return frequent_itemsets

def generate_candidates(frequent_itemsets):
    candidates = set()
    itemsets = list(frequent_itemsets.keys())
    num_itemsets = len(itemsets)
    

    for i in range(num_itemsets):
        for j in range(i + 1, num_itemsets):
            candidate = itemsets[i].union(itemsets[j])
            if len(candidate) == len(itemsets[i]) + 1:
                candidates.add(candidate)
    
    return candidates


def generate_association_rules(frequent_itemsets, min_confidence):
    rules = []
    
    for itemset in frequent_itemsets:
        subsets = [frozenset(x) for x in combinations(itemset, len(itemset) - 1)]
        
        for subset in subsets:
            
            if len(subset) == 0:
                continue
            
            rule = (subset, itemset - subset)
            support_count = frequent_itemsets[itemset]
            
            
            if len(subset) == 0:
                continue
            
            subset_support_count = frequent_itemsets.get(subset, 0)
            
            if subset_support_count > 0:
                confidence = support_count / subset_support_count
                if confidence >= min_confidence:
                    rules.append((subset, itemset - subset, confidence))
    
    return rules


dataset = [
    {'A', 'B', 'E'},
    {'B', 'D'},
    {'B', 'C'},
    {'A', 'B', 'D'},
    {'A', 'C'},
    {'B', 'C'},
    {'A', 'C'},
    {'A', 'B', 'C', 'E'},
    {'A', 'B', 'C'}
]


min_support_count = 2
min_confidence = 0.75  


C1 = [frozenset([item]) for transaction in dataset for item in transaction]
C1 = set(C1)  

L1 = scan_database(dataset, C1, min_support_count)


L = [L1]
k = 2
while True:
    Ck = generate_candidates(L[k - 2])
    Lk = scan_database(dataset, Ck, min_support_count)
    
    if not Lk:
        break
    
    L.append(Lk)
    k += 1


frequent_itemsets = {}
for level in L:
    frequent_itemsets.update(level)


association_rules = generate_association_rules(frequent_itemsets, min_confidence)


print("Frequent Itemsets:")
for itemset, count in frequent_itemsets.items():
    print(f"{set(itemset)}: {count} occurrences")

print("\nAssociation Rules:")
for rule in association_rules:
    print(f"{set(rule[0])} -> {set(rule[1])} with confidence = {rule[2]:.2f}")