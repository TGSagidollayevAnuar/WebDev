def cat_dog(str):
    cnt1 = 0
    cnt2 = 0
    for i in range(0, len(str) - 2):
        if str[i] + str[i + 1] + str[i + 2] == "cat":
            cnt1 += 1
    for i in range(0, len(str) - 2):
        if str[i] + str[i + 1] + str[i + 2] == "dog":
            cnt2 += 1
    if cnt1 == cnt2:
        return True
    return False
