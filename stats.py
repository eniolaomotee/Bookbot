
def count_words(text:str) -> str:
    num_words = text.split()
    return f"Found {len(num_words)} total words"


def count_characters(text:str):
    count = {}
    texts = text.lower()
    
    for text in texts:
        if text.isalpha():
            count[text] = count.get(text, 0) + 1
        
        results = [{"char":char, "num":num} for char, num in count.items()]
    return results


def sorted_list(count: list):
    sorted_count = sorted(count, key=lambda x:x["num"], reverse=True)
    return sorted_count