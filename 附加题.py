def compare_version(v1,v2):
    v1_list = v1.split('.')
    v2_list = v2.split('.')
    length = max(len(v1_list),len(v2_list))
    if len(v1_list)<length:
        v1_list.extend(['0']*(length-len(v1_list)))
    if len(v2_list)<length:
        v2_list.extend(['0']*(length-len(v2_list)))
    v1_list = [int(i) for i in v1_list]
    v2_list = [int(i) for i in v2_list]
    i = 0
    while i<len(v1_list):
        if v1_list[i]<v2_list[i]:
            return -1
        elif v1_list[i]>v2_list[i]:
            return 1
        else:
            i+=1
    return 0

if __name__ == "__main__":
    print(compare_version("0.1","1.1"))
    print(compare_version("1.0.1","1"))
    print(compare_version("7.5.2.4","7.5.3"))
    print(compare_version("1.01","1.001"))
    print(compare_version("1.0","1.0.0"))

