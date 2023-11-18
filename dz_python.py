#1
# text = input("Input current text: ")
# sentences = text.split('. ')
# capitalized_text = '. '.join(sentence.capitalize()for sentence in sentences)
# print(capitalized_text)
# count = 0
#
# for i in text:
#     if i.isdigit() is True:
#         count += 1
#         print(f"Digits used {count} times")
#
# count2 = 0
# temp = text.split()
# for i in range(len(temp)):
#     if temp[i].endswith(".") or temp[i].endswith(",") or temp[i].endswith(":") or temp[i].endswith("!") or temp[i].endswith(";") or temp[i].endswith("?"):
#         count2 += 1
#         print(f"Punctuation used {count2} times")
#
#
# count3 = 0
# temp2 = text.split()
# for i in range(len(temp2)):
#     if temp2[i].endswith("!"):
#         count3 += 1
#         print(f"! used {count3} times")
#2
# digits1 = input("Input digits: ")
# digits2 = input("Input current digit: ")
# print(digits1.count(digits2))
#3
# numbers = input("Input string of digits: ").split()
# numbers = [int(num) for num in numbers]
# sum_of_numbers = sum(numbers)
# average = sum_of_numbers / len(numbers) if len(numbers) > 0 else 0
# print(f"Sum: {sum_of_numbers}")
# print(f"Average: {average}")
