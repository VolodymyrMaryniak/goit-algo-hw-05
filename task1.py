class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        for pair in self.table[key_hash]:
            if pair[0] == key:
                pair[1] = value
                return

        self.table[key_hash].append(key_value)

    def get(self, key):
        key_hash = self.hash_function(key)
        for pair in self.table[key_hash]:
            if pair[0] == key:
                return pair[1]

        return None

    def delete(self, key):
        key_hash = self.hash_function(key)

        for pair in self.table[key_hash]:
            if pair[0] == key:
                self.table[key_hash].remove(pair)
                return True

        return False


def main():
    H = HashTable(5)
    H.insert("apple", 10)
    H.insert("apple", 15)
    H.insert("orange", 20)
    H.insert("banana", 30)

    print(H.get("apple"))  # Виведе: 15
    print(H.get("orange"))  # Виведе: 20
    print(H.get("banana"))  # Виведе: 30

    H.delete("apple")
    print(H.get("apple"))  # Виведе: None


if __name__ == "__main__":
    main()
