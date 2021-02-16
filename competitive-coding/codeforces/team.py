problemsCount = int(input())

response_list = []

for responses in range(problemsCount):
    response_list.append(input())

answerableSolutions = 0

for response in response_list:
    response1 = int(response.split(' ')[0])
    response2 = int(response.split(' ')[1])
    response3 = int(response.split(' ')[2])

    if response1 + response2 + response3 > 1:
        answerableSolutions += 1

print(answerableSolutions)

