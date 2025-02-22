from backend.util.crypto_hash import crypto_hash

def test_crypto_hash():
    # It should create the same hash with arguments of different data types in any order
    assert crypto_hash(1, [2], 'three') == crypto_hash('three', 1, [2])
    # It should create a unique hash when the properties have changed on an input
    assert crypto_hash(1) != crypto_hash(2)    
    # It should create a unique hash when the order of the properties have changed
    assert crypto_hash(1, 2, 3) != crypto_hash(3, 2, 1)    
    # It should create a unique hash for objects with the same properties but in a different order
    assert crypto_hash({'one': 1, 'two': 2}) != crypto_hash({'two': 2, 'one': 1})