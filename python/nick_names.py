from collections import defaultdict

def preprocess_names(names):
    prefix_count = defaultdict(int)
    for name in names:
        # Add all prefixes of the current name to the dictionary
        for i in range(1, len(name) + 1):
            prefix = name[:i]
            prefix_count[prefix] += 1
    return prefix_count

def main():
    a = int(input())
    names = [input().strip() for _ in range(a)]
    b = int(input())
    nick_names = [input().strip() for _ in range(b)]
    
    # Preprocess the names to get the count of each prefix
    prefix_count = preprocess_names(names)
    
    # Get the count of names starting with each nickname
    list_ = [prefix_count[nick] for nick in nick_names]
    
    # Print the results
    for count in list_:
        print(count)

if __name__ == "__main__":
    main()
