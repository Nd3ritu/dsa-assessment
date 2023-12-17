import string
class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
        
def is_balanced(expression):
    stack = Stack()
    brackets = {'(' : ')', '[': ']', '{':'}'}

    for char in expression:
        if char in brackets.keys():
            stack.push(char)
        elif char in brackets.values():
            if stack.is_empty() or brackets[stack.pop()] != char:
                return False
            
    return stack.is_empty()

expression1 = "([]{})"
expression2 = "([])]"
print(is_balanced(expression1))
print(is_balanced(expression2))
        
def remove_duplicates(sequence):
    seen = set()
    result = []

    for item in sequence:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
sequence = [1,1,1,1,2,2,3,3,5]
no_dups = remove_duplicates(sequence)
print(no_dups)


def word_frequency(sentence):
    words = sentence.lower().translate(str.maketrans("","", string.punctuation)).split()
    freq_dict = {}
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    return freq_dict

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
        