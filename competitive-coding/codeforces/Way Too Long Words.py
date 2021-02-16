# Input
# 4
# word
# localization
# internationalization
# pneumonoultramicroscopicsilicovolcanoconiosis
#
# Output
# word
# l10n
# i18n
# p43s

numberOfInputs = int(input())
out = []

for word in range(numberOfInputs):
    word = input()
    if len(word) > 10:
        output = word[0] + str(len(word)-2) + word[-1]
    else:
        output = word
    out.append(output)

for outp in out:
    print(outp)
